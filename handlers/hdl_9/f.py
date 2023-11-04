import jmespath
import jmespath
import pip
def f(event):
    try:
        return event
    except Exception as e:
        return {{'error': str(e)}}
        