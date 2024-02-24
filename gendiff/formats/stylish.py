import itertools


INDENT = ' '


def add_prefix(content, depth, symb=''):
    depth_indent = INDENT * (depth * 4 - len(symb))
    return f"{depth_indent}{symb}{content}"


def rename_bool(word):
    incorrect_view = {False: 'false', True: 'true', None: 'null'}
    if word in incorrect_view:
        return incorrect_view[word]
    else:
        return word


def format(dif, depth=0):
    if not isinstance(dif, dict):
        return f'{rename_bool(dif)}'
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
            lines.append(f'{add_prefix(key, current_depth, symb="- ")}: '
                         + f'{format(value[0], current_depth)}')
            lines.append(f'{add_prefix(key, current_depth, symb="+ ")}: '
                         + f'{format(value[1], current_depth)}')
        # if nested dict without changes
        else:
            lines.append(f'{add_prefix(key, current_depth)}: '
                         + f'{format(descrip, current_depth)}')

    result = itertools.chain('{', lines, [current_indent + '}'])
    return '\n'.join(result)
