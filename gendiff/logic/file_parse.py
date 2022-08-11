import json
import yaml


def parse_json(file_path):
    parsed_file = json.load(open(file_path))
    for i in parsed_file.keys():
        if isinstance(parsed_file[i], bool):
            parsed_file[i] = json.dumps(parsed_file[i])
    return parsed_file


def parse_yaml(file_path):
    parsed_file = yaml.safe_load(open(file_path))
    for i in parsed_file.keys():
        if isinstance(parsed_file[i], bool):
            parsed_file[i] = str(parsed_file[i]).lower()
    return parsed_file
