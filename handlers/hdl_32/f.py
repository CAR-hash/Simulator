import awscli
import boto3
import certifi
import charset_normalizer
import matplotlib
import packaging
import pyasn1_modules
def f(event):
    try:
        return event
    except Exception as e:
        return {{'error': str(e)}}
        