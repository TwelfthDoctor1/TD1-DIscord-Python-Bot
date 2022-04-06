import json


def json_dump(json_dict: dict):
    return json.dumps(json_dict, sort_keys=True, indent=4)


def json_load(json_dict: [str, bytes]):
    return json.loads(json_dict)
