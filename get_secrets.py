# Use this code snippet in your app.
# If you need more information about configurations or implementing the sample code, visit the AWS docs:
# https://aws.amazon.com/developers/getting-started/python/
import json
import os


def get_secret_from_file():
    try:
        with open('/secret/env.json') as f:
            txt = json.load(f)
            return txt
    except:
        return


def retrieve_secret(secret_name):
    return os.environ.get('SATOSHI') or get_secret_from_file() or 'FAILED'
