from pymol import cmd
from pymol_sketch import utils
from pymol_sketch import shape
from pymol_sketch import geometry


def sketch_pcoc(selection, state=None, name=None,
                prefix='', suffix='_coc', **kwargs):
    """Create a pseudo atom which indicate the center of coordinate of the
    selection

    USAGE

        sketch_pcoc selection, state=state, name=name,
                    prefix=prefix, suffix=suffix

    ARGUMENTS

        selection   a selection-expression
        state       a state-index if positive number or 0 to all, -1 to current
        name        a name of the pseudoatom, it will
                    automatically specified if None is specified (Default)
        prefix      a prefix of the pseudoatom. it will used only when name is
                    not specified
        suffix      a suffix of the pseudoatom. it will used only when name is
                    not specified

    EXAMPLE

        sketch_pcoc (resn PHE), state=10

    """
    if name is None:
        try:
            name = cmd.get_legal_name(selection)
            name = cmd.get_unused_name(
                '{}{}{}'.format(prefix, name, suffix), 0
            )
        except:
            name = '%s%s' % (prefix, suffix)

    if state is not None:
        com = geometry.find_center_of_coordinates(selection)
        cmd.pseudoatom(name, pos=com, **kwargs)
    else:
        for state in range(1, cmd.count_states()+1):
            com = geometry.find_center_of_coordinates(selection, state=state)
            cmd.pseudoatom(name, pos=com, state=state, **kwargs)


def sketch_pcom(selection, state=None, name=None,
                prefix='', suffix='_coc', **kwargs):
    """Create a pseudo atom which indicate the center of mass of the
    selection

    USAGE

        sketch_pcom selection, state=state, name=name,
                    prefix=prefix, suffix=suffix

    ARGUMENTS

        selection   a selection-expression
        state       a state-index if positive number or 0 to all, -1 to current
        name        a name of the pseudoatom, it will
                    automatically specified if None is specified (Default)
        prefix      a prefix of the pseudoatom. it will used only when name is
                    not specified
        suffix      a suffix of the pseudoatom. it will used only when name is
                    not specified

    EXAMPLE

        sketch_pcoc (resn PHE), state=10

    """
    if name is None:
        try:
            name = cmd.get_legal_name(selection)
            name = cmd.get_unused_name(
                '{}{}{}'.format(prefix, name, suffix), 0
            )
        except:
            name = '%s%s' % (prefix, suffix)

    if state is not None:
        com = geometry.find_center_of_mass(selection)
        cmd.pseudoatom(name, pos=com, **kwargs)
    else:
        for state in range(1, cmd.count_states()+1):
            com = geometry.find_center_of_mass(selection, state=state)
            cmd.pseudoatom(name, pos=com, state=state, **kwargs)


def sketch_scoc(selection, state=-1, name=None, prefix='coc',
                radius=1.0, color='gray', alpha=0.5, verbose=True):
    """
    Draw a sphere which indicate a center of coordinate of the selection

    USAGE

        sketch_scoc selection, state=state, name=name, prefix=prefix,
                    readius=radius, color=color, alpha=alpha

    ARGUMENTS

        selection   a selection-expression
        state       a state-index if positive number or 0 to all, -1 to current
        name        a name of the compiled graphic object, it will
                    automatically specified if None is specified (Default)
        prefix      a prefix of the compiled graphic object. it will used
                    only when name is not specified
        radius      a raidus of the sphere in float
        color       a color of the sphere
        alpha       a alpha-value of the sphere

    EXAMPLE

        sketch_scoc resn PHE, state=10, radius=3.2
        sketch_scoc resn PHE, state=10, color='red'
        sketch_scoc resn PHE, state=10, color=(0, 0.2, 0)

    """
    coc = geometry.find_center_of_coordinates(selection, state=int(state))
    sphere = shape.Sphere(coc, float(radius), utils.str_to_color(color))
    sphere.create(name, prefix, float(alpha))

    if verbose:
        print('Center of coordinate: %.3f, %.3f, %.3f' % (
            coc[0], coc[1], coc[2],
        ))


def sketch_scom(selection, state=-1, name=None, prefix='com',
                radius=1.0, color='gray', alpha=0.5, verbose=True):
    """
    Draw a sphere which indicate a center of mass of the selection

    USAGE

        sketch_scom selection, state=state, name=name, prefix=prefix,
                    readius=radius, color=color, alpha=alpha

    ARGUMENTS

        selection   a selection-expression
        state       a state-index if positive number or 0 to all, -1 to current
        name        a name of the compiled graphic object, it will
                    automatically specified if None is specified (Default)
        prefix      a prefix of the compiled graphic object. it will used
                    only when name is not specified
        radius      a raidus of the sphere in float
        color       a color of the sphere
        alpha       a alpha-value of the sphere

    EXAMPLE

        sketch_scom resn PHE, state=10, radius=3.2
        sketch_scom resn PHE, state=10, color='red'
        sketch_scom resn PHE, state=10, color=(0, 0.2, 0)

    """
    com = geometry.find_center_of_mass(selection, state=int(state))
    sphere = shape.Sphere(com, float(radius), utils.str_to_color(color))
    sphere.create(name, prefix, float(alpha))

    if verbose:
        print('Center of mass: %.3f, %.3f, %.3f' % (
            com[0], com[1], com[2],
        ))


def sketch_bbox(selection, state=-1, name=None, prefix='bbox',
                padding=0, linewidth=2.0,
                color='gray', alpha=0.5, verbose=True):
    """
    Draw a bounding box of the selection

    USAGE

        sketch_bbox selection, state=state, name=name, prefix=prefix,
                    padding=padding, linewidth=linewidth,
                    color=color, alpha=alpha

    ARGUMENTS

        selection   a selection-expression
        state       a state-index if positive number or 0 to all, -1 to current
        name        a name of the compiled graphic object, it will
                    automatically specified if None is specified (Default)
        prefix      a prefix of the compiled graphic object. it will used
                    only when name is not specified
        padding     padding width of the box
        linewidth   line width of the box
        color       a color of the sphere
        alpha       a alpha-value of the sphere

    EXAMPLE

        sketch_bbox resn PHE, state=10
        sketch_bbox resn PHE, state=10, color='red'
        sketch_bbox resn PHE, state=10, color=(0, 0.2, 0)

    """
    (p1, p2, p3, p4, p5, p6, p7, p8) = geometry.find_bounding_box(
        selection, state=int(state),
        dimension=False,
    )
    box = shape.Box(
        p1, p2, p3, p4, p5, p6, p7, p8,
        color=utils.str_to_color(color),
        linewidth=float(linewidth),
    )
    box.create(name, prefix, float(alpha))

    if verbose:
        dimension = geometry.find_bounding_box(
            selection, state=int(state),
        )
        print('Bounding box: %.3f, %.3f, %.3f' % (
            dimension[3],
            dimension[4],
            dimension[5],
        ))
