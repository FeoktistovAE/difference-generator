import json
import yaml


def file_parse(file_path):
    if file_path.endswith('.json'):
        return json.load(open(file_path))
    else:
        return yaml.safe_load(open(file_path))
