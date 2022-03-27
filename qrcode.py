import png
import pyqrcode
import boto3
import uuid
import json
from pyqrcode import QRCode

s3 = boto3.client('s3')

def img_process():
    
    source_Bucket_name = 'SOURCE_BUCKET'
    object_name = 'OBJECY_KEY'
    Dest_Bucket_name = 'DEST_BUCKET'

    
    
    s = 'https://{0}.s3.amazonaws.com/{1}'.format (Bucket_name,object_name)
    url = pyqrcode.create(s)        
    url.svg(" file.svg", scale = 8)
    with open("file.svg", "rb") as f:
        s3.upload_fileobj(f, Dest_Bucket_name, "{}.svg".format (object_name))
    return True

img_process()
