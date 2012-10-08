# a decorator

#================================================================== v.0.1
# def multimethod(type1, type2):
#     print 'multimethod for types: ', type1, type2
#     def f_decorator(f):
#         if type1 is Rock and type2 is Paper:
#             print 'f_decorator: rock-vs-paper'
#             def decorated_f(*args):
#                 print 'called: decorated_f of rock-vs-paper'
#                 return 'right'
#             return decorated_f
#         elif type1 is Paper and type2 is Rock:
#             print 'f_decorator: paper-vs-rock'
#             def decorated_f(*args):
#                 print 'called: decorated_f of paper-vs-rock'
#                 return 'left'
#             return decorated_f
#         else:
#             print 'f_decorator: unknown-combination'
#             def decorated_f(*args):
#                 print 'called: decorated_f of unknown'
#                 return 'decorated_f: unknown'
#             return decorated_f
#     return f_decorator
    
#================================================================== v.0.2

def multimethod(type1, type2):
    print 'multimethod for types: ', type1, type2
    def f_decorator(f):

            # print 'f_decorator: types = ', (type1, type2)
            # print 'f_decorator: cache = ', cache
            # print 'f_decorator: f = ', f
            multimethod.cache[(type1, type2)] = f
            # print 'f_decorator: cache = ', cache
            
            def decorated_f(*args):
                # print 'decorated_f: args = ', args
                types_tuple = (type(args[0]), type(args[1]))
                # print 'decorated_f: types_tuple = ', types_tuple

                if types_tuple not in cache:
                    raise RuntimeError
                
                f_ret = cache[types_tuple]
                print 'decorated_f: f_ret = ', f_ret
                return f_ret(*args)
            
 
            return decorated_f
    return f_decorator
multimethod.cache = {}


class Rock(object):     pass
class Paper(object):    pass
class Scissors(object): pass

print ''
print '===================================================< begin'
print '===> create the multimethod(Rock, Paper) '
@multimethod(Rock, Paper)
def winner(l,r): return 'right'
#winner = multimethod(Rock, Paper)(winner)

print '===> create the multimethod(Paper, Rock) '
@multimethod(Paper, Rock)
def winner(l,r): return 'left'
#winner = multimethod(Paper, Rock)(winner)


rock, paper, scissors = Rock(), Paper(), Scissors()

print ''
print '===================================< tests'
print '====== call for winner(rock, paper)'
print winner(rock, paper)
print '====== call for winner(rock, paper)'
print winner(paper, rock)

print '====== tests ========='
assert winner(rock, paper) == 'right'
assert winner(paper, rock) == 'left'
print 'ok!'
