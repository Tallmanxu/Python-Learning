class ShortInputException(Exception):
    def __init__(self,length,atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast

def have_a_try():
    try:
        s=raw_input('Enter sth-->')
        if len(s) < 3:
            raise ShortInputException(len(s),3)
    except EOFError:
        print '\nWhy did you do an EOF on me ?'
    except ShortInputException,x:
        print 'ShortInputException: The input was of length %d, was expecting at least %d'%(x.length,x.atleast)
    else:
        print 'No exception was raised.'
    finally:
        print 'clean up.'

def exec_eval():
    exec 'print "hello world!"'
    a = eval("2*3")
    print a

    assert a < 5 ,'what the fuck'


#exec_eval()

import json

data = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]

#a = json.encode(data)

a = json.dumps(data)


print a











