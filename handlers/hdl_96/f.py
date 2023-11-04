import docutils
import oauthlib
import s3transfer
import setuptools
import yaml
def f(event):
    try:
        return event
    except Exception as e:
        return {{'error': str(e)}}
        