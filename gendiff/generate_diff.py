import json


def json_to_dict(path):
    path1, path2 = path
    file1 = json.load(open(path1))
    file2 = json.load(open(path2))
    return file1, file2


def add_prefix(content, symb=' '):
    """
    Add a prefix to the given content.

    Args:
        content (str): The content to which the prefix will be added.
        symb (str, optional): The prefix symbol. Defaults to ' '.

    Returns:
        str: The content with the prefix added.
    """
    return symb + ' ' + content


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


def json_output(difference):
    result = '{\n'
    for key, value in difference.items():
        result += f'{key}: {json.dumps(value)} \n'
    result += '}'
    return result


def generate_diff(path):
    dir1, dir2 = json_to_dict(path)
    dif = find_files_content(dir1, dir2)
    return json_output(dif)
