import awscli
import xlwt
import setuptools
def f(event):
    try:
        return event
    except Exception as e:
        return {{'error': str(e)}}
        