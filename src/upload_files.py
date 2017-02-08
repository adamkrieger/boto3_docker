"""Upload files"""
import argparse
import os

from common import basic, filesys, msg

PARSER = argparse.ArgumentParser()
PARSER.add_argument('--bucket', help='Name of the destination bucket.', required=True)
PARSER.add_argument('--dir', help='Path to directory being uploaded.', required=True)

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

FILES = filesys.get_files_recursively(ARGUMENTS.dir)

print msg.notification("Uploading files.")

for each in FILES:
    path_src, path_dest = each
    print msg.notification("Uploading... "),
    print path_src + msg.notification(' to ') + path_dest,
    __upload_file__(BUCKET, path_src, path_dest, CONTENT_TYPES)
    print msg.success("DONE")
