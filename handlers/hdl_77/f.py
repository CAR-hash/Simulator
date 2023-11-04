import boto3
import jmespath
import oauthlib
import packaging
import xlwt
import pyasn1
import pytz
import typing_extensions
import urllib3
import wheel
def f(event):
    try:
        return event
    except Exception as e:
        return {{'error': str(e)}}
        