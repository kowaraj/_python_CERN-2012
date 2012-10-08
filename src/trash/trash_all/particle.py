import sys
from Vector import Vector2D

class Particle(object):

    def __init__(self, r,  x,y, vx, vy):
        self.r = r
        self.pos = Vector2D( x, y)
        self.vel = Vector2D(vx,vy)

    def move(self, dt):
        self.pos += self.vel * dt

    def boundary_bounce(self, bounds):

        def chunk(n, iterable):
            iterator = iter(iterable)
            while True:
                yield [iterator.next() for _ in xrange(n)]

        for i, (lo, hi) in enumerate(chunk(2, bounds)):

            if self.pos[i] + self.r > hi:
                self.pos[i] = hi - self.r
                self.vel[i] = - self.vel[i]
                
            if self.pos[i] - self.r < lo:
                self.pos[i] = lo + self.r
                self.vel[i] = - self.vel[i]

class Universe(object):

    def __init__(self, width, height, DisplayType):
        self.particles = [Particle(10, width/2, height/2, 100,  50),
                          Particle(20, width/4, height/2,  50, 100),
                          Particle(30, width/2, height/4,  75,  90),
                          Particle(25, width/2, height/2,  20, 110),
                          Particle(15, width/2, height/2, 140,   5),
                          ]
        self.display = DisplayType(width, height, self)

    def evolve(self, dt, bounds):
        for particle in self.particles:
            particle.move(dt)
            particle.boundary_bounce(bounds)

    def draw(self, display):
        for p in self.particles:
            display.draw_circle(p.r, *p.pos)

if sys.argv[1] == 'pyg':
    from PygletDisplay import PygletDisplay as Display
if sys.argv[1] == 'tk':
    from TkinterDisplay import TkinterDisplay as Display


Universe(600, 400, Display)
