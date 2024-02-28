def rename_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    incorrect_view = {False: 'false', True: 'true', None: 'null'}
    if value in incorrect_view:
        return incorrect_view[value]
    else:
        return f"'{value}'"


def differents(value, type):
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
    property = properties(dif)
    result = []
    for name, feature in property:
        result.append(f"Property '{name}' was {feature}")
    return '\n'.join(result)
