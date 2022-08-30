from gendiff.logic.file_parse import parse_json, parse_yaml
import itertools


def find_children_and_changes(intersection, node1, node2):
    changed = set()
    children = set()
    for i in intersection:
        if isinstance(node1[i], dict) and isinstance(node2[i], dict):
            children.add(i)
        elif node1[i] != node2[i]:
            changed.add(i)
    return children, changed


def find_diff(file1, file2):

    def walk(node1, node2, result):
        node1_keys = set(node1.keys())
        node2_keys = set(node2.keys())
        deleted = node1_keys - node2_keys
        added = node2_keys - node1_keys
        intersection = node1_keys & node2_keys
        joined_keys = list(node1_keys | node2_keys)
        children, changed = find_children_and_changes(intersection, node1, node2)
        for i in joined_keys:
            if i in children:
                result.append(
                    {'action': 'has_child', 'key': i, 'childrens': node1[i].keys() | node2[i].keys()}
                )
            elif i in changed:
                result.append(
                    {'action': 'changed', 'key': i, 'old_key_value': node1[i], 'new_key_value': node2[i]}
                )
            elif i in deleted:
                result.append(
                    {'action': 'deleted', 'key': i, 'key_value': node1[i]}
                )
            elif i in added:
                result.append(
                    {'action': 'added', 'key': i, 'key_value': node2[i]}
                )

            else:
                result.append(
                    {'action': 'unchanged', 'key': i, 'key_value': node1[i]}
                )

        list(map(lambda child: walk(node1[child], node2[child], result), children))
        return result
    return walk(file1, file2, [])


def dump(value):
    if isinstance(value, bool):
        return (str(value)).lower()
    elif value is None:
        return 'null'
    return value


def stylish(file1, file2):
    replacer = '  '
    spaces_count = 1
    internal_view = find_diff(file1, file2)
    joined_keys = file1.keys() | file2.keys()

    def iter_(value, depth):
        value = dump(value)
        deep_indent_size = depth + spaces_count
        deep_indent = replacer * deep_indent_size
        current_indent = replacer * depth
        lines = []
        if isinstance(value, dict):
            for key, val in value.items():
                lines.append(f'  {deep_indent}  {key}: {iter_(val, deep_indent_size+1)}')
            result = itertools.chain("{", lines, [deep_indent + "}"])
            return "\n".join(result)
        elif not isinstance(value, (set, dict)):
            return str(value)
        sorted_keys = sorted(list(value))
        for i in sorted_keys:
            for j in internal_view:
                if j['key'] == i:
                    if j['action'] == 'has_child':
                        lines.append(
                            f'{deep_indent}  {i}: {iter_(j["childrens"], deep_indent_size+1)}'
                        )
                    elif j['action'] == 'changed':
                        lines.append(
                            f'{deep_indent}- {i}: {iter_(j["old_key_value"], deep_indent_size)}'
                        )
                        lines.append(
                            f'{deep_indent}+ {i}: {iter_(j["new_key_value"], deep_indent_size)}'
                        )
                    elif j['action'] == 'deleted':
                        lines.append(
                            f'{deep_indent}- {i}: {iter_(j["key_value"], deep_indent_size)}'
                        )
                    elif j['action'] == 'added':
                        lines.append(
                            f'{deep_indent}+ {i}: {iter_(j["key_value"], deep_indent_size)}'
                        )
                    elif j['action'] == 'unchanged':
                        lines.append(
                            f'{deep_indent}  {i}: {iter_(j["key_value"], deep_indent_size)}'
                        )
        result = itertools.chain("{", lines, [current_indent + "}"])
        return "\n".join(result)
    return iter_(joined_keys, 0)


def generate_diff(path_to_file1, path_to_file2):
    if path_to_file1.endswith('.json') and path_to_file2.endswith('.json'):
        return stylish(
            parse_json(path_to_file1), parse_json(path_to_file2)
        )
    else:
        return stylish(
            parse_yaml(path_to_file1), parse_yaml(path_to_file2)
        )
