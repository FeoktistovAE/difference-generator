from gendiff.formatters.stylish import render_stylish
from gendiff.formatters.plain import render_plain
from gendiff.formatters.json import render_json


def apply_formatter(internal_view, format):
    if format == 'stylish':
        return render_stylish(internal_view)
    if format == 'plain':
        return render_plain(internal_view)
    if format == 'json':
        return render_json(internal_view)
    else:
        raise Exception('Unknown render format')
