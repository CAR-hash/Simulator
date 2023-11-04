import botocore
import charset_normalizer
import idna
import jmespath
import matplotlib
import numpy
import packaging
import pyasn1_modules
import pytz
import requests
def f(event):
    try:
        return event
    except Exception as e:
        return {{'error': str(e)}}
        