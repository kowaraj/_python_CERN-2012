###########
f = open('~/temp.txt', 'r')
try:
      print f.getline()
      #lots of code here
finally:
      f.close()


############ context manager: with + open
with open('~/temp.txt', 'r') as f:
      print f.getline()
      #lots of code here

      
