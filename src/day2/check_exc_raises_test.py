from math import sqrt
from pytest import raises

def test_should_raise_an_nonnum_exception():
    try:
        sqrt("hello")
    
    except TypeError:
        assert True
      
    except Exception:
        assert False
    else:
        fail("qqq fail")
    

   

def abstr_check_exc(ExpectedExceptionType, func, *args, **kwds):
    try:
        func(*args, **kwds)
    except (ExpectedExceptionType):
        assert True
    except Exception:
        assert False
    else:
        fail("qqq2 fail")


def test_should_raise_an_nonnum_exception2():
    abstr_check_exc(TypeError, sqrt, 'not a number')

    raises(TypeError, sqrt, 'not a number')
    raises(TypeError, "sqrt('not a number')")

with raises(TypeError):
    sqrt('not a number')



