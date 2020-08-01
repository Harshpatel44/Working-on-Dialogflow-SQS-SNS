import boto3
from orders import Orders
import time

def create_que(queue_name):
    # Create SQS client
    sqs = boto3.client('sqs')

    # Create a SQS queue
    response = sqs.create_queue(
        QueueName=queue_name,
        Attributes={
            'DelaySeconds': '60',
            'MessageRetentionPeriod': '86400'
        }
    )
    return response['QueueUrl']

def get_queue_url(queue_name):
    sqs = boto3.client('sqs')
    response = sqs.get_queue_url(QueueName=queue_name)
    return response['QueueUrl']

def delete_queue(url):
    sqs = boto3.client('sqs')
    sqs.delete_queue(QueueUrl = url)


# 'https://sqs.us-east-1.amazonaws.com/832544204593/serverlessAssignment.fifo'
def send_message(url, messageAttribute, message):
    sqs = boto3.client('sqs')

    response = sqs.send_message(QueueUrl=url, DelaySeconds=10,MessageAttributes= messageAttribute,
    MessageBody=(
        message
        )
    )
    return response['MessageId']

def get_message(url):
    sqs = boto3.client('sqs')
    response = sqs.receive_message(
        QueueUrl = url,
        AttributeNames=[
        'SentTimestamp'
    ],MessageAttributeNames=[
        'All'
    ],
    )
    print(response)
    receipt_handle = response['Messages'][0]['ReceiptHandle']
    message = response['Messages'][0]['Body']
    contact = response['Messages'][0]["MessageAttributes"]["Contact"]["StringValue"]
    print(message,contact)
    return receipt_handle,message,contact

def delete_message(url,receipt_handle):
    time.sleep(10)
    sqs = boto3.client('sqs')
    sqs.delete_message(QueueUrl = url, ReceiptHandle = receipt_handle)
    print('message deleted')




messageAttribute = {
    'Contact': {
            'DataType': 'String',
            'StringValue': 'harsh.patel@dal.ca'
        }
}


if __name__ == '__main__':
    url = create_que('assignmentserverless')
    url = get_queue_url('assignmentserverless')
    while True:
        print(send_message(url, messageAttribute, Orders().random_message()))


