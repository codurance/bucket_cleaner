import boto3
import json

BUCKET_NAME='codurance-site-pr'
FOLDER_FORMAT='site-%s/'

def lambda_handler(event, context):
    parsed_message = parse_message(event)
    if (is_closed_pr(parsed_message)):
        branch_name = parse_branch_name(parsed_message)
        paginator = get_bucket_paginator()
        objects_to_delete = objects_of_branch(paginator, branch_name)
        delete_objects_of_bucket(get_s3client(), objects_to_delete)
    else:
        return 'PR event is not closed'

def get_bucket_paginator():
    return boto3.client('s3').get_paginator('list_objects')

def get_s3client():
    return s3.meta.client

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
    page_iterator = paginator.paginate(Bucket = BUCKET_NAME, Prefix = FOLDER_FORMAT %branch_name)

    return reduce(lambda page, acc: page + acc, page_iterator, [])

def extract_object_keys(objects):
    return [{'Key' : k} for k in [obj['Key']
        for obj in objects.get('Contents', [])]]

def delete_objects_of_bucket(s3client, keys):
    s3client.delete_objects(Bucket=BUCKET_NAME, Delete={'Objects' : keys})
