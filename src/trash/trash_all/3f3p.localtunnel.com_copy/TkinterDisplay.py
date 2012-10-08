import Tkinter as tk

class TkinterDisplay(object):

    def __init__(self, width, height, universe):
        master = tk.Tk()
        self.universe = universe
        self.w = tk.Canvas(master, width=width, height=height, bg='black')
        self.w.pack()
        self.w.after(500, self.update, 1/60.0)
        tk.mainloop()

    def update(self, dt):
        # Clear old ovals
        self.w.delete(tk.ALL)
        self.universe.evolve(dt, self.bounds)
        self.universe.draw(self)

        self.w.update()
        self.w.after(17, self.update, 1/60.0)

    def draw_circle(self, radius, x, y):
        height = self.w.winfo_height()
        self.w.create_oval(x-radius, height-(y-radius),
                           x+radius, height-(y+radius), outline='yellow')

    @property
    def bounds(self):
        return (0, self.w.winfo_width(),   0, self.w.winfo_height())

