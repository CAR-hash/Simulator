import botocore
import s3transfer
def f(event):
    try:
        return event
    except Exception as e:
        return {{'error': str(e)}}
        