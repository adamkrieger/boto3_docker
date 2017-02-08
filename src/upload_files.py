"""Upload files"""
import argparse
import os

from common import basic

PARSER = argparse.ArgumentParser()
PARSER.add_argument('--bucket', help='Name of the destination bucket.', required=True)

def __upload_file__(bucket, file_src, file_dest, content_types):
    extra_args = {}

    _, file_extension = os.path.splitext(file_src)

    if file_extension in content_types:
        extra_args['ContentType'] = content_types[file_extension]

    bucket.upload_file(file_src, file_dest, ExtraArgs=extra_args)

CONTENT_TYPES = {
    ".html": "text/html",
    ".xml": "text/xml",
    ".css": "text/css"
}

ARGUMENTS = PARSER.parse_args()
STHREE = basic.get_s3_resource()
BUCKET = STHREE.Bucket(ARGUMENTS.bucket)

__upload_file__(BUCKET, './tmp/index.html', 'index.html', CONTENT_TYPES)
__upload_file__(BUCKET, './tmp/404.html', '404.html', CONTENT_TYPES)
