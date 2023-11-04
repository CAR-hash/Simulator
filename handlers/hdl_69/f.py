import charset_normalizer
import docutils
import jmespath
import matplotlib
import pip
import requests
import rsa
import typing_extensions
import urllib3
def f(event):
    try:
        return event
    except Exception as e:
        return {{'error': str(e)}}
        