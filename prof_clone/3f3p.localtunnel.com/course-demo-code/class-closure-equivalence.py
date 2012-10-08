def make_adder(a):
    def adder(b):
        return a+b
    return adder

add1 = make_adder(1)
add2 = make_adder(2)
assert (add1(1), add2(1)) == (2,3)

class MakeAdder(object):
    def __init__(self, a):
        self.a = a
    def __call__(self, b):
        return self.a + b

add1 = MakeAdder(1)
add2 = MakeAdder(2)
assert (add1(1), add2(1)) == (2,3)
