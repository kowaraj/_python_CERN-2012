
# class Rect(object):
#     def __init__(self, w, h):
#         self.w = w
#         self.h = h

#     def get_a(self):
#         return self.h * self.w
#     def set_a(self, value):
#         self.h = value / self.w

#     a = property(get_a, set_a)
    
#     del get_a, set_a

class Rect(object):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    @property
    def a(self):
        return self.h * self.w

    @a.setter
    def set_a(self, value):
        self.h = value / self.w

