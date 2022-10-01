import itertools


REPLACER = '  '
SPACES_COUNT = 1


def to_str(value, depth):
    deep_indent_size = depth + SPACES_COUNT
    deep_indent = REPLACER * deep_indent_size
    if isinstance(value, bool):
        return (str(value)).lower()
    if value is None:
        return 'null'
    if isinstance(value, dict):
        lines = []
        for key, val in value.items():
            lines.append(f'  {deep_indent}  {key}: {to_str(val, deep_indent_size+1)}')
        result = itertools.chain("{", lines, [deep_indent + "}"])
        return "\n".join(result)
    return str(value)


def build_stylish(content, depth=0):
    deep_indent_size = depth + SPACES_COUNT
    deep_indent = REPLACER * deep_indent_size
    current_indent = REPLACER * depth
    lines = []
    for i in content:
        if i['action'] == 'has_child':
            lines.append(
                f'{deep_indent}  {i["key"]}: {build_stylish(i["childrens"], deep_indent_size+1)}'
            )
        elif i['action'] == 'updated':
            lines.append(
                f'{deep_indent}- {i["key"]}: {to_str(i["old_value"], deep_indent_size)}'
            )
            lines.append(
                f'{deep_indent}+ {i["key"]}: {to_str(i["new_value"], deep_indent_size)}'
            )
        elif i['action'] == 'removed':
            lines.append(
                f'{deep_indent}- {i["key"]}: {to_str(i["value"], deep_indent_size)}'
            )
        elif i['action'] == 'added':
            lines.append(
                f'{deep_indent}+ {i["key"]}: {to_str(i["value"], deep_indent_size)}'
            )
        elif i['action'] == 'unchanged':
            lines.append(
                f'{deep_indent}  {i["key"]}: {to_str(i["value"], deep_indent_size)}'
            )
    result = itertools.chain("{", lines, [current_indent + "}"])
    return "\n".join(result)


def render_stylish(content):
    return build_stylish(content)
