import json
import yaml


def parse(data, format=False):
    '''
    Converts a file to a Python object based on the file format.
    '''
    if format is False:
        format = data.split('.')[-1]
    file = read_file(data)
    if format == 'json':
        return json_to_dict(file)
    elif format == 'yml' or format == 'yaml':
        return yaml_to_dict(file)
    else:
        raise Exception('Invalid file format.')


def read_file(filepath):
    with open(filepath) as file:
        output = file.read()
    return output


def json_to_dict(path):
    '''
    Convert a JSON file to a Python dictionary.
    '''
    return json.loads(path)


def yaml_to_dict(path):
    '''
    Convert a YAML file to a Python dictionary.
    '''
    return yaml.safe_load(path)
