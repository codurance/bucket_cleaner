from main import *
import pytest
from mock import MagicMock
import datetime
from dateutil.tz import tzutc

SNS_MESSAGE = {
    "Records": [
        {
            "EventSource": "aws:sns",
            "EventVersion": "1.0",
            "EventSubscriptionArn": "xxx",
            "Sns": {
                "Type": "Notification",
                "MessageId": "xxxx",
                "TopicArn": "xxx",
                "Subject": "null",
                "Message": "{\"ref\":\"refs/heads/prs_in_one_bucket\",\"before\":\"2a9a2706a6b1bf31ad31d52e4120abc72b6a5869\",\"after\":\"f39323ca99039274b64b26fdd55577029769a774\",\"created\":false,\"deleted\":true,\"forced\":false,\"base_ref\":null,\"compare\":\"https://github.com/RafalWilinski/rwilinski-page/compare/2a9a2706a6b1...f39323ca9903\",\"commits\":[{\"id\":\"f39323ca99039274b64b26fdd55577029769a774\",\"tree_id\":\"ba9bb4eed40d5ffd26b701e503f3b7683489ebc6\",\"distinct\":true,\"message\":\"Fixed font-boosting issues, better arrows\",\"timestamp\":\"2016-06-29T09:49:25+02:00\",\"url\":\"https://github.com/RafalWilinski/rwilinski-page/commit/f39323ca99039274b64b26fdd55577029769a774\",\"author\":{\"name\":\"Rafal Wilinski\",\"email\":\"raf.wilinski@gmail.com\",\"username\":\"RafalWilinski\"},\"committer\":{\"name\":\"Rafal Wilinski\",\"email\":\"raf.wilinski@gmail.com\",\"username\":\"RafalWilinski\"},\"added\":[],\"removed\":[],\"modified\":[\"static/app.js\",\"static/index.html\",\"static/styles.css\"]}],\"head_commit\":{\"id\":\"f39323ca99039274b64b26fdd55577029769a774\",\"tree_id\":\"ba9bb4eed40d5ffd26b701e503f3b7683489ebc6\",\"distinct\":true,\"message\":\"Fixed font-boosting issues, better arrows\",\"timestamp\":\"2016-06-29T09:49:25+02:00\",\"url\":\"https://github.com/RafalWilinski/rwilinski-page/commit/f39323ca99039274b64b26fdd55577029769a774\",\"author\":{\"name\":\"Rafal Wilinski\",\"email\":\"raf.wilinski@gmail.com\",\"username\":\"RafalWilinski\"},\"committer\":{\"name\":\"Rafal Wilinski\",\"email\":\"raf.wilinski@gmail.com\",\"username\":\"RafalWilinski\"},\"added\":[],\"removed\":[],\"modified\":[\"static/app.js\",\"static/index.html\",\"static/styles.css\"]},\"repository\":{\"id\":62137738,\"name\":\"rwilinski-page\",\"full_name\":\"RafalWilinski/rwilinski-page\",\"owner\":{\"name\":\"RafalWilinski\",\"email\":\"raf.wilinski@gmail.com\"},\"private\":false,\"html_url\":\"https://github.com/RafalWilinski/rwilinski-page\",\"description\":\"My personal page\",\"fork\":false,\"url\":\"https://github.com/RafalWilinski/rwilinski-page\",\"forks_url\":\"https://api.github.com/repos/RafalWilinski/rwilinski-page/forks\",\"keys_url\":\"https://api.github.com/repos/RafalWilinski/rwilinski-page/keys{/key_id}\",\"collaborators_url\":\"https://api.github.com/repos/RafalWilinski/rwilinski-page/collaborators{/collaborator}\",\"teams_url\":\"https://api.github.com/repos/RafalWilinski/rwilinski-page/teams\",\"hooks_url\":\"https://api.github.com/repos/RafalWilinski/rwilinski-page/hooks\",\"issue_events_url\":\"https://api.github.com/repos/RafalWilinski/rwilinski-page/issues/events{/number}\",\"events_url\":\"https://api.github.com/repos/RafalWilinski/rwilinski-page/events\",\"assignees_url\":\"https://api.github.com/repos/RafalWilinski/rwilinski-page/assignees{/user}\",\"branches_url\":\"https://api.github.com/repos/RafalWilinski/rwilinski-page/branches{/branch}\",\"tags_url\":\"https://api.github.com/repos/RafalWilinski/rwilinski-page/tags\",\"blobs_url\":\"https://api.github.com/repos/RafalWilinski/rwilinski-page/git/blobs{/sha}\",\"git_tags_url\":\"https://api.github.com/repos/RafalWilinski/rwilinski-page/git/tags{/sha}\",\"git_refs_url\":\"https://api.github.com/repos/RafalWilinski/rwilinski-page/git/refs{/sha}\",\"trees_url\":\"https://api.github.com/repos/RafalWilinski/rwilinski-page/git/trees{/sha}\",\"statuses_url\":\"https://api.github.com/repos/RafalWilinski/rwilinski-page/statuses/{sha}\",\"languages_url\":\"https://api.github.com/repos/RafalWilinski/rwilinski-page/languages\",\"stargazers_url\":\"https://api.github.com/repos/RafalWilinski/rwilinski-page/stargazers\",\"contributors_url\":\"https://api.github.com/repos/RafalWilinski/rwilinski-page/contributors\",\"subscribers_url\":\"https://api.github.com/repos/RafalWilinski/rwilinski-page/subscribers\",\"subscription_url\":\"https://api.github.com/repos/RafalWilinski/rwilinski-page/subscription\",\"commits_url\":\"https://api.github.com/repos/RafalWilinski/rwilinski-page/commits{/sha}\",\"git_commits_url\":\"https://api.github.com/repos/RafalWilinski/rwilinski-page/git/commits{/sha}\",\"comments_url\":\"https://api.github.com/repos/RafalWilinski/rwilinski-page/comments{/number}\",\"issue_comment_url\":\"https://api.github.com/repos/RafalWilinski/rwilinski-page/issues/comments{/number}\",\"contents_url\":\"https://api.github.com/repos/RafalWilinski/rwilinski-page/contents/{+path}\",\"compare_url\":\"https://api.github.com/repos/RafalWilinski/rwilinski-page/compare/{base}...{head}\",\"merges_url\":\"https://api.github.com/repos/RafalWilinski/rwilinski-page/merges\",\"archive_url\":\"https://api.github.com/repos/RafalWilinski/rwilinski-page/{archive_format}{/ref}\",\"downloads_url\":\"https://api.github.com/repos/RafalWilinski/rwilinski-page/downloads\",\"issues_url\":\"https://api.github.com/repos/RafalWilinski/rwilinski-page/issues{/number}\",\"pulls_url\":\"https://api.github.com/repos/RafalWilinski/rwilinski-page/pulls{/number}\",\"milestones_url\":\"https://api.github.com/repos/RafalWilinski/rwilinski-page/milestones{/number}\",\"notifications_url\":\"https://api.github.com/repos/RafalWilinski/rwilinski-page/notifications{?since,all,participating}\",\"labels_url\":\"https://api.github.com/repos/RafalWilinski/rwilinski-page/labels{/name}\",\"releases_url\":\"https://api.github.com/repos/RafalWilinski/rwilinski-page/releases{/id}\",\"deployments_url\":\"https://api.github.com/repos/RafalWilinski/rwilinski-page/deployments\",\"created_at\":1467115810,\"updated_at\":\"2016-06-28T21:37:24Z\",\"pushed_at\":1467186570,\"git_url\":\"git://github.com/RafalWilinski/rwilinski-page.git\",\"ssh_url\":\"git@github.com:RafalWilinski/rwilinski-page.git\",\"clone_url\":\"https://github.com/RafalWilinski/rwilinski-page.git\",\"svn_url\":\"https://github.com/RafalWilinski/rwilinski-page\",\"homepage\":null,\"size\":8,\"stargazers_count\":0,\"watchers_count\":0,\"language\":\"HTML\",\"has_issues\":true,\"has_downloads\":true,\"has_wiki\":true,\"has_pages\":false,\"forks_count\":0,\"mirror_url\":null,\"open_issues_count\":0,\"forks\":0,\"open_issues\":0,\"watchers\":0,\"default_branch\":\"master\",\"stargazers\":0,\"master_branch\":\"master\"},\"pusher\":{\"name\":\"RafalWilinski\",\"email\":\"raf.wilinski@gmail.com\"},\"sender\":{\"login\":\"RafalWilinski\",\"id\":3391616,\"avatar_url\":\"https://avatars.githubusercontent.com/u/3391616?v=3\",\"gravatar_id\":\"\",\"url\":\"https://api.github.com/users/RafalWilinski\",\"html_url\":\"https://github.com/RafalWilinski\",\"followers_url\":\"https://api.github.com/users/RafalWilinski/followers\",\"following_url\":\"https://api.github.com/users/RafalWilinski/following{/other_user}\",\"gists_url\":\"https://api.github.com/users/RafalWilinski/gists{/gist_id}\",\"starred_url\":\"https://api.github.com/users/RafalWilinski/starred{/owner}{/repo}\",\"subscriptions_url\":\"https://api.github.com/users/RafalWilinski/subscriptions\",\"organizations_url\":\"https://api.github.com/users/RafalWilinski/orgs\",\"repos_url\":\"https://api.github.com/users/RafalWilinski/repos\",\"events_url\":\"https://api.github.com/users/RafalWilinski/events{/privacy}\",\"received_events_url\":\"https://api.github.com/users/RafalWilinski/received_events\",\"type\":\"User\",\"site_admin\":false}}",
                "Timestamp": "2016-06-29T18:11:44.582Z",
                "SignatureVersion": "1",
                "Signature": "xxxxx",
                "SigningCertUrl": "xxxx",
                "UnsubscribeUrl": "xxx",
                "MessageAttributes": {
                    "X-Github-Event": {
                        "Type": "String",
                        "Value": "push"
                    }
                }
            }
        }
    ]
}

def test_parse_message_raises_when_empty_message():
    empty_message = {'Records' : [ { 'Sns' : { 'Message': '' } }]}
    with pytest.raises(ValueError):
        parse_message(empty_message)

def test_parse_message_has_ref_and_deleted():
    parsed_message = parse_message(SNS_MESSAGE)
    assert parsed_message['deleted'] == True
    assert parsed_message['ref'] == 'refs/heads/prs_in_one_bucket'

def test_parse_reference_throws_when_invalid_reference():
    reference = {'ref' : 'invalid'}
    with pytest.raises(ValueError):
        parse_branch_name(reference)

def test_parse_valid_reference():
    branch_name = 'branch_name'
    reference = {'ref' : 'refs/heads/%s' %branch_name}
    assert branch_name == parse_branch_name(reference)

def test_parse_is_closed_pr():
    deleted = {'deleted' : True}
    assert is_closed_pr(deleted) == True

def test_list_of_objects_of_a_branch_is_empty_if_there_is_no_pages():
    paginator = MagicMock()
    paginator.paginate = MagicMock(return_value=[])
    assert len(objects_of_branch(paginator, "no_branch_name")) == 0

def test_list_of_objects_of_a_branch_is_empty_if_there_is_one_empty_page():
    paginator = MagicMock()
    empty_page = []
    pages = [empty_page]
    paginator.paginate = MagicMock(return_value=pages)
    assert len(objects_of_branch(paginator, "no_branch_name")) == 0

def test_list_of_objects_of_a_branch_gives_one_object_when_only_one_page_and_one_object():
    paginator = MagicMock()
    page = [{}]
    pages = [page]
    paginator.paginate = MagicMock(return_value=pages)
    assert len(objects_of_branch(paginator, "no_branch_name")) == 1

def test_list_of_objects_of_a_branch_gives_two_object_when_one_page_and_two_object():
    paginator = MagicMock()
    page = [{}, {}]
    pages = [page]
    paginator.paginate = MagicMock(return_value=pages)
    assert len(objects_of_branch(paginator, "no_branch_name")) == 2

def test_list_of_objects_of_a_branch_gives_two_object_when_two_pages_and_one_object_per_page():
    paginator = MagicMock()
    page = [{}]
    pages = [page, page]
    paginator.paginate = MagicMock(return_value=pages)
    assert len(objects_of_branch(paginator, "no_branch_name")) == 2

def test_extract_object_keys_gives_empty_array_when_no_objects():
    assert extract_object_keys({'Contents': []}) == []

def test_extract_object_keys_gives_an_object_when_contents_field_has_an_object():
    page_with_one_element = {u'Name': 'codurance-site-pr', 'ResponseMetadata': {'HTTPStatusCode': 200, 'RetryAttempts': 0, 'HostId': 'zznSWrPmIfD1D8GXi8DkJAQ09zmWYYbORevgA7JThqKlN/5qOr7bQPIBOqNeW973uyzxsIxk8R0=', 'RequestId': 'B5AA92BCC7BCC8D5', 'HTTPHeaders': {'x-amz-bucket-region': 'eu-west-1', 'x-amz-id-2': 'zznSWrPmIfD1D8GXi8DkJAQ09zmWYYbORevgA7JThqKlN/5qOr7bQPIBOqNeW973uyzxsIxk8R0=', 'server': 'AmazonS3', 'transfer-encoding': 'chunked', 'x-amz-request-id': 'B5AA92BCC7BCC8D5', 'date': 'Wed, 25 Jan 2017 12:24:33 GMT', 'content-type': 'application/xml'}}, u'MaxKeys': 1000, u'Prefix': 'site-prs_in_one_bucket/atom.xml', u'Marker': u'', u'EncodingType': 'url', u'IsTruncated': False, u'Contents': [{u'LastModified': datetime.datetime(2017, 1, 24, 16, 31, 24, tzinfo=tzutc()), u'ETag': '"08023ee06b6f1c34c6a9648a8bf3fd4c"', u'StorageClass': 'STANDARD', u'Key': u'site-prs_in_one_bucket/atom.xml', u'Owner': {u'DisplayName': 'mash', u'ID': '8041a9f893f115ddd3fb2d30011f24d4b5b40b32a44a540f802a484bdb43e01e'}, u'Size': 32084}]}
    assert extract_object_keys(page_with_one_element) == [{'Key' : 'site-prs_in_one_bucket/atom.xml' }]

def test_extract_object_keys_gives_three_objects_when_contents_field_has_three_objects():
    page_with_three_elements= {u'Name': 'codurance-site-pr', 'ResponseMetadata': {'HTTPStatusCode': 200, 'RetryAttempts': 0, 'HostId': 'xs6iOqZ/XANcbGOaW8vA3UNHrAA5FClThFl4WLp5TVLPR3wxhCmkbnVKR7EUSbEXjfNu+ljv1Qc=', 'RequestId': '31243B5D2F0295A9', 'HTTPHeaders': {'x-amz-bucket-region': 'eu-west-1', 'x-amz-id-2': 'xs6iOqZ/XANcbGOaW8vA3UNHrAA5FClThFl4WLp5TVLPR3wxhCmkbnVKR7EUSbEXjfNu+ljv1Qc=', 'server': 'AmazonS3', 'transfer-encoding': 'chunked', 'x-amz-request-id': '31243B5D2F0295A9', 'date': 'Wed, 25 Jan 2017 14:05:00 GMT', 'content-type': 'application/xml'}}, u'MaxKeys': 1000, u'Prefix': 'site-prs_in_one_bucket/folder', u'Marker': u'', u'EncodingType': 'url', u'IsTruncated': False, u'Contents': [{u'LastModified': datetime.datetime(2017, 1, 25, 14, 3, 2, tzinfo=tzutc()), u'ETag': '"d41d8cd98f00b204e9800998ecf8427e"', u'StorageClass': 'STANDARD', u'Key': u'site-prs_in_one_bucket/folder/', u'Owner': {u'DisplayName': 'mash', u'ID': '8041a9f893f115ddd3fb2d30011f24d4b5b40b32a44a540f802a484bdb43e01e'}, u'Size': 0}, {u'LastModified': datetime.datetime(2017, 1, 25, 14, 3, 9, tzinfo=tzutc()), u'ETag': '"d41d8cd98f00b204e9800998ecf8427e"', u'StorageClass': 'STANDARD', u'Key': u'site-prs_in_one_bucket/folder/asdf/', u'Owner': {u'DisplayName': 'mash', u'ID': '8041a9f893f115ddd3fb2d30011f24d4b5b40b32a44a540f802a484bdb43e01e'}, u'Size': 0}, {u'LastModified': datetime.datetime(2017, 1, 25, 14, 3, 11, tzinfo=tzutc()), u'ETag': '"d41d8cd98f00b204e9800998ecf8427e"', u'StorageClass': 'STANDARD', u'Key': u'site-prs_in_one_bucket/folder/asdff/', u'Owner': {u'DisplayName': 'mash', u'ID': '8041a9f893f115ddd3fb2d30011f24d4b5b40b32a44a540f802a484bdb43e01e'}, u'Size': 0}]}
    assert extract_object_keys(page_with_three_elements) == [{u'Key': u'site-prs_in_one_bucket/folder/'}, {u'Key': u'site-prs_in_one_bucket/folder/asdf/'}, {u'Key': u'site-prs_in_one_bucket/folder/asdff/'}]
