import json


def render_json(content):
    return json.dumps(content, indent=1)
