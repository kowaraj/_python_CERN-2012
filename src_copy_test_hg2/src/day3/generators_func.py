def xxrange():
    v = 0
    step = 1
    while True:
        try: 
            new_step = yield(v)
            print 'gen: type of yield retval = ', type(new_step)
            if type(new_step) is int:
                step = new_step
            v += step
        except RuntimeError:
            print 'exception!'
            


f = xxrange()
print f.next()
print f.next()
print f.next()
print f.next()

print f.send(3)
print f.next()
print f.next()
print f.next()
print f.next()

print f.send(RuntimeError())
print f.next()

print f.throw(RuntimeError())
print f.next()
print f.next()
print f.next()
print f.next()
print f.next()
