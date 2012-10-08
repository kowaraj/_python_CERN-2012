import sys

class Particle(object):

    def __init__(self, r,  x,y, vx, vy):
        self.r = r
        self.x,  self.y  =  x,  y
        self.vx, self.vy = vx, vy

    def move(self, dt, bounds):
        
        x_min, x_max, y_min, y_max = bounds

        self.x += self.vx * dt
        self.y += self.vy * dt

        if self.x + self.r > x_max:
            self.x = x_max - self.r
            self.vx = -self.vx

        if self.x - 30 < x_min:
            self.x = x_min + self.r
            self.vx = -self.vx

        if self.y + self.r > y_max:
            self.y = y_max - self.r
            self.vy = -self.vy

        if self.y - 30 < y_min:
            self.y = y_min + self.r
            self.vy = -self.vy


if sys.argv[1] == 'pyg':

    import pyglet

    from math import sin, cos, pi, sqrt
    twopi = 2*pi

    window = pyglet.window.Window(600,400)
    fps_display = pyglet.clock.ClockDisplay()

    x,y = window.width / 2, window.height / 2
    vx, vy = 80.0, 150.0

    radius = 30
    particle = Particle(radius, x,y,  vx,vy)

    @window.event
    def on_draw():
        window.clear()
        def circle_vertices():
            delta_angle = twopi / 20
            angle = 0
            while angle < twopi:
                yield particle.x + 30 * cos(angle)
                yield particle.y + 30 * sin(angle)
                angle += delta_angle

        pyglet.gl.glColor3f(1.0, 1.0, 0)
        vertex_order = range(20)
        pyglet.graphics.draw(20, pyglet.gl.GL_LINE_LOOP,
                             ('v2f', tuple(circle_vertices())))

        fps_display.draw()


    def update(dt):
        global particle
        particle.move(dt, (0, window.width, 0, window.height))

    pyglet.clock.schedule_interval(update, 1/60.0)

    pyglet.app.run()

################################################################################

if sys.argv[1] == 'tk':
    import Tkinter as tk

    master = tk.Tk()

    diameter = 60

    w = tk.Canvas(master, width=600, height=400, bg='black')
    w.pack()

    x,y = w.winfo_height() / 2, w.winfo_width() / 2
    vx, vy = 80.0, 150.0

    particle = Particle(diameter/2, x+diameter/2,y+diameter/2, vx,vy)
    oval = w.create_oval(x,y, diameter,diameter, outline='yellow')

    def update(dt):
        global particle
        oldx, oldy = particle.x, particle.y
        particle.move(dt, (0, w.winfo_width(), 0, w.winfo_height()))
        w.move(oval, particle.x-oldx, particle.y-oldy)
        w.update()
        w.after(17, update, 1/60.0)

    update(0)

    tk.mainloop()


