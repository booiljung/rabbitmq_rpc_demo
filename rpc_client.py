import numpy as np
import pickle
import pika
import time
import uuid

class RpcClient(object):

    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self.channel = self.connection.channel()
        result = self.channel.queue_declare(queue='', exclusive=True)
        self.callback_queue = result.method.queue
        self.channel.basic_consume(on_message_callback=self.on_response, auto_ack=True, queue=self.callback_queue)


    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body


    def __call__(self, arr):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        body = pickle.dumps(arr)
        self.channel.basic_publish(
                exchange='',
                routing_key='my_rpc_queue',
                properties=pika.BasicProperties(
                        reply_to = self.callback_queue,
                        correlation_id = self.corr_id,
                ),
                body=body)
        while self.response is None:
            self.connection.process_data_events()
            time.sleep(0.01)
        return pickle.loads(self.response)

