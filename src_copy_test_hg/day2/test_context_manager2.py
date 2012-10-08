from math import sqrt
    
##############################################
#         re-written with context-manager

#ex:

#def cm(a):
#    print 'entering'
#    yield a
#    print 'exiting'
#
#c = cm('aoeu') # input = 3, input ='hello'
#
#try:
#    n = c.next()
#    print n*n
#finally:
#    c.next()


from contextlib import contextmanager

#@contextmanager
#def cm2(a):
#    print 'entering2'
#    try:
#        yield a
#    finally:
#        print 'exiting2'
#
#with cm2('auoe') as n:
#    print n*n


@contextmanager
def myraises2(E_spec):
    try:
        yield
    except E_spec:
        assert True
    except Exception:
        assert False
    else:
        assert False

def test_sqrt_should_raise_TypeError_on_non_numerical_input3():
    with myraises2(TypeError):
        sqrt('not a number')

def test_sqrt_should_raise_TypeError_on_non_numerical_input4():
    with myraises2(TypeError):
        sqrt('asdf')






