from test_helpers import assert_evolution, approximately_eq
from operator import eq
from particle import Particle

def test_Particle_speed_should_remain_constant():
    almost_eq = approximately_eq(13)
    assert_speed_unchanged = assert_evolution(lambda:abs(p.vel), almost_eq)
    p = Particle(30, 40, 50, 60, 70)
    for dt in xrange(10,30,1):
        p.move(dt/1000.0)
        assert_speed_unchanged()
