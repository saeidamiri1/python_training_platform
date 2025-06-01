import sys

def test(outfile,errfile):
        sys.stdout = open(outfile,"w")
        sys.stderr = open(errfile,"w")
        print(str(2) + " " + "Hello")
        print(2 + " " + "Hello")
        return()

test('stdout.file','error.log')
