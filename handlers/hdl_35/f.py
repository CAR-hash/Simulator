import cachetools
import certifi
import charset_normalizer
import cryptography
import matplotlib
import pip
import pytz
def f(event):
    try:
        return event
    except Exception as e:
        return {{'error': str(e)}}
        