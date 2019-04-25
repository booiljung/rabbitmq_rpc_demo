from keras.models import load_model
import numpy as np
import pickle
import pika

import custom_layers

class RpcServer(object):

    def __init__(self):
        print(" [x] Loading model...")
        self.model = self.load_model()
        print(" [x] Model loaded")

        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='my_rpc_queue')
        self.channel.basic_qos(prefetch_count=1)
        self.channel.basic_consume(on_message_callback=self.on_request, queue='my_rpc_queue')
        print(" [x] Awaiting RPC requests")
        self.channel.start_consuming()


    def on_request(self, ch, method, props, body):
        image = pickle.loads(body)
        print(" [.] on_request. predict image {} {}".format(type(image), image.shape))
        pred = self.model.predict(image)
        print(" [.] on_request. predicted image {} {}".format(type(pred), pred.shape))
        response = pickle.dumps(pred)

        ch.basic_publish(exchange='',
                        routing_key=props.reply_to,
                        properties = pika.BasicProperties(correlation_id = props.correlation_id),
                        body=response)
        ch.basic_ack(delivery_tag = method.delivery_tag)


    def load_model():
      # load your model here
      return model

if __name__ == "__main__":
    server = RpcServer()
