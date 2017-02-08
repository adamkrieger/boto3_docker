"""Set bucket policy"""
import argparse
from jinja2 import Template
from botocore.exceptions import ClientError

from common import basic
from common import msg

PARSER = argparse.ArgumentParser()
PARSER.add_argument('--bucket', help='Name of the destination bucket.', required=True)
PARSER.add_argument('--policy_path', help='Path to policy file.', required=True)

def get_existing_bucket_policy(bucket_policy):
    """Gets existing bucket policy, returns None if not set."""
    existing_policy = None

    try:
        existing_policy = bucket_policy.policy
    except ClientError as ex:
        if "NoSuchBucketPolicy" in str(ex):
            pass
        else:
            raise

    return existing_policy

ARGUMENTS = PARSER.parse_args()
STHREE = basic.get_s3_resource()

BUCKET_POLICY = STHREE.BucketPolicy(ARGUMENTS.bucket)
EXISTING_POLICY = get_existing_bucket_policy(BUCKET_POLICY)

print msg.notification("Existing policy: ")
print EXISTING_POLICY

POLICY_FILE = open(ARGUMENTS.policy_path, 'r')
POLICY_FILE_CONTENTS = "".join(POLICY_FILE.readlines())
POLICY_TEMPLATE = Template(POLICY_FILE_CONTENTS)

NEW_POLICY = POLICY_TEMPLATE.render(bucket=ARGUMENTS.bucket)

BUCKET_POLICY.put(Policy=NEW_POLICY)

print msg.success("New policy:")
print NEW_POLICY
