def foo(n):
    return [          (lambda : i)     for i in xrange(n)]
    return [(lambda x:(lambda : x))(i) for i in xrange(n)]
        
def xfoo(n):
    r = []
    for i in xrange(n):
        def closure():
            return i
        r.append(closure)
    return r


for fn in xfoo(5):
    print fn()

print 'done'
