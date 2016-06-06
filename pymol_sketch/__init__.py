from pymol import cmd
from pymol_sketch import commands


def register_commands():
    cmd.extend('sketch_pseudo_coc', commands.sketch_pseudo_coc)
    cmd.extend('sketch_pseudo_com', commands.sketch_pseudo_com)
    cmd.extend('sketch_coc', commands.sketch_coc)
    cmd.extend('sketch_com', commands.sketch_com)
    cmd.extend('sketch_bbox', commands.sketch_bbox)
    cmd.extend('sketch_radgyr', commands.sketch_radgyr)
