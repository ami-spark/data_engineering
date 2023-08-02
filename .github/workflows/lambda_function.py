import boto3
import os
from debugpy._vendored.pydevd._pydevd_bundle.pydevd_command_line_handling import handler
from jupyter_server.terminal import initialize
from pyspark.sql import context

import business_logic

# Call the initialization code
initialize()


def handler(event, context):
    pass
# ...
# Call the business logic
# ...
