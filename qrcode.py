import png
import pyqrcode
import boto3
import uuid
import json
import os
from pyqrcode import QRCode

s3 = boto3.client('s3')

def img_process():
    
    source_Bucket_name = os.environ['SourceBucket']
    object_name = os.environ['ObjectName']
    Dest_Bucket_name = os.environ['DestinationBucket']

    
    
    s = 'https://{0}.s3.amazonaws.com/{1}'.format (source_Bucket_name,object_name)
    url = pyqrcode.create(s)        
    url.svg(" /tmp/file.svg", scale = 8)
    with open("/tmp/file.svg", "rb") as f:
        s3.upload_fileobj(f, Dest_Bucket_name, "{}.svg".format (object_name))
    return True

img_process()
