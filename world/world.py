from .coordinates import Coordinates

class World(object):
    minx = miny = 0
    maxx = maxy = 63

    @property
    def northmost(self):
        return Coordinates(self.minx, self.miny)

    @property
    def southmost(self):
        return Coordinates(self.maxx, self.maxy)

    @property
    def eastmost(self):
        return Coordinates(self.maxx, self.miny)

    @property
    def westmost(self):
        return Coordinates(self.minx, self.maxy)
