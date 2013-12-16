from math import sqrt

class Coordinates(object):
    """
    Represents a set of in-world coordinates.

    Assumes a 2D isometric world with the (0,0) corner being the north-most point.
    """

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def offset_by(self, dx=0, dy=0):
        """
        Create a new :py:class:`Coordinates` representing a point offset from the current one
        by `dx` and `dy`.
        """
        newx, newy = self.x + dx, self.y + dy
        return Coordinates(newx, newy)

    def manhattan_distance_to(self, other):
        """
        Calculate `Manhattan distance <https://en.wikipedia.org/wiki/Taxicab_geometry>`_ to
        another point.
        """
        return abs(other.x - self.x) + abs(other.y - self.y)

    def distance_to(self, other):
        """ Calculate Euclidean distance to another point. """
        dx = other.x - self.x
        dy = other.y - self.y
        return sqrt(dx * dx + dy * dy)

    def is_north_of(self, other):
        """ Is this point north of that other point? """
        return self.x + self.y < other.x + other.y

    def is_south_of(self, other):
        """ Is this point south of that other point? """
        return self.x + self.y > other.x + other.y

    def is_west_of(self, other):
        """ Is this point west of that other point? """
        return self.x - self.y < other.x - other.y

    def is_east_of(self, other):
        """ Is this point east of that other point? """
        return self.x - self.y > other.x - other.y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return self.x != other.x or self.y != other.y
