import json
import yaml


def parse_json(file_path):
    parsed_file = json.load(open(file_path))
    return parsed_file


def parse_yaml(file_path):
    parsed_file = yaml.safe_load(open(file_path))
    return parsed_file
