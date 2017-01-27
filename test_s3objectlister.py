from mock import MagicMock
from s3objectlister import *
from itertools import repeat
import datetime
from dateutil.tz import tzutc

BUCKET_NAME='some'

def generate_pages(pages_count, objects_per_page):
    objects_of_page = {'Contents':list(repeat({}, objects_per_page))}
    return list(repeat(objects_of_page , pages_count))

def test_list_of_objects_of_a_branch_is_empty_if_there_is_no_pages():
    paginator = MagicMock()
    pages = generate_pages(pages_count=0, objects_per_page=0)
    paginator.paginate = MagicMock(return_value=pages)

    assert len(objects_of_branch(BUCKET_NAME, paginator, "no_branch_name")) == 0

def test_list_of_objects_of_a_branch_is_empty_if_there_is_one_empty_page():
    paginator = MagicMock()
    pages = generate_pages(pages_count=1, objects_per_page=0)
    paginator.paginate = MagicMock(return_value=pages)

    assert len(objects_of_branch(BUCKET_NAME, paginator, "no_branch_name")) == 0

def test_list_of_objects_of_a_branch_gives_two_objects_when_two_pages_and_one_object_per_page():
    paginator = MagicMock()
    pages = generate_pages(pages_count=2, objects_per_page=1)
    paginator.paginate = MagicMock(return_value=pages)

    assert len(objects_of_branch(BUCKET_NAME, paginator, "no_branch_name")) == 2

def test_list_of_objects_of_a_branch_gives_four_objects_when_two_pages_and_two_object_per_page():
    paginator = MagicMock()
    pages = generate_pages(pages_count=2, objects_per_page=2)
    paginator.paginate = MagicMock(return_value=pages)

    assert len(objects_of_branch(BUCKET_NAME, paginator, "no_branch_name")) == 4

def test_extract_object_keys_gives_empty_array_when_no_objects():
    assert extract_object_keys([]) == []

def test_extract_object_keys_gives_an_object_when_contents_field_has_an_object():
    page_with_one_element = [{u'LastModified': datetime.datetime(2017, 1, 24, 16, 31, 24, tzinfo=tzutc()), u'ETag': '"08023ee06b6f1c34c6a9648a8bf3fd4c"', u'StorageClass': 'STANDARD', u'Key': u'site-prs_in_one_bucket/atom.xml', u'Owner': {u'DisplayName': 'mash', u'ID': '8041a9f893f115ddd3fb2d30011f24d4b5b40b32a44a540f802a484bdb43e01e'}, u'Size': 32084}]

    assert extract_object_keys(page_with_one_element) == [{'Key' : 'site-prs_in_one_bucket/atom.xml' }]

def test_extract_object_keys_gives_three_objects_when_contents_field_has_three_objects():
    page_with_three_elements = [{u'LastModified': datetime.datetime(2017, 1, 25, 14, 3, 2, tzinfo=tzutc()), u'ETag': '"d41d8cd98f00b204e9800998ecf8427e"', u'StorageClass': 'STANDARD', u'Key': u'site-prs_in_one_bucket/folder/', u'Owner': {u'DisplayName': 'mash', u'ID': '8041a9f893f115ddd3fb2d30011f24d4b5b40b32a44a540f802a484bdb43e01e'}, u'Size': 0}, {u'LastModified': datetime.datetime(2017, 1, 25, 14, 3, 9, tzinfo=tzutc()), u'ETag': '"d41d8cd98f00b204e9800998ecf8427e"', u'StorageClass': 'STANDARD', u'Key': u'site-prs_in_one_bucket/folder/asdf/', u'Owner': {u'DisplayName': 'mash', u'ID': '8041a9f893f115ddd3fb2d30011f24d4b5b40b32a44a540f802a484bdb43e01e'}, u'Size': 0}, {u'LastModified': datetime.datetime(2017, 1, 25, 14, 3, 11, tzinfo=tzutc()), u'ETag': '"d41d8cd98f00b204e9800998ecf8427e"', u'StorageClass': 'STANDARD', u'Key': u'site-prs_in_one_bucket/folder/asdff/', u'Owner': {u'DisplayName': 'mash', u'ID': '8041a9f893f115ddd3fb2d30011f24d4b5b40b32a44a540f802a484bdb43e01e'}, u'Size': 0}]

    assert extract_object_keys(page_with_three_elements) == [{u'Key': u'site-prs_in_one_bucket/folder/'}, {u'Key': u'site-prs_in_one_bucket/folder/asdf/'}, {u'Key': u'site-prs_in_one_bucket/folder/asdff/'}]
