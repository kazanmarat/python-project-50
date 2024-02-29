def rename_value(value):
    '''
    Function to rename a value to a different representation.
    '''
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, (int)) and not isinstance(value, bool):
        return value
    elif isinstance(value, (str)) and not isinstance(value, bool):
        return f"'{value}'"
    correct_view = {False: 'false', True: 'true', None: 'null'}
    return correct_view[value]


def differents(value, type):
    '''
    Return a string based on the given type and value,
    using the rename_value
    function to format the output.
    '''
    if type == 'added':
        return f'added with value: {rename_value(value)}'
    elif type == 'deleted':
        return 'removed'
    elif type == 'changed':
        old_value = value.get('old_value')
        new_value = value.get('new_value')
        return (f'updated. From {rename_value(old_value)}'
                + f' to {rename_value(new_value)}')
    else:
        return


def properties(dif, parent=''):
    '''
    Generate a list of properties and their differences.

    Args:
        dif: A dictionary representing the input differences.
        parent: A string representing of the full path to the root
                (default is an empty string).

    Returns:
        A list of tuples containing the property name and its differences.
    '''
    lines = []
    types = {'added',
             'deleted',
             'changed'
             }
    for name, descrip in dif.items():
        type = descrip.get('type')
        value = descrip.get('value')
        name = f'{parent}{name}'
        if type in types:
            lines.append((name, differents(value, type)))
        elif type == 'unchanged':
            continue
        elif type == 'nested':
            lines.extend((properties(value, name + '.')))
    return lines


def format(dif):
    '''
    Format the given difference and return
    a string representation of its properties.'''
    property = properties(dif)
    result = []
    for name, feature in property:
        result.append(f"Property '{name}' was {feature}")
    return '\n'.join(result)
