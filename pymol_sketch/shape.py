from chempy import cpv
from pymol import cgo
from pymol import cmd


class CGO(object):
    """A representation object of a compiled graphic object"""
    def __init__(self):
        self._primitive = []

    @property
    def primitive(self):
        return self._primitive

    def create(self, name=None, prefix='cgo', alpha=1.0, state=0):
        """
        Create a compiled graphic object with given name
        """
        if name is None:
            name = cmd.get_unused_name(prefix)
        # remove a object which has a same name
        cmd.delete(name)
        # store origianl value of auto_zoom
        original_auto_zoom = cmd.get('auto_zoom')
        # disable auto_zoom
        cmd.set('auto_zoom', 0.0)
        # create CGO
        cmd.load_cgo(
            [cgo.ALPHA, float(alpha)] + self.primitive, name, state=state
        )
        # restore auto_zoom value
        cmd.set('auto_zoom', float(original_auto_zoom))

    def __add__(self, other):
        """
        Create a new CGO from two CGOs
        """
        cgo = CGO()
        cgo._primitive = self._primitive + other._primitive
        return cgo


class Sphere(CGO):
    """A sphere compiled graphic object

    ARGUMENTS

        p           A coordinate vector (x, y, z) of the center of the sphere
        radius      A radius of the sphere
        color       A color vector (r, g, b) of the sphere

    """
    def __init__(self, p, radius, color):
        x, y, z = p
        r, g, b = color
        self._primitive = [
            cgo.COLOR,
            r, g, b,
            cgo.SPHERE,
            x, y, z,
            radius,
        ]


class Cylinder(CGO):
    """A cylinder compiled graphic object

    ARGUMENTS

        p1          A coordinate vector (x, y, z) of the point 1
        p2          A coordinate vector (x, y, z) of the point 2
        radius      A radius of the cylinder
        color1      A color vector (r, g, b) of the point 1
        color2      A color vector (r, g, b) of the point 2 (optional)

    """
    def __init__(self, p1, p2, radius, color1, color2=None):
        x1, y1, z1 = p1
        x2, y2, z2 = p2
        r1, g1, b1 = color1
        r2, g2, b2 = color2 or color1
        self._primitive = [
            cgo.CYLINDER,
            x1, y1, z1,
            x2, y2, z2,
            radius,
            r1, g1, b1,
            r2, g2, b2
        ]


class Cone(CGO):
    """A cone compiled graphic object

    ARGUMENTS

        p1          A coordinate vector (x, y, z) of the base of the cone
        p2          A coordinate vector (x, y, z) of the tip of the cone
        radius1     A radius of the base of the cone
        color1      A color vector (r, g, b) of the base of the cone
        radius2     A radius of the tip of the cone (optional: 0)
        color2      A color vector (r, g, b) of the tip of the cone (optional)

    """
    def __init__(self, p1, p2, radius1, color1, radius2=0, color2=None):
        x1, y1, z1 = p1
        x2, y2, z2 = p2
        r1, g1, b1 = color1
        r2, g2, b2 = color2 or color1
        # create a cone object
        # https://www.jiscmail.ac.uk/cgi-bin/webadmin?A2=CCP4BB;8318a2d9.1008
        self._primitive = [
            cgo.CONE,
            x1, y1, z1,         # coordinate of the base of the cone
            x2, y2, z2,         # coordinate of the tip of the cone
            radius1, radius2,   # radius of the base and tip of the cone
            r1, g1, b1,         # color for the base of the cone
            r2, g2, b2,         # color for the tip of the cone
            1,                  # if '1' the base of the cone is filled in
            0,                  # if '1' the tip of the cone is filled in
        ]


class Arrow(CGO):
    """An arrow compiled graphic object

    ARGUMENTS

        p1          A coordinate vector (x, y, z) of the arrow base
        p2          A coordinate vector (x, y, z) of the arrow tip
        radius      A radius of the arrow base
        color1      A color vector (r, g, b) of the arrow base
        color2      A color vector (r, g, b) of the arrow hat base (optional)
        color3      A color vector (r, g, b) of the arrow hat tip (optional)
        hlength     A length of the arrow hat (optional)
        hradius     A radius of the arrow hat (optional)
        hlength_scale   A length scale of the arrow hat used when no hlength is
                        specified (optional: 3.0)
        hradius_scale   A radius scale of the arrow hat used when no hradius is
                        specified (optional: 0.6)

    """
    def __init__(self, p1, p2, radius, color1,
                 color2=None, color3=None,
                 hlength=None, hradius=None,
                 hlength_scale=3.0, hradius_scale=0.6):
        if hlength is None:
            hlength = radius * hlength_scale
        if hradius is None:
            hradius = hlength * hradius_scale
        normal = cpv.normalize(cpv.sub(p1, p2))
        pM = cpv.add(cpv.scale(normal, hlength), p2)
        line = Cylinder(p1, pM, radius, color1, color2)
        cone = Cone(
            pM, p2, hradius, color2 or color1, radius2=0, color2=color3
        )
        self._primitive = (line + cone).primitive


class Box(CGO):
    """A box compiled graphic object

    ARGUMENTS
        p{n}        A coordinate vector (x, y, z) of {n} in the figure
        color       A color vector (r, g, b) of the box
        linewidth   A line width (Default: 2.0)

    FIGURE

        Individual p{n} indicate the vertex of the following box

                     5-----6
                    /|    /|
        y  z       / 8-- / 7
        | /       1-----2 /
        |/        |/    |/
        -----x    4-----3

    """
    def __init__(self, p1, p2, p3, p4, p5, p6, p7, p8,
                 color=None, linewidth=2.0):
        x1, y1, z1 = p1
        x2, y2, z2 = p2
        x3, y3, z3 = p3
        x4, y4, z4 = p4
        x5, y5, z5 = p5
        x6, y6, z6 = p6
        x7, y7, z7 = p7
        x8, y8, z8 = p8
        r, g, b = color
        self._primitive = [
            cgo.LINEWIDTH, linewidth,
            cgo.BEGIN, cgo.LINES,
            cgo.COLOR, r, g, b,
            # front surface
            cgo.VERTEX, x1, y1, z1,
            cgo.VERTEX, x2, y2, z2,

            cgo.VERTEX, x2, y2, z2,
            cgo.VERTEX, x3, y3, z3,

            cgo.VERTEX, x3, y3, z3,
            cgo.VERTEX, x4, y4, z4,

            cgo.VERTEX, x4, y4, z4,
            cgo.VERTEX, x1, y1, z1,

            # back surface
            cgo.VERTEX, x5, y5, z5,
            cgo.VERTEX, x6, y6, z6,

            cgo.VERTEX, x6, y6, z6,
            cgo.VERTEX, x7, y7, z7,

            cgo.VERTEX, x7, y7, z7,
            cgo.VERTEX, x8, y8, z8,

            cgo.VERTEX, x8, y8, z8,
            cgo.VERTEX, x5, y5, z5,

            # left side surface
            cgo.VERTEX, x1, y1, z1,
            cgo.VERTEX, x5, y5, z5,

            cgo.VERTEX, x4, y4, z4,
            cgo.VERTEX, x8, y8, z8,

            # right side surface
            cgo.VERTEX, x2, y2, z2,
            cgo.VERTEX, x6, y6, z6,

            cgo.VERTEX, x3, y3, z3,
            cgo.VERTEX, x7, y7, z7,

            cgo.END
        ]
