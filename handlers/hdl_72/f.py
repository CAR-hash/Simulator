import xlwt
import pyasn1_modules
import requests
def f(event):
    try:
        return event
    except Exception as e:
        return {{'error': str(e)}}
        