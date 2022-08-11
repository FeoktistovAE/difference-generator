from gendiff.logic.file_parse import parse_json, parse_yaml


def find_diff_values(intersection, file1, file2):
    keys_with_diff_values = set()
    for i in intersection:
        if file1[i] != file2[i]:
            keys_with_diff_values.add(i)
    return keys_with_diff_values


def find_diff(file1, file2):
    file1_set = set(file1.keys())
    file2_set = set(file2.keys())
    only_file1_set = file1_set - file2_set
    only_file2_set = file2_set - file1_set
    intersection = file1_set & file2_set
    diff_values = find_diff_values(intersection, file1, file2)
    output = ''
    all_keys = sorted(list(file1_set | file2_set))
    for i in all_keys:
        if i in diff_values:
            output += f'- {i}: {file1[i]}\n+ {i}: {file2[i]}\n'
        elif i in only_file1_set:
            output += f'- {i}: {file1[i]}\n'
        elif i in only_file2_set:
            output += f'+ {i}: {file2[i]}\n'
        elif i in intersection:
            output += f'  {i}: {file1[i]}\n'
    return f'{{\n{output}}}'


def generate_diff(path_to_file1, path_to_file2):
    if path_to_file1.endswith('.yml') and path_to_file2.endswith('.yml'):
        return find_diff(
            parse_yaml(path_to_file1), parse_yaml(path_to_file2)
        )
    else:
        return find_diff(
            parse_json(path_to_file1), parse_json(path_to_file2)
        )
