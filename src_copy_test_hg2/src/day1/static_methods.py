class C(object):

      def normal(*args):
      	  return args

      @staticmethod
      def static(*args):
          return args

      #alternative way to specify static
      def static2(*args):
          return args
      static2 = staticmethod(static2)

      @classmethod
      def class_(*args):
          return args


print C().normal()
# print C.normal() --> TypeError: unbound method normal() mu
print C().static()
print C.static()

print C.class_()

#m = C.normal
#m(C())
#mm = C().normal
#mm()
