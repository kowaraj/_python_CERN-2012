def fubar(a,x=[]):
    x.append(a)
    return x

print fubar(1)
print fubar(2)

def foo(a,x=None):
    if x is None:
        x = []
    x.append(a)
    return x

print foo(1)
print foo(2)
