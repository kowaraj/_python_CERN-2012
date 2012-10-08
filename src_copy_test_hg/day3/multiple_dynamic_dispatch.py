#for VisitorPatter: methods
class A(object):
    def meth(self, other):
        return other.viaA(self)
    
class B(object):
    def meth(self,other):
        return other.viaB(self)

#for VisitorPatter: operations
class Alpha(object):
    def viaA(self, other):
        return "A-Alpha"
    def viaB(self, other):
        return "B-Alpha"

class Beta(object):
    def viaA(self, other):
        return "A-Beta"
    def viaB(self, other):
        return "B-Beta"


a, b, al, be = A(), B(), Alpha(), Beta()

print a.meth(al)
print a.meth(be)
print b.meth(al)
print b.meth(be)


# HOMEWORK: rock-paper-scissor with this

# much simple with the decorators!
