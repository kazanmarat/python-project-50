import json
import yaml


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


def add_prefix(content, symb=' '):
    """
    Add a prefix to the given content.

    Args:
        content (str): The content to which the prefix will be added.
        symb (str, optional): The prefix symbol. Defaults to ' '.

    Returns:
        str: The content with the prefix added.
    """
    return f"  {symb} {content}"


def find_files_content(file1, file2):
    """
    Generate a dictionary that contains
    the differences and commonalities
    between of file1 and file2.

    Combine the keys from both dictionaries
    and convert them into a set
    to remove duplicates.
    Iterate through the sorted keys and
    check for the presence of each key
    in both dictionaries.
    Add prefixes according to the following rules.
    1.  If the key is in both dictionaries
    and its values are the same, then add ' '.
    2.  If the key is only in the second dictionary
    or the value of the key in the second dictionary
    differs from the value in the first dictionary,
    then add '+'.
    3.  If the key is only in the first dictionary
    or the value of the key in the first dictionary
    differs from the value in the second dictionary,
    then add '-'.
    """
    sorted_content = sorted({*file1.keys(), *file2.keys()})
    result = {}
    for content in sorted_content:
        if content in file1 and content in file2:
            if file1[content] == file2[content]:
                result[add_prefix(content)] = file1[content]
            else:
                result[add_prefix(content, symb='-')] = file1[content]
                result[add_prefix(content, symb='+')] = file2[content]
        elif content in file2:
            result[add_prefix(content, symb='+')] = file2[content]
        else:
            result[add_prefix(content, symb='-')] = file1[content]
    return result


def to_str(word):
    return str(word).lower()


def json_output(difference):
    result = '{\n'
    for key, value in difference.items():
        result += f'{key}: {to_str(value)}\n'
    result += '}'
    return result


def generate_diff(path):
    file1, file2 = path
    dir1 = file_to_python_obj(file1)
    dir2 = file_to_python_obj(file2)
    # dir1, dir2 = json_to_dict(path)
    dif = find_files_content(dir1, dir2)
    return json_output(dif)
