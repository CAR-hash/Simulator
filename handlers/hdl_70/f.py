import cachetools
import certifi
import idna
import packaging
import xlwt
def f(event):
    try:
        return event
    except Exception as e:
        return {{'error': str(e)}}
        