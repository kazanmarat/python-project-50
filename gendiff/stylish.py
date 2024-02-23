import itertools


def add_prefix(content, depth, symb=''):
    INDENT = ' '
    depth_indent = INDENT * (depth * 4 - len(symb))
    return f"{depth_indent}{symb}{content}"


def rename_bool(word):
    incorrect_view = {False: 'false', True: 'true', None: 'null'}
    if word in incorrect_view:
        return incorrect_view[word]
    else:
        return word


def format(dif):
    def inner(dif, depth):
        if not isinstance(dif, dict):
            return f'{rename_bool(dif)}'
        current_indent = INDENT * 4 * depth
        current_depth = depth + 1
        lines = []
        for key, descrip in dif.items():
            # when descrip just value
            if not isinstance(descrip, dict):
                lines.append(f'{add_prefix(key, current_depth)}: '
                             + f'{inner(descrip, current_depth)}')
                continue
            value = descrip.get('value')
            type = descrip.get('type')
            if type == 'added':
                lines.append(f'{add_prefix(key, current_depth, symb="+ ")}: '
                             + f'{inner(value, current_depth)}')
            elif type == 'deleted':
                lines.append(f'{add_prefix(key, current_depth, symb="- ")}: '
                             + f'{inner(value, current_depth)}')
            elif type == 'unchanged':
                lines.append(f'{add_prefix(key, current_depth, symb="  ")}: '
                             + f'{inner(value, current_depth)}')
            elif type == 'changed':
                lines.append(f'{add_prefix(key, current_depth, symb="- ")}: '
                             + f'{inner(value[0], current_depth)}')
                lines.append(f'{add_prefix(key, current_depth, symb="+ ")}: '
                             + f'{inner(value[1], current_depth)}')
            elif type == 'nested':
                lines.append(f'{add_prefix(key, current_depth, symb="  ")}: '
                             + f'{inner(value, current_depth)}')
            # if nested dict without changes
            else:
                lines.append(f'{add_prefix(key, current_depth)}: '
                             + f'{inner(descrip, current_depth)}')

        result = itertools.chain('{', lines, [current_indent + '}'])
        return '\n'.join(result)
    depth = 0
    INDENT = ' '
    return inner(dif, depth)
