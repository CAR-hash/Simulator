import packaging
import pip
import pytz
import rsa
def f(event):
    try:
        return event
    except Exception as e:
        return {{'error': str(e)}}
        