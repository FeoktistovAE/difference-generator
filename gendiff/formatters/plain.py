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


def build_plain(content, path=''):
    lines = []
    for i in content:
        if i['action'] == 'has_child':
            lines.append(
                build_plain(i['childrens'], f"{path}{i['key']}."))
        elif i['action'] == 'updated':
            lines.append(
                f"Property '{path}{i['key']}' was updated. "
                f"From {to_str(i['old_value'])} to "
                f"{to_str(i['new_value'])}"
            )
        elif i['action'] == 'removed':
            lines.append(
                f"Property '{path}{i['key']}' was removed"
            )
        elif i['action'] == 'added':
            lines.append(
                f"Property '{path}{i['key']}' was added with value: "
                f"{to_str(i['value'])}"
            )
    result = '\n'.join(lines)
    return result


def render_plain(content):
    return build_plain(content)
