"""List all buckets (it's boo`kay!)"""
from common import basic

CLIENT = basic.get_s3()
BUCKETS = CLIENT.list_buckets()['Buckets']

for each in BUCKETS:
    print each['Name']
