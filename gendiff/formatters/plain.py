def convert_to_str(value):
    if isinstance(value, bool):
        return (str(value)).lower()
    elif value is None:
        return 'null'
    elif isinstance(value, dict):
        return '[complex value]'
    return f"'{value}'"


def plain(file1, file2, internal_view):
    joined_keys = file1.keys() | file2.keys()
    lines = []

    def iter_(value, path=''):
        if not isinstance(value, set):
            return convert_to_str(value)
        sorted_keys = sorted(list(value))
        for i in sorted_keys:
            for j in internal_view:
                if j['key'] == i:
                    if j['action'] == 'has_child':
                        iter_(j['childrens'], f'{path}{i}.')

                    elif j['action'] == 'updated':
                        lines.append(
                            f"Property '{path}{i}' was updated. "
                            f"From {convert_to_str(j['old_key_value'])} to "
                            f"{convert_to_str(j['new_key_value'])}"
                        )
                    elif j['action'] == 'removed':
                        lines.append(
                            f"Property '{path}{i}' was removed"
                        )
                    elif j['action'] == 'added':
                        lines.append(
                            f"Property '{path}{i}' was added with value: "
                            f"{convert_to_str(j['key_value'])}"
                        )
        return '\n'.join(lines)
    return iter_(joined_keys)
