from math import sqrt

class Coordinates(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def offset_by(self, dx=0, dy=0):
        newx, newy = self.x + dx, self.y + dy
        return Coordinates(newx, newy)

    def manhattan_distance_to(self, other):
        return abs(other.x - self.x) + abs(other.y - self.y)

    def distance_to(self, other):
        dx = other.x - self.x
        dy = other.y - self.y
        return sqrt(dx * dx + dy * dy)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return self.x != other.x or self.y != other.y
