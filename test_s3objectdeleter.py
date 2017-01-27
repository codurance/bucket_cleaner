import pytest
from mock import MagicMock
from s3objectdeleter import *
from itertools import repeat
from mock import call

BUCKET_NAME='some'

def test_delete_objects_for_keys_uses_s3_client_to_delete_objects():
    list_of_keys = [{'Key':'1'}, {'Key', '2'}]
    s3client = MagicMock()
    s3client.delete_objects = MagicMock()

    delete_objects_for_keys(s3client, BUCKET_NAME, list_of_keys)

    s3client.delete_objects.assert_called_once_with(Bucket=BUCKET_NAME, Delete={'Objects' : list_of_keys})

def test_delete_objects_uses_s3_client_twice_to_delete_1001_objects():
    key = {'Key': 'x'}
    keys = list(repeat(key, 1001))
    s3client = MagicMock()
    s3client.delete_objects = MagicMock()

    delete_objects_for_keys(s3client, BUCKET_NAME, keys)

    s3client.delete_objects.assert_has_calls([
        delete_objects_call(key, 1000),
        delete_objects_call(key, 1)])

def delete_objects_call(key, number_of_objects):
    return call(Bucket=BUCKET_NAME, Delete={'Objects' : list(repeat(key, number_of_objects))})
