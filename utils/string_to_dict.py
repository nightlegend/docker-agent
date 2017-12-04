import json


# Parse a string to dict type.
def parse_to_dict(parse_string):
    json_str = json.dumps(parse_string)
    dict_res = json.loads(json_str)
    # print(type(dict_res))
    return dict_res
