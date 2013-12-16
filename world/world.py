from .coordinates import Coordinates

class World(object):
    def __init__(self, width=64, height=64):
        self.minx = self.miny = 0
        self.maxx = width - 1
        self.maxy = height - 1

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
