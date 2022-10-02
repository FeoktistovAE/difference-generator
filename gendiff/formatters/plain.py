def to_str(value):
    if isinstance(value, bool):
        return (str(value)).lower()
    if value is None:
        return 'null'
    if isinstance(value, dict):
        return '[complex value]'
    if isinstance(value, int):
        return str(value)
    return f"'{value}'"


def build_plain(elements, path=''):
    lines = []
    for node in elements:
        if node['action'] == 'has_child':
            lines.append(
                build_plain(node['childrens'], f"{path}{node['key']}."))
        elif node['action'] == 'updated':
            lines.append(
                f"Property '{path}{node['key']}' was updated. "
                f"From {to_str(node['old_value'])} to "
                f"{to_str(node['new_value'])}"
            )
        elif node['action'] == 'removed':
            lines.append(
                f"Property '{path}{node['key']}' was removed"
            )
        elif node['action'] == 'added':
            lines.append(
                f"Property '{path}{node['key']}' was added with value: "
                f"{to_str(node['value'])}"
            )
    result = '\n'.join(lines)
    return result


def render_plain(elements):
    return build_plain(elements)
