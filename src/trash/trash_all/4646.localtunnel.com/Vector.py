class Vector(object):

    def __init__(self, x, y):
        self.x, self.y = x,y

    def __add__(self, other):
        return Vector(self.x + other.x,
                      self.y + other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar,
                      self.y * scalar)

    __rmul__ = __mul__


