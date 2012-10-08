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

    #raises(TypeError, sqrt, 'not a number')
    #raises(TypeError, "sqrt('not a number')")

    with raises(TypeError):
         sqrt('not a number')


class myraises(object):
    def __init__(self, Exception_spec):
        self._Exception_spec = Exceptoin_spec

    def __enter__(self):
        pass

    def __exit(self, ExType, ExInst, tb):
        if ExType is Excetion_spec or ExType in self._Exception_spec:
            assert True
        else:
            assert False
        return True

def test_should_raise_an_nonnum_exception3():
    with myraises(TypeError):
         sqrt('not a number')
