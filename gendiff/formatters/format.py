from gendiff.formatters.stylish import render_stylish
from gendiff.formatters.plain import plain
from gendiff.formatters.json import get_json


def apply_formatter(internal_view, format):
    if format == 'stylish':
        return render_stylish(internal_view)
    elif format == 'plain':
        return plain(internal_view)
    elif format == 'json':
        return get_json(internal_view)
    else:
        raise Exception('Unknown render format')
