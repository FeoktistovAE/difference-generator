from gendiff.parser import get_content
from gendiff.formatters.format import apply_formatter


def build_diff(content1, content2):
    node1_keys = set(content1.keys())
    node2_keys = set(content2.keys())
    removed = node1_keys - node2_keys
    added = node2_keys - node1_keys
    intersection = node1_keys & node2_keys
    joined_keys = sorted(list(node1_keys | node2_keys))
    result = []
    for key in joined_keys:
        if key in intersection:
            if isinstance(content1[key], dict) and isinstance(content2[key], dict):
                result.append(
                    {'action': 'has_child', 'key': key, 'childrens': build_diff(content1[key], content2[key])}
                )
            elif content1[key] != content2[key]:
                result.append(
                    {'action': 'updated', 'key': key, 'old_value': content1[key], 'new_value': content2[key]}
                )
            else:
                result.append(
                    {'action': 'unchanged', 'key': key, 'value': content1[key]}
                )
        elif key in removed:
            result.append(
                {'action': 'removed', 'key': key, 'value': content1[key]}
            )
        elif key in added:
            result.append(
                {'action': 'added', 'key': key, 'value': content2[key]}
            )
    return result


def generate_diff(path_to_file1, path_to_file2, format='stylish'):
    content1 = get_content(path_to_file1)
    content2 = get_content(path_to_file2)
    dicts_diff = build_diff(content1, content2)
    return apply_formatter(dicts_diff, format)
