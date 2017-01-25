import boto3
import json

BUCKET_NAME='codurance-site-pr'
FOLDER_FORMAT='site-%s/'

def lambda_handler(event, context):
    parsed_message = parse_message(event)
    if (is_closed_pr(parsed_message)):
        branch_name = parse_branch_name(parsed_message)
        paginator = get_bucket_paginator()
        objects = objects_of_branch(paginator, branch_name)
        object_keys = extract_object_keys(objects)
        delete_objects_for_keys(get_s3client(), object_keys)
    else:
        return 'PR event is not closed'

def get_bucket_paginator():
    return boto3.client('s3').get_paginator('list_objects')

def get_s3client():
    return boto3.resource('s3').meta.client

def parse_branch_name(parsed_message):
    ref = parsed_message['ref']
    branch_name = ref[ref.rindex('/')+1:]
    return branch_name

def is_closed_pr(parsed_message):
    return parsed_message['deleted'] == True

def parse_message(event):
    message = event['Records'][0]['Sns']['Message']
    parsed_message = json.loads(message)
    return parsed_message

def objects_of_branch(paginator, branch_name):
    page_iterator = paginator.paginate(Bucket=BUCKET_NAME, Prefix=FOLDER_FORMAT %branch_name)

    return reduce(lambda acc, page: page['Contents'] + acc, page_iterator, [])

def extract_object_keys(objects):
    return [{'Key' : k} for k in [obj['Key']
        for obj in objects]]

def delete_objects_for_keys(s3client, keys):
    for chunk in chunks(keys, 1000):
        s3client.delete_objects(Bucket=BUCKET_NAME, Delete={'Objects' : chunk})

def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]
