from math import sqrt
from pytest import raises

class myraises(object):
    def __init__(self, Exception_spec):
        self._Exception_spec = Exception_spec

    def __enter__(self):
        pass

    def __exit__(self, ExType, ExInst, tb):
        if ExType is self._Exception_spec or ExType in self._Exception_spec:
            assert True
        else:
            assert False
        return True

def test_should_raise_an_nonnum_exception3():
    with myraises(TypeError):
         sqrt('not a number')




    
##############################################
#         re-written with context-manager

#ex:

def cm(a):
    print 'entering'
    yield a
    print 'exiting'

c = cm('aoeu') # input = 3, input ='hello'

try:
    n = c.next()
    print n*n
finally:
    c.next()






