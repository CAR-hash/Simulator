import botocore
import cachetools
import idna
import jmespath
import numpy
import packaging
import pip
import requests
import rsa
import urllib3
def f(event):
    try:
        return event
    except Exception as e:
        return {{'error': str(e)}}
        