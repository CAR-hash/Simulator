import cryptography
import docutils
import six
def f(event):
    try:
        return event
    except Exception as e:
        return {{'error': str(e)}}
        