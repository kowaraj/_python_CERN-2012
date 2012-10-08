def xfoo(n):
    r = []
    for i in xrange(n):
    	def hmm():
	    return i 
        r.append(hmm())
    return r

for fn in xfoo(5):
    print fn


def xfoo(n):
    r = []
    for i in xrange(n):
    	def hmm(i):
	    return i 
        r.append(hmm(i))
    return r

for fn in xfoo(5):
    print fn
    



print '===> lambda version'

def foo2(n):
    return [           (lambda : x)     for i in xrange(n)]
    return [(lambda x: (lambda : x))(i) for i in xrange(n)]

def xfoo2(n):
    r = []
    print 'xfoo2'
    for i in xrange(n):
        print 'in range'
        def hmm(i):
            print 'in hmm'
            def closure():
                return i
            r.append(closure)
            return 
    return r

for fn in xfoo2(5):
    print fn
    print fn()
    
