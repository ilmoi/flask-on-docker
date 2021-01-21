# Use this code snippet in your app.
# If you need more information about configurations or implementing the sample code, visit the AWS docs:
# https://aws.amazon.com/developers/getting-started/python/
import json
import os

import boto3
import base64
from botocore.exceptions import ClientError


# def get_secret(secret_name):
#     print('im called!!!')
#     region_name = "us-east-2"
#
#     session = boto3.session.Session()
#     client = session.client(
#         service_name='secretsmanager',
#         region_name=region_name
#     )
#
#     get_secret_value_response = client.get_secret_value(
#         SecretId=secret_name
#     )
#
#     if 'SecretString' in get_secret_value_response:
#         secret = get_secret_value_response['SecretString']
#     else:
#         decoded_binary_secret = base64.b64decode(get_secret_value_response['SecretBinary'])
#
#     return json.loads(secret) or decoded_binary_secret


def get_secret_from_file():
    try:
        with open ('env.json') as f:
            txt = json.load(f)
            return txt
    except:
        return


def get_from_env_or_ssm(secret_name):
    print('================ RUNNING VERSION: V2')
    return os.environ.get('SATOSHI') or get_secret_from_file() or 'FAILED'