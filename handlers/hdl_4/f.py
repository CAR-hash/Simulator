import boto3
import botocore
import cachetools
import google_auth_oauthlib
import jmespath
import pyasn1
import pyasn1_modules
import requests
import s3transfer
import six
def f(event):
    try:
        return event
    except Exception as e:
        return {{'error': str(e)}}
        