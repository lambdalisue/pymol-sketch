from chempy import cpv
from pymol import cmd


def find_center_of_coordinates(selection, state=0):
    """
    Find center of coordinates of the selection and return the value

    USAGE

        find_center_of_coordinates selection
        find_center_of_coordinates selection, state=state

    ARGUMENTS

        selection   a selection-expression
        state       a state-index if positive number or 0 to all, -1 to current

    """
    # find middle x, y, z coordinate of the selection
    minc, maxc = cmd.get_extent(selection, state=state)
    coc = [float(l + (u - l) / 2.0) for l, u in zip(minc, maxc)]
    return coc


def find_center_of_mass(selection, state=0):
    """
    Find center of mass of the selection and return the value

    USAGE

        find_center_of_mass selection
        find_center_of_mass selection, state=state

    ARGUMENTS

        selection   a selection-expression
        state       a state-index if positive number or 0 to all, -1 to current

    """
    model = cmd.get_model(selection, state=state)
    com = cpv.get_null()
    # iterate all atoms and add vectors of center of mass of each atoms
    for atom in model.atom:
        com = cpv.add(com, atom.coord)
    com = cpv.scale(com, 1.0 / len(model.atom))
    return com


def find_bounding_box(selection, state=0, padding=0, dimension=True):
    """
    Find a bounding box of the selection and return the value

    USAGE

        find_bounding_box selection
        find_bounding_box selection, state=state

    ARGUMENTS

        selection   a selection-expression
        state       a state-index if positive number or 0 to all, -1 to current
        padding     padding width of the box
        dimension   True to return dimension instead of coordinates

    RETURN

        dimension (dimension=True)

        (minx, miny, minz, widthx, widthy, widthz)

        coordinate (dimension=False)

        (p1, p2, p3, p4, p5, p6, p7, p8)

        p{n} := (x, y, z)

    FIGURE

        Individual p{n} indicate the vertex of the following box

                     5-----6
                    /|    /|
        y  z       / 8-- / 7
        | /       1-----2 /
        |/        |/    |/
        -----x    4-----3


    """
    ((minx, miny, minz), (maxx, maxy, maxz)) = cmd.get_extent(
        selection, state=state
    )
    minx = minx - padding
    miny = miny - padding
    minz = minz - padding
    maxx = maxx + padding
    maxy = maxy + padding
    maxz = maxz + padding

    if dimension:
        return (
            minx,
            miny,
            minz,
            maxx - minx,
            maxy - miny,
            maxz - minz,
        )
    else:
        return (
            (minx, maxy, minz),
            (maxx, maxy, minz),
            (maxx, miny, minz),
            (minx, miny, minz),
            (minx, maxy, maxz),
            (maxx, maxy, maxz),
            (maxx, miny, maxz),
            (minx, miny, maxz),
        )

