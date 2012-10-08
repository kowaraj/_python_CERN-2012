def make_state(n):

    def get():
        return n 

    def set(new_n):
        #nonlocal n 
        n = new_n

    return get, set

g, s = make_state('old')
print g() # 'old'
s('new')
print g() # still 'old'


#trick in python2

def make_state_tricky(m):
    n = [m]
    def get():
        return n[0] 

    def set(new_n):
        n[0] = new_n

    return get, set

g, s = make_state_tricky('old')
print g() # 'old'
s('new')
print g() # still 'old'


