from .coordinates import Coordinates

class World(object):
    """
    Represents a complete world of a given width and height.
    """
    def __init__(self, width=64, height=64):
        self.minx = self.miny = 0
        self.maxx = width - 1
        self.maxy = height - 1

    @property
    def northmost(self):
        """ The north-most point of this world (usually (0,0)) as :py:class:`world.Coordinates`. """
        return Coordinates(self.minx, self.miny)

    @property
    def southmost(self):
        """ The south-most point of this world (usually (0,0)) as :py:class:`world.Coordinates`. """
        return Coordinates(self.maxx, self.maxy)

    @property
    def eastmost(self):
        """ The east-most point of this world (usually (0,0)) as :py:class:`world.Coordinates`. """
        return Coordinates(self.maxx, self.miny)

    @property
    def westmost(self):
        """ The west-most point of this world (usually (0,0)) as :py:class:`world.Coordinates`. """
        return Coordinates(self.minx, self.maxy)
