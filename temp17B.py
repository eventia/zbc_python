#import sys
from sys import argv, path

print('The command line arguments are:')
#for i in sys.argv:
for i in argv:
    print(i)

print('\n\nPATH is')
#for i in sys.path:
for i in path:
    print(i)
