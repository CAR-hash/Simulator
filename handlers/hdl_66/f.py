import botocore
import certifi
import charset_normalizer
import dateutil
import jmespath
import xlwt
import pyasn1
import s3transfer
import six
import typing_extensions
def f(event):
    try:
        return event
    except Exception as e:
        return {{'error': str(e)}}
        