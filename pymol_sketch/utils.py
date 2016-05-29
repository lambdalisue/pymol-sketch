import re
from pymol import cmd


NUMBER_PATTERN = r'(?:\d+(?:\.\d+)?|\.\d+)'


def str_to_vector(s):
    pattern = r'\s*{0}(?:\s*,\s*{0})*\s*'.format(NUMBER_PATTERN)
    m = re.search(pattern, s)
    if m is not None:
        return list(map(float, m.group().split(',')))
    else:
        raise AttributeError('A value requires to be like (0, 1, ...)')


def str_to_color(c):
    color_map = dict(cmd.get_color_indices())
    if c in color_map:
        return cmd.get_color_tuple(color_map[c])
    return str_to_vector(c)
