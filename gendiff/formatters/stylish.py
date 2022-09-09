import itertools


def convert_to_str(value):
    if isinstance(value, bool):
        return (str(value)).lower()
    elif value is None:
        return 'null'
    return str(value)


def stylish(file1, file2, internal_view):
    replacer = '  '
    spaces_count = 1
    joined_keys = file1.keys() | file2.keys()

    def iter_(value, depth):
        deep_indent_size = depth + spaces_count
        deep_indent = replacer * deep_indent_size
        current_indent = replacer * depth
        lines = []
        if isinstance(value, dict):
            for key, val in value.items():
                lines.append(f'  {deep_indent}  {key}: {iter_(val, deep_indent_size+1)}')
            result = itertools.chain("{", lines, [deep_indent + "}"])
            return "\n".join(result)
        elif not isinstance(value, set):
            return convert_to_str(value)
        sorted_keys = sorted(list(value))
        for i in sorted_keys:
            for j in internal_view:
                if j['key'] == i:
                    if j['action'] == 'has_child':
                        lines.append(
                            f'{deep_indent}  {i}: {iter_(j["childrens"], deep_indent_size+1)}'
                        )
                    elif j['action'] == 'updated':
                        lines.append(
                            f'{deep_indent}- {i}: {iter_(j["old_key_value"], deep_indent_size)}'
                        )
                        lines.append(
                            f'{deep_indent}+ {i}: {iter_(j["new_key_value"], deep_indent_size)}'
                        )
                    elif j['action'] == 'removed':
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
