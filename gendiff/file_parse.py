import json
import yaml
from os.path import splitext


def file_parse(file_path, format):
    if format == '.json':
        return json.load(file_path)
    if format in ('.yml', '.yaml'):
        return yaml.safe_load(file_path)
    raise Exception('Unknown format')


def get_content(file_path):
    format = splitext(file_path)[1]
    return file_parse(open(file_path), format)
