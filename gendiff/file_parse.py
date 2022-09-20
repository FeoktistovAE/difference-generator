import json
import yaml


def content_parse(content, parser):
    if parser == 'json':
        return json.load(content)
    elif parser == 'yml':
        return yaml.safe_load(content)


def file_parse(file_path):
    if file_path.endswith('.json'):
        return content_parse(open(file_path), 'json')
    elif file_path.endswith(('.yaml', '.yml')):
        return content_parse(open(file_path), 'yml')
    else:
        raise Exception('Unknown file format')
