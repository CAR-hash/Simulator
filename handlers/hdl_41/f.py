import pyasn1_modules
import wheel
def f(event):
    try:
        return event
    except Exception as e:
        return {{'error': str(e)}}
        