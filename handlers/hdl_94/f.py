import botocore
import jmespath
import xlwt
def f(event):
    try:
        return event
    except Exception as e:
        return {{'error': str(e)}}
        