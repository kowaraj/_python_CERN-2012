class Foo(object):

    def __init__(self, n):
        self.n = n
f = Foo(3)
try:
    f.show()
except AttributeError:
    print 'yes'
    
def show(self):
    print self.n

Foo.show = show

class Vector2D(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
class Vector3D(object):
    def __init__(self, x, y, x):
        self.x = x
        self.y = y
        self.z = z




# def make_adder(a):
#     def adder(b):
#         return a + b
#     return adder


