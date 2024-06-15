import boto3
import os

def create_queues(queue_names, endpoint_url):
    # Create a new session using default AWS credentials
    session = boto3.Session()

    # Create an SQS client with the specified endpoint URL
    sqs = session.client('sqs', endpoint_url=endpoint_url)

    for queue_name in queue_names:
        try:
            response = sqs.create_queue(QueueName=queue_name)
            print(f'Queue created: {queue_name}, URL: {response["QueueUrl"]}')
        except Exception as e:
            print(f'Error creating queue {queue_name}: {e}')

if __name__ == '__main__':
    endpoint_url = 'http://localhost:4566'
    file = open('fileQueue.txt', 'r')
    file_data = file.read()
    file.close()
    queue_names = file_data.split(',')

    create_queues(queue_names, endpoint_url)