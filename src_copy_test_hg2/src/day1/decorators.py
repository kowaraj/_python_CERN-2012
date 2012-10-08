def one(_):
    return 1

#def hello():
#    print "hi"
#hello = one(hello)
#
#=> same as:
@one
def hello():
    print "hi"

print hello


def inc(n):
    return n+1


@inc
@inc
@one
def hello():
    print "hi"

print hello


def inc_by(n):
    def inc(m):
        return n+m
    return inc

@inc_by(10)
@inc
@inc
@one
def hello():
    print "hi"
print hello



def report_args(the_func_to_be_decorated):
    def the_enhanced_function(*args, **kwds):
        print args, kwds
        return the_func_to_be_decorated(*args, **kwds)
    return the_enhanced_function

def report_result(the_func_to_be_decorated):
    def the_enhanced_function(*args, **kwds):
        res = the_func_to_be_decorated(*args, **kwds)
        print 'decorated by report_result: {0}'.format(res)
        return res
    return the_enhanced_function

@report_args
def my_add(a,b):
    return a+b


@report_result
def my_add2(a,b):
    return a+b

def increment_result_by(increment_k):
    def the_enhanced_function(the_func_to_be_decorated):
        def f2(*args, **kwds):
            return the_func_to_be_decorated(*args, **kwds) + increment_k
        return f2
    return the_enhanced_function

@increment_result_by(10)
def my_add3(a,b):
    return a+b
# my_add = increment_result_by(10)(my_add)


@increment_result_by(5)
def my_mul(a,b):
    return a+b

def my_add_10(x,y):
    return my_mul(x,y) + 10

my_add3(1,2)
my_add3(4,2)
my_mul(1,2)
my_mul(10,3)












#my_add3 = increment_result_by(10)(my_add3)

