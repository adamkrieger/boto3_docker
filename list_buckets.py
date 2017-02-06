"""Basic AWS Operations"""
from common import basic

CLIENT = basic.get_client()
BUCKETS = CLIENT.list_buckets()['Buckets']

for each in BUCKETS:
    print each['Name']
