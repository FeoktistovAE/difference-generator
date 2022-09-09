import json


def get_json(file1, file2, internal_view):
    joined_keys = file1.keys() | file2.keys()

    def iter_(value):
        lines = []
        sorted_keys = sorted(list(value))
        for i in sorted_keys:
            for j in internal_view:
                if j['key'] == i:
                    if j['action'] == 'has_child':
                        lines.append({'key': i, 'status': 'parent', 'value': iter_(j['childrens'])})
                    elif j['action'] == 'updated':
                        lines.append(
                            {'key': i, 'status': 'updated', 'old_value': j['old_key_value'],
                             'new_value': j['new_key_value']}
                        )
                    elif j['action'] == 'removed':
                        lines.append({'key': i, 'status': 'removed', 'value': j['key_value']})
                    elif j['action'] == 'added':
                        lines.append({'key': i, 'status': 'added', 'value': j['key_value']})
                    elif j['action'] == 'unchanged':
                        lines.append({'key': i, 'status': 'unchanged', 'value': j['key_value']})
        return lines
    return json.dumps(iter_(joined_keys), indent=2)
