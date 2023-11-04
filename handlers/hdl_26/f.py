import google_auth_oauthlib
import pyasn1_modules
def f(event):
    try:
        return event
    except Exception as e:
        return {{'error': str(e)}}
        