from gendiff.logic.file_parse import parse_json, parse_yaml
from gendiff.formatters.stylish_formatter import stylish
from gendiff.formatters.plain_formatter import plain


def find_children_and_updates(intersection, node1, node2):
    updated = set()
    children = set()
    for i in intersection:
        if isinstance(node1[i], dict) and isinstance(node2[i], dict):
            children.add(i)
        elif node1[i] != node2[i]:
            updated.add(i)
    return children, updated


def find_diff(file1, file2):

    def walk(node1, node2, result):
        node1_keys = set(node1.keys())
        node2_keys = set(node2.keys())
        removed = node1_keys - node2_keys
        added = node2_keys - node1_keys
        intersection = node1_keys & node2_keys
        joined_keys = list(node1_keys | node2_keys)
        children, updated = find_children_and_updates(intersection, node1, node2)
        for i in joined_keys:
            if i in children:
                result.append(
                    {'action': 'has_child', 'key': i, 'childrens': node1[i].keys() | node2[i].keys()}
                )
            elif i in updated:
                result.append(
                    {'action': 'updated', 'key': i, 'old_key_value': node1[i], 'new_key_value': node2[i]}
                )
            elif i in removed:
                result.append(
                    {'action': 'removed', 'key': i, 'key_value': node1[i]}
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


def generate_diff(path_to_file1, path_to_file2, format='stylish'):
    if path_to_file1.endswith('.json'):
        file1 = parse_json(path_to_file1)
    else:
        file1 = parse_yaml(path_to_file1)
    if path_to_file2.endswith('.json'):
        file2 = parse_json(path_to_file2)
    else:
        file2 = parse_yaml(path_to_file2)
    if format == 'stylish':
        return stylish(file1, file2, find_diff)
    else:
        return plain(file1, file2, find_diff)
