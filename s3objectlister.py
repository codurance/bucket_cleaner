import boto3

FOLDER_FORMAT='site-%s/'

def object_keys_for_branch(paginator, bucket_name, branch_name):
    objects = objects_of_branch(bucket_name, paginator, branch_name)
    object_keys = extract_object_keys(objects)
    return object_keys


def objects_of_branch(bucket_name, paginator, branch_name):
    page_iterator = paginator.paginate(Bucket=bucket_name, Prefix=FOLDER_FORMAT %branch_name)

    return reduce(lambda acc, page: page['Contents'] + acc, page_iterator, [])

def extract_object_keys(objects):
    return [{'Key' : k} for k in [obj['Key']
        for obj in objects]]
