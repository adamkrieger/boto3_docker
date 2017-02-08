"""Basic AWS Operations"""
import boto3
import os

def get_s3():
    """Returns an s3 client"""
    client = boto3.client(
        's3',
        aws_access_key_id=os.environ.get('AWS_ACCESS_KEY'),
        aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY')
    )

    return client
    
