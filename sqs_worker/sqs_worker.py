import logging
from typing import Any, Callable

import boto3

process_fn = Callable[[dict[str, Any]], None]


class AwsQueueProcessor:
    aws_region: str
    aws_account_id: str
    sqs_queue_name: str

    def __init__(self, aws_region: str, aws_account_id: str, queue_name: str):
        self.aws_region = aws_region
        self.aws_account_id = aws_account_id
        self.sqs_queue_name = queue_name

        self.sqs = boto3.client("sqs")

    # @property
    # def sns_topic_arn(self) -> str:
    #     return f"arn:aws:sns:{self.aws_region}:{self.aws_account_id}:{self.queue_name}"

    @property
    def queue_url(self) -> str:
        return f"https://sqs.{self.aws_region}.amazonaws.com/{self.aws_account_id}/{self.sqs_queue_name}"

    def register_message_process_function(self, function: process_fn) -> None:
        self.process_function = function

    def run_process_loop(self) -> None:
        # Here you can implement the logic to continuously process messages from the queue.
        # For now, let's just call the registered function in a loop.
        logger = logging.getLogger()
        while True:
            logger.info(
                f"Polling message for SQS queue",
                extra={
                    "queue_url": self.queue_url,
                },
            )
            # message = self.get_message_from_queue()
            # if message is None:
            #     break
            # self.process_function(message)
