import aws
import boto3
# import aws_sdk
import os

from statsmodels.stats.libqsturng.make_tbls import success

import business_logic

QUEUE_URL = os.environ['QUEUE_URL']
BATCH_SIZE = os.environ.get('BATCH_SIZE', 1)
sqs_client = aws.sdk.client('sqs')


def handle_message(message):
    pass


def main():
    # Infinite loop to poll for messages from SQS
    while True:

        # Receive a batch of messages from the queue
        response = sqs_client.receive_message(
            QueueUrl=QUEUE_URL,
            MaxNumberOfMessages=BATCH_SIZE,
            WaitTimeSeconds=20)

        # Loop over the messages in the batch
        entries = []
        i = 1
        for message in response.get('Messages', []):

            # Process a single message
            handle_message(message)

            # Append the message handle to an array that is later
            # used to delete processed messages

            if success:
                entries.append(
                    {
                        'Id': f'index{i}',
                        'ReceiptHandle': message['receiptHandle']
                    }
                )
                i += 1

        # Delete all the processed messages
        if len(entries) > 0:
            sqs_client.delete_message_batch(
                QueueUrl=QUEUE_URL,
                Entries=entries
            )
