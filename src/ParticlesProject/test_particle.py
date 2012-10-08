from pytest import raises
from operator import eq, gt
from assert_evol import assert_evolution
from particle import Particle, ParticleAcc, ParticleDec, ParticleCM, Universe
from math import sqrt
from mock import Mock



def test_particle_should_accept_diff_formats_of_colours():

    r, g, b = 0.3, 0.2, 0.1
    c = ParticleColour.rgb01(r,g,b)

    p = ParticleAcc(30, 40, 50, None, None, c)

    assert (p.colour.as_rgb01 == (r,g,b))
    assert (p.colour.as_name == 'white')
    assert (p.colour.as_rgb255 == (30, 20, 10))
    

def test_universe():

    disp = Mock()
    u = Universe(600, 400, disp)
    u.add_particle(ParticleAcc(30, 40, 50, None, None))
    u.draw(disp)

    print disp.method_calls
    assert ('draw_circle', (30,40,50), {}) in disp.method_calls
    assert ('draw_circle', (30,40,4000), {}) in disp.method_calls
    assert len(disp.method_calls) == 1
    

def test_particleAcc_should_accelerate():

    p = ParticleAcc(10, 200, 200, 100,  50)
    def val():
        return sqrt(p.vel.x**2 + p.vel.y**2)

    print 'vel3 = ', val()
    p.move(1.0/60)
    print 'vel = ', val()
    
    assert_invariant = assert_evolution(val, eq)

    p.move(1.0/60)
    print 'vel = ', val()
    assert_invariant()

    p.move(1.0/60)
    print 'vel = ', val()
    assert_invariant()

    p.move(1.0/60)
    print 'vel = ', val()
    assert_invariant()
    print 'ok!'
    

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

