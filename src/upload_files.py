"""Upload files"""
import argparse

from common import basic

PARSER = argparse.ArgumentParser()
PARSER.add_argument('--bucket', help='Name of the destination bucket.', required=True)

def __upload_file__(bucket, file_src, file_dest):
    extra_args = {}

    if file_src.endswith('.html'):
        extra_args['ContentType'] = 'text/html'

    bucket.upload_file(file_src, file_dest, ExtraArgs=extra_args)

ARGUMENTS = PARSER.parse_args()
STHREE = basic.get_s3_resource()
BUCKET = STHREE.Bucket(ARGUMENTS.bucket)

__upload_file__(BUCKET, './tmp/index.html', 'index.html')
__upload_file__(BUCKET, './tmp/404.html', '404.html')
