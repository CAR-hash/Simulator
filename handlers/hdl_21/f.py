import awscli
import packaging
import xlwt
import pyasn1_modules
import urllib3
def f(event):
    try:
        return event
    except Exception as e:
        return {{'error': str(e)}}
        