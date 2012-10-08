def gen_func(n, d):
    while True:
        yield n
        n+=d




class gen_class:

    def __init__(self):
        self.i = 0

    def next(self):
        if self.i < 3:
            self.i +=1
            return self.i
        else:
            raise StopIteration

    def __iter__(self):
        return self
    

f = gen_func(3, 10)
assert f.next() == 3
assert f.next() == 13
assert f.next() == 23
assert f.next() == 33
assert f.next() == 43



