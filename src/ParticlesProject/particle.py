import sys
from Vector import Vector2D
from math import sqrt
from time import time

class ParticleColour(object):

    @staticmethod
    def rgb01(r, g, b):
        c = ParticleColour()
        c.rgb_components = (r,g,b)
        return c

    @staticmethod
    def rgb255(r255, g255, b255):
        c = ParticleColour()
        c.rgb_components = (r255/10, g255/10, b255/10)
        return c

    @property
    def as_rgb01(self):
        return self.rgb_components


    @property
    def as_rgb255(self):
        (r, g, b) = self.rgb_components
        return (r*10, g*10, b*10)

    @property
    def as_name (self):
        r = 'unknown'
        if self.rgb_components == (3.0, 2.0, 1.0):
            r = 'white'
        elif self.rgb_components == (1.0, 2.0, 3.0):
            r = 'red'
        return r

    def switch(self):
        if self.rgb_components == (3.0, 2.0, 1.0):
            self.rgb_components = (1.0, 2.0, 3.0)
        elif self.rgb_components == (1.0, 2.0, 3.0):
            self.rgb_components = (3.0, 2.0, 1.0)
           
class Particle(object):

    def __init__(self, r,  x,y, vx, vy, colour):
        self.r = r
        self.pos = Vector2D( x, y)
        self.vel = Vector2D(vx,vy)
        self.colour = colour

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
        # print 'move_Acc'

        self.pos += self.vel*dt
        self.vel += self.vel*0.01

        vel_mag = sqrt(self.vel.x**2 + self.vel.y**2)            
        if vel_mag > 300:
            self.colour.switch() 
            self.__class__ = ParticleDec
        
class ParticleDec(Particle):

    def move(self, dt):
        # print 'move_Dec'
        
        self.pos += self.vel*dt
        self.vel += self.vel*(-0.01)
            
        vel_mag = sqrt(self.vel.x**2 + self.vel.y**2)            
        if vel_mag < 100:
            self.colour.switch() 
            self.__class__ = ParticleAcc


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
        # t1 = time()
        for particle in self.particles:
            particle.move(dt)
            particle.boundary_bounce(bounds)
        # t2 = time()
        # print 'fps = ', 1/(t2 - t1)

    def draw(self, display):
        for p in self.particles:
            display.draw_circle(p.r, p.colour, *p.pos)

if len(sys.argv) == 1:
    from TkinterDisplay import TkinterDisplay as Display
else:
    if sys.argv[1] == 'pyg':
        from PygletDisplay import PygletDisplay as Display
    if sys.argv[1] == 'tk':
        from TkinterDisplay import TkinterDisplay as Display


u = Universe(600, 400, Display)
pc1 = ParticleColour.rgb01(3.0, 2.0, 1.0)
pc2 = ParticleColour.rgb01(1.0, 2.0, 3.0)

for i in range(300):
    u.add_particle(ParticleAcc(10+i*10, 100, 100, 100+i*10,  50, pc1))
    u.add_particle(ParticleDec(10+i*20, 200, 200, 100+i*20,  50, pc2))

# Particle(20, width/4, height/2,  50, 100),
# Particle(30, width/2, height/4,  75,  90),
# Particle(25, width/2, height/2,  20, 110),
# Particle(15, width/2, height/2, 140,   5),

u.go()

