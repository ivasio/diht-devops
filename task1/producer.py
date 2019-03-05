import time
import random
import pika


def main():
	with pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq', 
		retry_delay=2, connection_attempts=10)) as connection:
		channel = connection.channel()
		channel.queue_declare(queue='promprog-task1')
		while True:
			channel.basic_publish(exchange='', routing_key='promprog-task1',
				body=str(random.randint(0, 1000)))
			time.sleep(random.randint(1, 4))


if __name__ == '__main__':
	main()