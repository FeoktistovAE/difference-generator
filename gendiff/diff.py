from gendiff.file_parse import get_content
from gendiff.formatters.format import apply_formatter


def build_diff(content1, content2):
    node1_keys = set(content1.keys())
    node2_keys = set(content2.keys())
    removed = node1_keys - node2_keys
    added = node2_keys - node1_keys
    intersection = node1_keys & node2_keys
    joined_keys = sorted(list(node1_keys | node2_keys))
    result = []
    for i in joined_keys:
        if i in intersection:
            if isinstance(content1[i], dict) and isinstance(content2[i], dict):
                result.append(
                    {'action': 'has_child', 'key': i, 'childrens': build_diff(content1[i], content2[i])}
                )
            elif content1[i] != content2[i]:
                result.append(
                    {'action': 'updated', 'key': i, 'old_value': content1[i], 'new_value': content2[i]}
                )
            else:
                result.append(
                    {'action': 'unchanged', 'key': i, 'value': content1[i]}
                )
        elif i in removed:
            result.append(
                {'action': 'removed', 'key': i, 'value': content1[i]}
            )
        elif i in added:
            result.append(
                {'action': 'added', 'key': i, 'value': content2[i]}
            )
    return result


def generate_diff(path_to_file1, path_to_file2, format='stylish'):
    content1 = get_content(path_to_file1)
    content2 = get_content(path_to_file2)
    content_diff = build_diff(content1, content2)
    return apply_formatter(content_diff, format)
