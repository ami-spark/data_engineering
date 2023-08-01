from nacl import public
from pip._internal.cli.cmdoptions import python
from snowflake.snowpark._internal.analyzer.analyzer_utils import FROM, COPY

# FROM public.ecr.aws/lambda/python:3.9
# COPY *.py requirements.txt ./
# RUN python.9 -m pip install -r requirements.txt -t .
# CMD ["app.lambda_handler"]


# FROM python:3.9
# COPY *.py requirements.txt ./
# RUN python3.9 -m pip install -r requirements.txt -t .
# CMD ["python", "./app.py"]