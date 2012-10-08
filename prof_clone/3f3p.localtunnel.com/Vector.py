from operator import isNumberType
from math import sqrt

def Vector(component_names):

    class Vector(object):

        def __init__(self, *data):
            if len(data) != len(component_names):
                raise TypeError("%d-dimensional vector's (%s) constructor given %d components." %
                                (len(component_names), Vector.__name__, len(data)))
            self._data = list(data)

        def __getitem__(self, dimension):
            return self._data[dimension]

        def __setitem__(self, dimension, value):
            self._data[dimension] = value

        def __add__(self, other):
            return Vector(*[s+o for s,o in zip(self, other)])

        def __mul__(self, scalar):
            if not isNumberType(scalar):
                raise TypeError("Vectors can only be multiplied by numeric values, not %s" % (type(scalar),))
            return Vector(*[s*scalar for s in self])

        __rmul__ = __mul__

        def __div__(self, scalar):
            if not isNumberType(scalar):
                raise TypeError("Vectors can only be divided by numeric values, not %s" % (type(scalar),))
            return Vector(*[s/scalar for s in self])

        def __eq__(self, other):
            for s,o in zip(self, other):
                if s != o:
                    return False
            else:
                return True

        def __repr__(self):
            return "%s(%s)" % (Vector.__name__, ','.join(map(str, self._data)))

        def __abs__(self):
            return sqrt(sum([x*x for x in self]))

        def normalized(self):
            l = abs(self)
            return Vector(*[x/l for x in self])

        def normalize(self):
            l = abs(self)
            for i,_ in enumerate(self):
                self[i] /= l

    def make_accessors(position):
        def get(self):
            return self._data[position]
        def set(self, value):
            self._data[position] = value

        return get, set

    for position, name in enumerate(component_names):
        setattr(Vector, name, property(*make_accessors(position)))

    Vector.__name__ = "Vector(%r)" % (component_names)

    return Vector

Vector2D = Vector('xy')
Vector2D.__name__ = "Vector2D"
Vector3D = Vector('xyz')
Vector3D.__name__ = "Vector3D"
