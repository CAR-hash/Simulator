import botocore
import jmespath
import oauthlib
def f(event):
    try:
        return event
    except Exception as e:
        return {{'error': str(e)}}
        