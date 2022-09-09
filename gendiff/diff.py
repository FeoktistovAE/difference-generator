from gendiff.file_parse import file_parse
from gendiff.formatters.format import apply_formatter


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
    file1 = file_parse(path_to_file1)
    file2 = file_parse(path_to_file2)
    internal_view = find_diff(file1, file2)
    return apply_formatter(file1, file2, format, internal_view)
