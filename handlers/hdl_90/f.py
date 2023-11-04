import jmespath
import numpy
import pip
import pyasn1
def f(event):
    try:
        return event
    except Exception as e:
        return {{'error': str(e)}}
        