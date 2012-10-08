from pytest import raises
from operator import eq, gt
from assert_evol import assert_evolution
from particle import Particle


def test_particleAcc_should_accelerate():

    p = ParticleAcc(10, 200, 200, 100,  50)
    def val():
        return sqrt(p.vel.x**2 + p.vel.y**2)

    print 'vel = ', val()
    p.move(1.0/60)
    print 'vel = ', val()
    
    assert_invariant = assert_evolution(val, eq)
    p.move(1.0/60)
    assert_invariant()
    p.move(1.0/60)
    assert_invariant()
    p.move(1.0/60)
    assert_invariant()
    print 'ok!'
    
test_particleAcc_should_accelerate()

def test_assert_evolution_should_fail_with_non_constant_expression_and_eq():
    assert_invariant = assert_evolution(lambda:x, eq)
    x = 1
    assert_invariant()
    assert_invariant()
    x = 2
    with raises(AssertionError):
        assert_invariant()

def test_assert_evolution_should_work_with_increasing_expression_and_gt():
    assert_increasing = assert_evolution(lambda:x, gt)
    for x in range(20):
        assert_increasing()

    x -= 2
    with raises(AssertionError):
        assert_increasing()

def test_assert_evolution_should_fail_with_constant_expression_and_gt():
    assert_increasing = assert_evolution(lambda:x, gt)
    x = 1
    assert_increasing()
    with raises(AssertionError):
        assert_increasing()

