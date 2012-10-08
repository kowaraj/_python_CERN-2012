def one (*args, **kwds):
    return args, kwds

print one(**dict(a=2, b=4))

print one('hello')
print one(*'hello')


