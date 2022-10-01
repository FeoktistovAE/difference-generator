import json
import yaml
from os.path import splitext


def parse(file_path, extension):
    extension = extension[1:]
    if extension == 'json':
        return json.load(file_path)
    if extension in ('yml', 'yaml'):
        return yaml.safe_load(file_path)
    raise Exception('Unknown extension')


def get_content(file_path):
    _, extension = splitext(file_path)
    return parse(open(file_path), extension)
