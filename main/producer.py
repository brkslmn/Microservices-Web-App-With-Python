import pika, json

params = pika.URLParameters('amqps://htytdqxk:QZL0E4NV42kecmdWTiTSdBK4rgMoWRFy@roedeer.rmq.cloudamqp.com/htytdqxk')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)
