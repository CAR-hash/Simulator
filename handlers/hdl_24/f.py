import certifi
import jmespath
def f(event):
    try:
        return event
    except Exception as e:
        return {{'error': str(e)}}
        