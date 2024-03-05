from gendiff.formats import stylish
from gendiff.formats import plain
from gendiff.formats import json_format
from gendiff.parser import parse


def sort_files_content(dict1, dict2):
    '''
    Sorts the content of two dictionaries and returns a dictionary
    representing the differences between the two.

    Args:
        dict1 (dict): The first dictionary to compare.
        dict2 (dict): The second dictionary to compare.

    Returns:
        dict: A dictionary representing the differences
        between dict1 and dict2.
    '''
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
    '''
    Generate the difference between two files and return
    the result in the specified format.

    Args:
        file1: The first file to compare.
        file2: The second file to compare.
        format (str): The format in which to return the difference.
        Default is 'stylish'.

    Returns:
        str: The difference between the two files in the specified format.

    Raises:
        Exception: If an invalid format is provided.
    '''
    dict1 = parse(file1)
    dict2 = parse(file2)
    dif = sort_files_content(dict1, dict2)
    if format == 'stylish':
        return stylish(dif)
    elif format == 'plain':
        return plain(dif)
    elif format == 'json':
        return json_format(dif)
    else:
        raise Exception('Invalid format.')
