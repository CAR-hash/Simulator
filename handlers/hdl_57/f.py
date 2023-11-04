import awscli
import charset_normalizer
import dateutil
import docutils
import idna
import numpy
import packaging
import pyasn1
def f(event):
    try:
        return event
    except Exception as e:
        return {{'error': str(e)}}
        