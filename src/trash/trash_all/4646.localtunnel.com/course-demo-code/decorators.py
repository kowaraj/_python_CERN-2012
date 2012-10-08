from functools import wraps

def increment_result_by(n):
    def decorator(function_being_decorated):
        @wraps(function_being_decorated)
        def enhanced_function(*args, **kwds):
            result = function_being_decorated(*args, **kwds)
            return result + n
        return enhanced_function
    return decorator

def report_args(the_function_being_decorated):
    @wraps(the_function_being_decorated)
    def the_enhanced_function(*args, **kwds):
        print 'args', args, kwds
        return the_function_being_decorated(*args, **kwds)
    return the_enhanced_function

def report_result(the_function_being_decorated):
    @wraps(the_function_being_decorated)
    def the_enhanced_function(*args, **kwds):
        result = the_function_being_decorated(*args, **kwds)
        print 'result', result
        return result
    return the_enhanced_function

@increment_result_by(10)
@report_result
@report_args
def my_add(a,b):
    return a+b



def one(_):
    return 1

def inc(n):
    return n+1

def inc_by(n):
    def inc(m):
        return n+m
    return inc

@inc_by(10)
@inc
@inc
@inc
@one
def hello():
    print "hi"
print hello
