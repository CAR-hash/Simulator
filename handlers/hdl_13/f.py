import awscli
import boto3
import google_auth_oauthlib
import jmespath
import matplotlib
def f(event):
    try:
        return event
    except Exception as e:
        return {{'error': str(e)}}
        