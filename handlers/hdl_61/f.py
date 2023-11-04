import matplotlib
import numpy
import packaging
import requests
def f(event):
    try:
        return event
    except Exception as e:
        return {{'error': str(e)}}
        