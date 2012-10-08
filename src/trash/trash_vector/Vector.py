def Vector(names):
    
    class Vector(object):

        #d == position_of_name
        d1 = { name:pos for pos,name in enumerate(names)}
        d2 = {}
        for pos, name in enumerate(names):
            d2[name] = pos
        d3 = dict([(name, pos) for pos, name in enumerate(names)])

        # print d1
        # print d2
        # print d3

        _names = d1

        def __init__(self, *data):
            self._data = {name:pos for name,pos in zip(self._names, data)}
            
        def __getitem__(self, i):
            return self._data[i]

        def __setitem__(self, n, value):
            self._data[n] = value
            
        def __getattr__(self, name):
            print '__getattr__: ', self._data 
            return self._data[name]

    
    def make_accessors(name):
        def get(self):
            return self._data[name]
        def set(self, value):
            self._data[name] = value
        return get, set

    print names
    for name in names:
        setattr(Vector, name, property(*make_accessors(name)))
        
           
    return Vector

Vector2D = Vector('xy')
Vector3D = Vector('xyz')

# print '###### test ######'

print 'create a instance of Vector2D'
v2d = Vector2D(666,777)

print 'get.x'
print v2d.x
print 'set.x '
v2d.x = 4

print 'props'
print 'x = ', v2d.x
print 'x = ', v2d.x
print 'set a new x'
v2d.x = 5
print 'x = ', v2d.x
print 'x = ', v2d.x
