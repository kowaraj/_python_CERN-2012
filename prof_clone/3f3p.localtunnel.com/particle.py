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

class Circular(Particle):

    def move(self, dt):
        self.pos += self.vel * dt
        old_v = abs(self.vel)
        orthogonal = Vector2D(self.vel.y, -self.vel.x) * 0.1
        self.vel += orthogonal
        self.vel.normalize()
        self.vel *= old_v



class Universe(object):

    def __init__(self, width, height, DisplayType):
        self.particles = []
        self.width, self.height = width, height
        self.DisplayType = DisplayType

    def go(self):
        width, height = self.width, self.height
        del self.width, self.height
        self.display = self.DisplayType(width, height, self)
        
    def add_particle(self, p):
        self.particles.append(p)

    def evolve(self, dt, bounds):
        for particle in self.particles:
            particle.move(dt)
            particle.boundary_bounce(bounds)

    def draw(self, display):
        for p in self.particles:
            display.draw_circle(p.r, *p.pos)

if __name__ == "__main__":
    if sys.argv[1] == 'pyg':
        from PygletDisplay import PygletDisplay as Display
    if sys.argv[1] == 'tk':
        from TkinterDisplay import TkinterDisplay as Display

    width, height = 600,400
    u = Universe(600, 400, Display)
    u.add_particle(Particle(10, width/2, height/2, 100,  50))
    u.add_particle(Circular(20, width/4, height/2,  50, 100))
    u.add_particle(Particle(30, width/2, height/4,  75,  90))
    u.add_particle(Circular(25, width/2, height/2,  20, 110))
    u.add_particle(Particle(15, width/2, height/2, 140,   5))
    u.go()

