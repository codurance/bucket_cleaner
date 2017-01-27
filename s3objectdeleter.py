import boto3

def delete_objects_for_keys(s3client, bucket_name, keys):
    for chunk in chunks(keys, 1000):
        s3client.delete_objects(Bucket=bucket_name, Delete={'Objects' : chunk})

def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]
