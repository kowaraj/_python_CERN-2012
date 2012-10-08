def shifter():
    return 1

def make_adder(a1):
    a = a1+shifter()
    print 'a= {0}'.format(a)
    def adder(b): 
        return a + b
    return adder

def shifter():
    return 2

add3 = make_adder(3)
add4 = make_adder(4)

def shifter():
    return 3

print add3(10)
print add4(10)

