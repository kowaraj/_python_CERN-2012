class Happy(object):

    def comment(self):
        print "I'm so happy"

    def sing(self):
        print "Yippeeee !"

    def change(self):
        self.__class__ = Sad

class Sad(object):
    
    def comment(self):
        print "Oh noooooo"

    def sing(self):
        print "I don't want to sing, I'm too depressed"

    def change(self):
        self.__class__ = Happy

me = Happy()
me.comment()
me.sing()
me.change()
me.comment()
me.sing()
