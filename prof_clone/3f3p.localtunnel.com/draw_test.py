from mock import Mock
from particle import Particle, Universe

def test_universe_should_draw_particles_in_correct_place():
    m = Mock()
    u = Universe(None, None, m)
    u.add_particle(Particle(30, 40,50, None, None))
    u.add_particle(Particle( 3,  5, 4, None, None))
    u.draw(m)
    assert ('draw_circle', (30,40,50),{}) in m.method_calls
    assert ('draw_circle', ( 3, 5, 4),{}) in m.method_calls
    assert len(m.method_calls) == 2
