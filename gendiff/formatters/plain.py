def to_str(content):
    if isinstance(content, bool):
        return (str(content)).lower()
    elif content is None:
        return 'null'
    elif isinstance(content, dict):
        return '[complex value]'
    return f"'{content}'"


def plain(content, path='', lines=[]):

    if not isinstance(content, list):
        return to_str(content)
    for i in content:
        if i['action'] == 'has_child':
            plain(i['childrens'], f"{path}{i['key']}.")
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
    return '\n'.join(lines)
