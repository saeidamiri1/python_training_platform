---
title: SYS
---

# sys

The `sys` module provides an interface to the Python runtime environment, allowing access to interpreter variables such as the module search path (`sys.path`), standard input/output/error streams (`sys.stdin`, `sys.stdout`, `sys.stderr`), and functions for exiting the interpreter (`sys.exit()`), among others.
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

The standard input, output, and error streams (sys.stdin, sys.stdout, and sys.stderr) are particularly useful for debugging and are discussed further in the logging section.
To test stdout and stderr, run the following function, then open the files stdout.file and error.log, which capture the standard output and error streams, respectively.
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

To test the function via the terminal, create a file named test.py and run it.
```
$ python3 test.py
$ cat stdout.file
2 Hello
$ cat error.log  
Traceback (most recent call last):
  File "~/test.py", line 10, in <module>
    test('stdout.file','error.log')
  File "~/test.py", line 7, in test
    print(2 + " " + "Hello")
          ~~^~~~~
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

### sys.argv
To pass the names of the output and error files to the script, create a file named test2.py and paste the following code into it.

``` python
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
```


Run the following command to pass the names of the standard output and error files to the script.

```
python3 test.py stdout2.file error2.log
```
