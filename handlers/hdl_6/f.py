import cryptography
import idna
import numpy
import six
import urllib3
def f(event):
    try:
        return event
    except Exception as e:
        return {{'error': str(e)}}
        