import json

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

def parse(event):
    parsed_message = parse_message(event)
    return (is_closed_pr(parsed_message), parse_branch_name(parsed_message))
