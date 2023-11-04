import awscli
import boto3
import cachetools
import requests
import typing_extensions
import wheel
def f(event):
    try:
        return event
    except Exception as e:
        return {{'error': str(e)}}
        