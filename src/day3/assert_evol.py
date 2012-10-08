
def assert_evolution(v, f):

    def assert_inv():
	prev_val = v()
	while True:
	    yield
	    new_val = v()
	    assert f(new_val, prev_val)
            print 'a.ok!'
	    prev_val = new_val

    gen = assert_inv()
    return gen.next

############################################################
# print '================> test'
# assert_invariant = assert_evolution(lambda:x, eq)
# x = 1
# assert_invariant()
# assert_invariant()
# x = 3
# assert_invariant()
############################################################
