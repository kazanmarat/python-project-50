import itertools


INDENT = ' '


def add_prefix(content, depth, symb=''):
    '''
    Adds a prefix to the given content string
    based on the depth and symbol provided.
    '''
    depth_indent = INDENT * (depth * 4 - len(symb))
    return f"{depth_indent}{symb}{content}"


def rename_value(value):
    '''
    Rename bool value to their original representation.
    '''
    if isinstance(value, (int, str)) and not isinstance(value, bool):
        return value
    correct_view = {False: 'false', True: 'true', None: 'null'}
    return correct_view[value]


def format(dif, depth=0):
    '''
    Recursively formats a nested dictionary `dif`
    and returns a string representation.

    Args:
        dif: The input nested dictionary to be formatted.
        depth: The current depth of the recursion (default is 0).

    Returns:
        A string representation of the formatted nested dictionary.
    '''
    if not isinstance(dif, dict):
        return f'{rename_value(dif)}'
    current_indent = INDENT * 4 * depth
    current_depth = depth + 1
    types = {'added': "+ ",
             'deleted': "- ",
             'unchanged': "  ",
             'nested': "  "
             }
    lines = []
    for key, descrip in dif.items():
        # when descrip just value
        if not isinstance(descrip, dict):
            lines.append(f'{add_prefix(key, current_depth)}: '
                         + f'{format(descrip, current_depth)}')
            continue
        value = descrip.get('value')
        type = descrip.get('type')
        if type in types:
            prefix = types[type]
            lines.append(f'{add_prefix(key, current_depth, prefix)}: '
                         + f'{format(value, current_depth)}')
        elif type == 'changed':
            old_value = value.get('old_value')
            new_value = value.get('new_value')
            lines.append(f'{add_prefix(key, current_depth, symb="- ")}: '
                         + f'{format(old_value, current_depth)}')
            lines.append(f'{add_prefix(key, current_depth, symb="+ ")}: '
                         + f'{format(new_value, current_depth)}')
        # if nested dict without changes
        else:
            lines.append(f'{add_prefix(key, current_depth)}: '
                         + f'{format(descrip, current_depth)}')

    result = itertools.chain('{', lines, [current_indent + '}'])
    return '\n'.join(result)
