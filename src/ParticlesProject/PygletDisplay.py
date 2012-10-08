import pyglet
from math import sin, cos, pi
twopi = 2*pi

class PygletDisplay(object):

    def __init__(self, width, height, universe):
        self.universe = universe
        self.window = pyglet.window.Window(width, height)
        self.fps_display = pyglet.clock.ClockDisplay()
        self.window.event(self.on_draw)
        pyglet.clock.schedule_interval(self.update, 1/60.0)
        pyglet.app.run()

    def update(self, dt):
        self.universe.evolve(dt, self.bounds)

    #@window.event
    def on_draw(self):
        self.window.clear()
        self.universe.draw(self)
        self.fps_display.draw()

    def draw_circle(self, radius, x, y, colour = (1.0, 1.0, 0)):
        def circle_vertices():
            delta_angle = twopi / 20
            angle = 0
            while angle < twopi:
                yield x + radius * cos(angle)
                yield y + radius * sin(angle)
                angle += delta_angle

        pyglet.gl.glColor3f(colour)
        vertex_order = range(20)
        pyglet.graphics.draw(20, pyglet.gl.GL_LINE_LOOP,
                             ('v2f', tuple(circle_vertices())))

    @property
    def bounds(self):
        return (0, self.window.width,   0, self.window.height)
