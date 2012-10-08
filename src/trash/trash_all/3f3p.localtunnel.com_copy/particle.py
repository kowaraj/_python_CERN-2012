import sys
from Vector import Vector2D
from math import sqrt

        
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
                
        ll = len(tuple(self.pos))
        chunked_bounds = chunk(ll, bounds)
        pos_i = xrange(ll)

        from operator import sub, add, lt, gt
        def do_bounce_i(i, d_max, d_min, fn_mod1, fn_mod2, fn_comp):
            if fn_comp(fn_mod1(self.pos[i], self.r), d_max):
                self.pos[i] = fn_mod2(d_max, self.r)
                self.vel[i] = -self.vel[i]

        for i, (d_min, d_max) in zip(pos_i, chunked_bounds):
            do_bounce_i(i, d_max, d_min, add, sub, gt)
            do_bounce_i(i, d_min, d_max, sub, add, lt)

        # for i, (d_min, d_max) in zip(pos_i, chunked_bounds):
        #     if self.pos[i] + self.r > d_max:
        #         self.pos[i] = d_max - self.r
        #         self.vel[i] = -self.vel[i]
        #     if self.pos[i] - self.r < d_min:
        #         self.pos[i] = d_min + self.r
        #         self.vel[i] = -self.vel[i]
                
        # x_min, x_max, y_min, y_max = bounds
        # chunked: [_min, _max], [_min, _max], ...
        
        # if self.pos.x + self.r > x_max:
        #     self.pos.x = x_max - self.r
        #     self.vel.x = -self.vel.x

class ParticleCM(Particle):

    def move(self, dt):
        ov = Vector2D(-self.vel.y/200, self.vel.x/200)
        vel_mag_old = sqrt(self.vel.x**2 + self.vel.y**2)
        
        self.pos += self.vel *dt
        
        self.vel += ov
        vel_mag_new = sqrt(self.vel.x**2 + self.vel.y**2)
        self.vel = self.vel*(vel_mag_old/vel_mag_new)

class ParticleAcc(Particle):

    def move(self, dt):
        print 'move_Acc'

        self.pos += self.vel*dt
        self.vel += self.vel*0.01

        vel_mag = sqrt(self.vel.x**2 + self.vel.y**2)            
        if vel_mag > 300:
            self.__class__ = ParticleDec
        
class ParticleDec(Particle):

    def move(self, dt):
        print 'move_Dec'
        
        self.pos += self.vel*dt
        self.vel += self.vel*(-0.01)
            
        vel_mag = sqrt(self.vel.x**2 + self.vel.y**2)            
        if vel_mag < 100:
            self.__class__ = ParticleAcc


class Universe(object):

    def __init__(self, width, height, DisplayType):
        self.particles = [ParticleAcc(10, width/2, height/2, 100,  50) #,
                          # Particle(20, width/4, height/2,  50, 100),
                          # Particle(30, width/2, height/4,  75,  90),
                          # Particle(25, width/2, height/2,  20, 110),
                          # Particle(15, width/2, height/2, 140,   5),
                          ]
        self.display = DisplayType(width, height, self)

    def evolve(self, dt, bounds):
        for particle in self.particles:
            particle.move(dt)
            particle.boundary_bounce(bounds)

    def draw(self, display):
        for p in self.particles:
            display.draw_circle(p.r, *p.pos)

if len(sys.argv) == 1:
    from TkinterDisplay import TkinterDisplay as Display
else:
    if sys.argv[1] == 'pyg':
        from PygletDisplay import PygletDisplay as Display
    if sys.argv[1] == 'tk':
        from TkinterDisplay import TkinterDisplay as Display


Universe(600, 400, Display)

