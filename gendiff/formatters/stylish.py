import itertools


REPLACER = '  '
SPACES_COUNT = 1


def to_str(value, depth):
    deep_indent_size = depth + SPACES_COUNT
    indent = REPLACER * deep_indent_size
    if isinstance(value, bool):
        return (str(value)).lower()
    if value is None:
        return 'null'
    if isinstance(value, dict):
        lines = []
        for key, val in value.items():
            lines.append(f'  {indent}  {key}: {to_str(val, deep_indent_size + SPACES_COUNT)}')
        result = itertools.chain("{", lines, [indent + "}"])
        return "\n".join(result)
    return str(value)


def build_stylish(elements, depth=0):
    deep_indent_size = depth + SPACES_COUNT
    deep_indent = REPLACER * deep_indent_size
    current_indent = REPLACER * depth
    lines = []
    for node in elements:
        if node['action'] == 'has_child':
            lines.append(
                f'{deep_indent}  {node["key"]}: '
                f'{build_stylish(node["childrens"], deep_indent_size + SPACES_COUNT)}'
            )
        elif node['action'] == 'updated':
            lines.append(
                f'{deep_indent}- {node["key"]}: {to_str(node["old_value"], deep_indent_size)}'
            )
            lines.append(
                f'{deep_indent}+ {node["key"]}: {to_str(node["new_value"], deep_indent_size)}'
            )
        elif node['action'] == 'removed':
            lines.append(
                f'{deep_indent}- {node["key"]}: {to_str(node["value"], deep_indent_size)}'
            )
        elif node['action'] == 'added':
            lines.append(
                f'{deep_indent}+ {node["key"]}: {to_str(node["value"], deep_indent_size)}'
            )
        elif node['action'] == 'unchanged':
            lines.append(
                f'{deep_indent}  {node["key"]}: {to_str(node["value"], deep_indent_size)}'
            )
    result = itertools.chain("{", lines, [current_indent + "}"])
    return "\n".join(result)


def render_stylish(content):
    return build_stylish(content)
