import boto3
import pip
import pytz
def f(event):
    try:
        return event
    except Exception as e:
        return {{'error': str(e)}}
        