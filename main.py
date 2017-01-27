import boto3
from eventparser import parse
from s3objectlister import object_keys_for_branch
from s3objectdeleter import delete_objects_for_keys

BUCKET_NAME='codurance-site-pr'

def lambda_handler(event, context):
    (is_pr_closed, branch_name) = parse(event)
    if (is_pr_closed):
        object_keys = object_keys_for_branch(get_bucket_paginator(), BUCKET_NAME, branch_name)
        delete_objects_for_keys(get_s3_client(), BUCKET_NAME, object_keys)
        return 'Site preview has been deleted'
    else:
        return 'PR event is not closed'

def get_s3_client():
    return boto3.resource('s3').meta.client

def get_bucket_paginator():
    return boto3.client('s3').get_paginator('list_objects')
