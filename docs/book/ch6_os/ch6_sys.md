---
title: Sys
---

# sys

The sys module provides an access point to the Python environment, like path settings, the standard input, output and error stream, etc. 

``` python
import sys
# Version of the Python interpreter:
print(sys.version)
# Directories in which Python looks for modules:
print(sys.path)
print ('\n'.join(sys.path))
# Exit Python altogether:
sys.exit()
```


like most normal programming language, python have stdout (whenever we use print()), stdin ( whenever input() is used, it comes from stdin), and stderr (when ever Exceptions occur), which are accessible via sys.stdout, sys.stdin, and sys.stderr.  These variables are very useful for debugging and discuss more in logging part. 



``` python
import sys

def test(outfile,errfile):
        sys.stdout = open(outfile,"w")
        sys.stderr = open(errfile,"w")
        print(str(2) + " " + "Hello")
        print(2 + " " + "Hello")
        return()

test('stdout.file','error.log')
```


Now let run the function from terminal,  create a file entilte  filetes.py and run it 
```
python3 filetes.py
```

### sys.argv

To pass the name of outfile and errfile to file, creat a file filetes2.py
and paste the following code. 

``` python
import sys

def test(outfile,errfile):
        sys.stdout = open(outfile,"w")
        sys.stderr = open(errfile,"w")
        print(str(2) + " " + "Hello")
        print(2 + " " + "Hello")
        return()

test(sys.argv[1],sys.argv[2])
print(f'name of file is {sys.argv[0]}')
print(f'first parameter is {sys.argv[1]}')
print(f'second parameter is {sys.argv[1]}')
```
```
python3 test.py stdout3.file error3.log
```
This example show how pass the parameters to code. 







