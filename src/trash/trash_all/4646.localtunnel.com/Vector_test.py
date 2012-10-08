from Vector import Vector

from pytest import mark

def test_should_be_instantiable_with_2_args():
    Vector(1,2)

@mark.parametrize(('x','y'), ((1,2),
                              (3,4),
                              (5,6)))
def test_should_be_able_to_access_components_by_name(x,y):
    v = Vector(x,y)
    assert v.x == x
    assert v.y == y

def test_should_be_addable():
    v = Vector(1,2)
    w = Vector(3,5)
    a = v + w
    assert a.x == 4
    assert a.y == 7

def test_should_be_incrementable():
    v = Vector(4,6)
    w = Vector(-1,3)
    v += w
    assert v.x == 3
    assert v.y == 9
    assert w.x == -1
    assert w.y ==  3

def test_should_by_multiplyable_by_scalar_from_right():
    v = Vector(6,2)
    w = v * 3
    assert w.x == 18
    assert w.y ==  6

def test_should_by_multiplyable_by_scalar_from_left():
    v = Vector(5,3)
    w = 3 * v
    assert w.x == 15
    assert w.y ==  9
