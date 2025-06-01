import sys

def test(outfile,errfile):
        sys.stdout = open(outfile,"w")
        sys.stderr = open(errfile,"w")
        print(str(2) + " " + "Hello")
        print(2 + " " + "Hello")
        return()
# we pass the name of std and error file here
test(sys.argv[1],sys.argv[2])
print(f'name of file is {sys.argv[0]}')
print(f'first parameter is {sys.argv[1]}')
print(f'second parameter is {sys.argv[1]}')
