import certifi
import charset_normalizer
import google_auth_oauthlib
import numpy
import oauthlib
import pytz
import rsa
import s3transfer
import setuptools
import wheel
def f(event):
    try:
        return event
    except Exception as e:
        return {{'error': str(e)}}
        