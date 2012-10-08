import os
import sys
 
# update python interpreter sys.path with a current directory

def go():
    cur_path_to_add = os.getcwd()
    print 'cwd = ', cur_path_to_add 
    sys.path.append(cur_path_to_add)
