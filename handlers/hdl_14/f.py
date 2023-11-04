import awscli
import jmespath
import oauthlib
import setuptools
import typing_extensions
def f(event):
    try:
        return event
    except Exception as e:
        return {{'error': str(e)}}
        