from math import sqrt

def test_should_raise_an_nonnum_exception():
    try:
        sqrt("hello")
    
    except TypeError:
        assert True

    except Exception:
        assert False

    else:
        assert False
    


