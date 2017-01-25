import boto3
import json

BUCKET_NAME='codurance-site-pr'
FOLDER_FORMAT='site-%s/'

def lambda_handler(event, context):
    parsed_message = parse_message(event)
    if (is_closed_pr(parsed_message)):
        branch_name = parse_branch_name(parsed_message)
        print(branch_name)
        return delete_objects_of_branch(branch_name)
    else:
        return 'PR event is not closed'

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

def delete_objects_of_branch(branch_name):
    s3 = boto3.resource('s3')
    objects_to_delete = objects_of_branch(s3, branch_name)
    if objects_to_delete:
        delete_objects_of_bucket(s3, objects_to_delete)
        return 'Deleted %s folder' %branch_name
    else:
        return 'Could not delete the folder with name: %s' %branch_name

def objects_of_branch(s3, branch_name):
    #paginator = boto3.Session.client(service_name='s3').get_paginator("list_objects")
    paginator = boto3.client('s3').get_paginator('list_objects')
    page_iterator = paginator.paginate(Bucket = BUCKET_NAME, Prefix = FOLDER_FORMAT %branch_name)

    bucket_object_list = []
    i = 0
    for page in page_iterator:
        if i == 0:
            print("ad")
            print(page)
        else:
            break
    #   bucket_object_list.append(page['Contents'])
       # for key in page[ "Contents" ]:
       #    keyString = key[ "Key" ]
       #    bucket_object_list.append(keyString)
    #s3.meta.client.list_objects(Bucket=BUCKET_NAME, Prefix=FOLDER_FORMAT %branch_name)

def delete_objects_of_bucket(s3, objects):
    delete_keys = {'Objects' : []}
    delete_keys['Objects'] = [{'Key' : k} for k in [obj['Key'] for obj in objects.get('Contents', [])]]
    print(delete_keys)
    #s3.meta.client.delete_objects(Bucket=BUCKET_NAME, Delete=delete_keys)
