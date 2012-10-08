def make_state_broken(n):
    def get():
        return n

    def set(new_n):
        n = new_n

    return get, set

g,s = make_state_broken('old')
print g()  # 'old'
s('new')
print g()  # still 'old' !

def make_state_fixed(m):
    n = [m]

    def get():
        return n[0]

    def set(new_n):
        n[0] = new_n

    return get, set

g,s = make_state_fixed('old')
print g()  # 'old'
s('new')
print g()  # 'new'
