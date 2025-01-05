---
title: Scope and namespace
---

# Scope and namespace 
## Scope
Variables are containers for storing data values. The scope of a variable refers to the region in the code where the variable is accessible. Generally, there are three types of scopes: Global, Local, and Nonlocal. Let's explore these concepts in detail.

``` python
#primer.py
# Global scope
VAR1="OUT SIDE"
def f():
    # Local Scope
    VAR2="IN SIDE"
    print(VAR1)
    print(VAR2)
    print(VAR3)
    def f_sub():
        # NonLocal Scope
        VAR3="IN IN SIDE"
        print(VAR1)
        print(VAR2)
        print(VAR3)
    f_sub()

f()
VAR1
VAR2
VAR3
```


Running this function results in an error because VAR1 is defined in the global scope and is accessible throughout the module. However, VAR2 is defined in the local scope of the function and is accessible only within that function. Similarly, VAR3, which is defined within a nested function, is accessible only within the nonlocal scope. To fix the issue, we need to adjust the function accordingly. Once corrected, rerunning the function should resolve the errors.


``` python
def f():
    # Local Scope
    VAR2="IN SIDE"
    print(VAR1)
    print(VAR2)
    def f_sub():
    # NonLocal Scope
        VAR3="IN IN SIDE"
        print(VAR1)
        print(VAR2)
        print(VAR3)
    f_sub()

f()
VAR1
VAR2
VAR3
```

In Python, variables can be categorized into three types based on their scope: local, nonlocal, and global, each serving a distinct purpose. To view the variables in Python's global scope, you can use the dir() function without any arguments. This will display a list of all names available in your current environment.

### Local variables
A local variable is one that is defined within a specific function and is accessible only within that function. It cannot be accessed from outside the function. Here's an example where we define a variable inside a function and then try to access it from outside:

``` python
#primer.py
# Global scope
def f():
    # Local scope
    # local variable
    VAR="IN SIDE"
    print(VAR)

f()
VAR
```

The code execution is shown below. As demonstrated, although the variable is defined within the function, it cannot be accessed from the global scope.

``` bash
>>> def f():
...     # local variable
...     VAR="IN SIDE"
...     print(VAR)
... 
>>> f()
IN SIDE
>>> VAR
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'VAR' is not defined
```

To view the local variables, use the locals().keys() function. This returns a dictionary containing all the local variables within the current scope.


``` python
def f():
    # Local scope
    # local variable
    VAR="IN SIDE"
    print(VAR)
    print(locals().keys())
```


### Global variable
Unlike a local variable, a global variable is defined outside of any function but can still be accessed from within functions. Global variables are often used to store data that needs to be shared across multiple functions, both inside and outside.

To declare a global variable in Python, use the global keyword followed by the variable name. If you have multiple global variables, separate their names with commas after the global keyword.

Let's run the following code:

``` python
def f():
    global VAR
    VAR="IN SIDE"
    print(VAR)

f()
VAR
```


The code execution is shown below. As you can see, even though the variable is defined inside the function, it cannot be accessed from the global scope.

``` bash
>>> def f():
...     global VAR
...     VAR="IN SIDE"
...     print(VAR)
... 
>>> f()
IN SIDE
>>> VAR
'IN SIDE'
```

Let define as globals. 

``` python
VAR="OUT SIDE"
def f():
    global VAR
    VAR="IN SIDE"
    print(VAR)

f()
VAR
```

Clearly, assigning the variable as a global variable changes its value.

``` bash
>>> VAR="OUT SIDE"
>>> def f():
...     global VAR
...     VAR="IN SIDE"
...     print(VAR)
... 
>>> f()
IN SIDE
>>> VAR
'IN SIDE'
```


``` python
VAR="OUT SIDE"
VAR
f()
VAR
```

``` bash
>>> VAR="OUT SIDE"
>>> VAR
'OUT SIDE'
>>> f()
IN SIDE
>>> VAR
'IN SIDE'
```

More specifically, when you start a program, you begin in the global scope. Python treats the main script of your program as a module named __main__ to manage the execution of the main program. To test this, run __name__:


``` bash
>>> __name__
'__main__'
```
This demonstrates that the name of the main module is __main__.

To view the global variables, run globals().keys(), which returns a dictionary representing the current global variables. At the global scope, both locals() and globals() return the same dictionary for the global namespace. In contrast, dir() returns a list of the current local variables.

### Nonlocal Variables
A nonlocal variable is defined inside a nested function. You can share this variable between the local and nonlocal scopes by using the nonlocal keyword followed by the variable name.

```python
def f():
    # Local Scope
    VAR="IN SIDE"
    # print(VAR2)
    # print(VAR3)
    def f_sub():
        # NonLocal Scope
        nonlocal VAR
        VAR = "IN IN SIDE"
        print("nonlocal scope:",VAR)
    f_sub()
    print("local scope:", VAR)

f()
VAR


def f():
    # Local Scope
    VAR="IN SIDE"
    # print(VAR2)
    # print(VAR3)
    def f_sub():
        # NonLocal Scope
        # nonlocal VAR
        VAR = "IN IN SIDE"
        print("nonlocal scope:",VAR)
    f_sub()
    print("local scope:", VAR)

f()
VAR

```


In the above example, the f_sub function modifies the value of the local variables. Now, let's explore the use of a nonlocal variable. To compute an average, we need both the sum and the count of numbers. The following code demonstrates how to use nonlocal variables to maintain and update the sum and count when new data is added.

``` python
def average():
     sum = 0
     count = 0
     def _average(input):
         nonlocal sum, count
         sum += input
         count += 1
         return sum / count
     return _average

ave=average()
ave(2)
ave(3)
```

## Namespace 
A namespace is a collection of names that map to values of variables and other objects within a program. In Python, these namespaces are stored as dictionaries and are often referred to as scopes. The most important namespace is the built-in namespace, which is created when the Python interpreter starts and remains available throughout the program's execution. This namespace includes built-in functions like print() and dir(), which are always accessible.

You can view the names available in the current Python scope using the following command:

``` python
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__']
```

Python also has a standard library module called builtins, which is automatically loaded into the built-in namespace when the interpreter starts. You can access the names of objects in the builtins namespace via __builtins__. Here's an example:

```python

>>> dir(__builtins__)
['ArithmeticError', 'AssertionError', ..., 'zip']

>>> len(dir(__builtins__))
158
```

Each module has its own global namespace, and similarly, each function has its own local namespace.
