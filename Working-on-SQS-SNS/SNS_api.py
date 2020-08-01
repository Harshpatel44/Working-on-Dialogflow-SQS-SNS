import boto3
import SQS_api
import time

def send_sns(message):
    sns = boto3.client('sns')
    sns.publish(TopicArn = "arn:aws:sns:us-east-1:832544204593:Order-delievery",
            Message = message)

def fetch_messages_and_notify():
    time.sleep(300)
    try:
        url = SQS_api.get_queue_url('assignmentserverless')
        receipt_handle, message, contact = SQS_api.get_message(url)
        print('message fetched')
        send_sns(message)
        print('message sent')
        SQS_api.delete_message(url, receipt_handle)
        print('message deleted')
    except Exception as e:
        print(e)


while True:
    fetch_messages_and_notify()