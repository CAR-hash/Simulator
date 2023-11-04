import certifi
import dateutil
import google_auth_oauthlib
def f(event):
    try:
        return event
    except Exception as e:
        return {{'error': str(e)}}
        