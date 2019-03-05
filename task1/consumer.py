import pika
import logging
import sys


def callback(ch, method, properties, body):
	logging.info("Received %s" % body.decode("utf-8"))


def main():
	logging.basicConfig(stream=sys.stdout, level=logging.INFO,
		format="%(message)s")
	
	with pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq', 
		retry_delay=2, connection_attempts=10)) as connection:
		channel = connection.channel()
		channel.queue_declare(queue='promprog-task1')
		channel.basic_consume(callback, queue='promprog-task1', no_ack=True)
		channel.start_consuming()


if __name__ == '__main__':
	main()