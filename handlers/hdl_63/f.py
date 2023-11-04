import jmespath
import pip
import pyasn1
import wheel
def f(event):
    try:
        return event
    except Exception as e:
        return {{'error': str(e)}}
        