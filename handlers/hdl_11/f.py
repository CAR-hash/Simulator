import boto3
import botocore
import certifi
import charset_normalizer
import cryptography
import jmespath
import numpy
import packaging
import setuptools
import typing_extensions
def f(event):
    try:
        return event
    except Exception as e:
        return {{'error': str(e)}}
        