def func2():
    '''''this is func1'''
    print "this is func2"

print func2.__doc__

def foo():
    '''
        Here the document.
    '''
    print 'Hello world!'

print foo.__doc__


def hi():
    '''
        What the fuck!
    '''

print hi.__doc__


import sys
import using_name
print 'the command line arguments are: '
for i in sys.argv:
    print i

print '\n\nThe pythonpath is ',sys.path,'\n'




