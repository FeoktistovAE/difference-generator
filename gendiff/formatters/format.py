from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain
from gendiff.formatters.json import get_json


def apply_formatter(file1, file2, format, find_diff):
    if format == 'stylish':
        return stylish(file1, file2, find_diff)
    elif format == 'plain':
        return plain(file1, file2, find_diff)
    elif format == 'json':
        return get_json(file1, file2, find_diff)
