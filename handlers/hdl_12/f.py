import google_auth_oauthlib
import pyasn1
import rsa
import typing_extensions
import urllib3
def f(event):
    try:
        return event
    except Exception as e:
        return {{'error': str(e)}}
        