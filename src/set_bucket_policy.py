"""Set bucket policy"""
import argparse
import os

from common import basic

PARSER = argparse.ArgumentParser()
PARSER.add_argument('--bucket', help='Name of the destination bucket.', required=True)
PARSER.add_argument('--policy_path', help='Path to policy file.', required=True)

ARGUMENTS = PARSER.parse_args()
CLIENT = basic.get_s3()

BUCKET_POLICY = CLIENT.BucketPolicy(ARGUMENTS.bucket)

POLICY_FILE = open(ARGUMENTS.policy_path, 'r')
POLICY_FILE_CONTENTS = POLICY_FILE.readlines()

print BUCKET_POLICY.policy

NEW_POLICY = POLICY_FILE_CONTENTS.format(ARGUMENTS.bucket)

print NEW_POLICY
