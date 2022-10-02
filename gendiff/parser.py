import json
import yaml
from os.path import splitext


def parse(content, extension):
    if extension == 'json':
        return json.load(content)
    if extension in ('yml', 'yaml'):
        return yaml.safe_load(content)
    raise Exception('Unknown extension')


def get_content(file_path):
    _, extension = splitext(file_path)
    return parse(open(file_path), extension[1:])
