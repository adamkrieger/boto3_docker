"""Set bucket policy"""
import argparse
from jinja2 import Template

from common import basic

PARSER = argparse.ArgumentParser()
PARSER.add_argument('--bucket', help='Name of the destination bucket.', required=True)
PARSER.add_argument('--policy_path', help='Path to policy file.', required=True)

ARGUMENTS = PARSER.parse_args()
STHREE = basic.get_s3_resource()

BUCKET_POLICY = STHREE.BucketPolicy(ARGUMENTS.bucket)

POLICY_FILE = open(ARGUMENTS.policy_path, 'r')
POLICY_FILE_CONTENTS = "".join(POLICY_FILE.readlines())
POLICY_TEMPLATE = Template(POLICY_FILE_CONTENTS)

print BUCKET_POLICY.policy

NEW_POLICY = POLICY_TEMPLATE.render(bucket=ARGUMENTS.bucket)

print NEW_POLICY
