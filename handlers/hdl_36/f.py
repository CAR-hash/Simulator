import botocore
import cryptography
import dateutil
import idna
import numpy
import oauthlib
import s3transfer
import typing_extensions
import yaml
def f(event):
    try:
        return event
    except Exception as e:
        return {{'error': str(e)}}
        