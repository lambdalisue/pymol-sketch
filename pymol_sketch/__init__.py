from pymol import cmd
from pymol_sketch import commands


def register_commands():
    cmd.extend('sketch_pcoc', commands.sketch_pcoc)
    cmd.extend('sketch_pcom', commands.sketch_pcom)
    cmd.extend('sketch_scoc', commands.sketch_scoc)
    cmd.extend('sketch_scom', commands.sketch_scom)
    cmd.extend('sketch_bbox', commands.sketch_bbox)
