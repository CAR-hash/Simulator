import awscli
import boto3
import botocore
import charset_normalizer
import packaging
import rsa
def f(event):
    try:
        return event
    except Exception as e:
        return {{'error': str(e)}}
        