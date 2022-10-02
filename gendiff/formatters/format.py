from gendiff.formatters.stylish import render_stylish
from gendiff.formatters.plain import render_plain
from gendiff.formatters.json import render_json


def apply_formatter(dicts_diff, format):
    if format == 'stylish':
        return render_stylish(dicts_diff)
    if format == 'plain':
        return render_plain(dicts_diff)
    if format == 'json':
        return render_json(dicts_diff)
    raise Exception('Unknown render format')
