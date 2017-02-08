"""Upload files"""
import argparse

from common import basic

PARSER = argparse.ArgumentParser()
PARSER.add_argument('--bucket', help='Name of the destination bucket.', required=True)

def upload_file(client, bucket_name, file_src, file_dest):
    client.upload_file(file_src, bucket_name, file_dest)

ARGUMENTS = PARSER.parse_args()
CLIENT = basic.get_s3()

upload_file(CLIENT, ARGUMENTS.bucket, './tmp/index.html', 'index.html')
upload_file(CLIENT, ARGUMENTS.bucket, './tmp/404.html', '404.html')
