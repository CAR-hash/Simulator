import awscli
import jmespath
import numpy
import packaging
import pyasn1
import setuptools
import six
def f(event):
    try:
        return event
    except Exception as e:
        return {{'error': str(e)}}
        