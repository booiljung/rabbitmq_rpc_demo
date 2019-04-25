# clear message buffer

import pika


class RpcClear(object):

    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='my_rpc_queue')
        self.channel.basic_qos(prefetch_count=1)
        self.channel.basic_consume(on_message_callback=self.on_request, queue='my_rpc_queue')
        print(" [x] Awaiting RPC requests")
        self.channel.start_consuming()


    def on_request(self, ch, method, props, body):
        ch.basic_publish(exchange='',
                        routing_key=props.reply_to,
                        properties = pika.BasicProperties(correlation_id = props.correlation_id),
                        body="")
        ch.basic_ack(delivery_tag = method.delivery_tag)


if __name__ == "__main__":
    clear = RpcClear()
