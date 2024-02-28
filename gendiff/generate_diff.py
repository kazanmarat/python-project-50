import json
import yaml
from gendiff.formats import stylish
from gendiff.formats import plain
from gendiff.formats import f_json


def file_to_python_obj(file):
    if file.endswith('.json'):
        return json_to_dict(file)
    elif file.endswith('.yml') or file.endswith('.yaml'):
        return yaml_to_dict(file)
    else:
        raise Exception('Invalid file format.')


def json_to_dict(path):
    with open(path) as file:
        output = json.load(file)
    return output


def yaml_to_dict(path):
    with open(path) as file:
        output = yaml.safe_load(file)
    return output


def sort_files_content(dict1, dict2):
    sorted_content = sorted({*dict1.keys(), *dict2.keys()})
    result = {}
    for content in sorted_content:
        dict1_content = dict1.get(content)
        dict2_content = dict2.get(content)

        if content in dict1 and content in dict2:
            if (isinstance(dict1_content, dict)
               and isinstance(dict2_content, dict)):
                result[content] = {'type': 'nested',
                                   'value': sort_files_content(dict1_content,
                                                               dict2_content)}

            elif dict1_content == dict2_content:
                result[content] = {'type': 'unchanged', 'value': dict1_content}
            else:
                result[content] = {'type': 'changed',
                                   'value': {'old_value': dict1_content,
                                             'new_value': dict2_content}}

        elif content in dict1:
            result[content] = {'type': 'deleted', 'value': dict1_content}
        else:
            result[content] = {'type': 'added', 'value': dict2_content}
    return result


def generate_diff(file1, file2, format='stylish'):
    dict1 = file_to_python_obj(file1)
    dict2 = file_to_python_obj(file2)
    dif = sort_files_content(dict1, dict2)
    if format == 'stylish':
        return stylish(dif)
    elif format == 'plain':
        return plain(dif)
    elif format == 'json':
        return f_json(dif)
    else:
        raise Exception('Invalid format.')
