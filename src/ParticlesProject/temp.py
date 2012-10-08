class A(object):

    def meth(self, other):
        return other.viaA(self)
    
class B(object):

    def meth(self,other):
        return other.viaB(self)

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
