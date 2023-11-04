import dateutil
import google_auth_oauthlib
import rsa
import typing_extensions
def f(event):
    try:
        return event
    except Exception as e:
        return {{'error': str(e)}}
        