---
title: Error Handling
---


# Error Handling
The `try.. except` statement allows your program to catch and handle errors instead of terminating unexpectedly.  To manage errors gracefully, you can use `try ... except`, its basic structure is as follows:

## simple Exception 
``` py
try:
   operations;
except ExceptionI:
   If there is ExceptionI, then execute this block.
except ExceptionII:
   If there is ExceptionII, then execute this block.
   ...
else:
   If there is no exception then execute this block. this part arbitary and can be dropt.  
finally: 
   This block always runs.
```

The following show how to use `sys` function to find out what error happen, let try a simple mathemtic operation and see what error might happen.    

``` py
import sys
list_n = ['a',0, 3]
for entry in list_n:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
    except:
        print("Oops!", sys.exc_info()[0], "occurred.")
        print("Next entry.")
```

You see two error  'ValueError' and 'ZeroDivisionError'....



## assert
The assert statement is useful for debugging, as it tests a condition in your code.  If the condition is not True, the program raises an AssertionError.

``` py
while True:
        num = int(input("Enter a number: "))
        assert num % 2 == 0 , "Not an Even number" 
        reciprocal = 1/num
        print(reciprocal)
```

``` py
while True:
    try:
        num = int(input("Enter a number: "))
        assert num % 2 == 0 , "An even number"
    except:
        print("Not an even number!")
        break
    else:
        reciprocal = 1/num
        print(reciprocal)
```

## Exception configuration
User can set up and control how exceptions determining what happens when an error occurs, how it is reported. 

### Exception class
We can detect error withous using `sys`. Since every exception in Python inherits from the base Exception class, we can achieve the same result using the following approach:

``` py
import sys
list_n = ['a',0, 3]
for entry in list_n:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
    except Exception as e:
        print("Oops!", e.__class__, "occurred.")
        print("Next entry.")
```


Try the following which show you can handle the error inside the `try`. Run the following code with -1, 1, 'a'. 

``` py
try:
     a = int(input("Enter a positive integer: "))
     if a <= 0:
         raise ValueError("That is not a positive number!")
except Exception as ve:
     print(ve)
```


### IndexError
This error occurs when you try to assign a value to an index that is beyond the valid range of indices in the list.

``` py
tournaments = ["NAGA", "IBJJF", "EBI"]
while True:
    try:
        tournament = tournaments.pop()
        print(f"I would like to compete in the {tournament} tournament.")
    except IndexError:
        print("There are no more tournaments")
        break
```

### Raise
You can define your own types of Exception types:

```python
i_num = int(input("Enter a number: "))
if i_num < number:
    raise RuntimeError(f'{i_num} is small')
```

You can use raise with try to handle exceptions. Let's consider defining a function that raises an error if the input number is less than or greater than zero. First, define the base class to propagate the error:

``` py
class Error(Exception):
    """Base class for other exceptions"""
    pass
```

Then, specify the errors and pass the exception to them.

``` py
class ErrorTooSmall(Error):
    """Raised when the input value is too small"""
    pass

class ErrorTooLarge(Error):
    """Raised when the input value is too large"""
    pass
```

Now, run the following to 

``` py
number = 10

while True:
    try:
        i_num = int(input("Enter a number: "))
        if i_num < number:
            raise ErrorTooSmall
        elif i_num > number:
            raise ErrorTooLarge
        print("Congratulations! You guessed it correctly.")
        break
    except ErrorTooSmall:
        print("This value is too small, try again!")
        print()
    except ErrorTooLarge:
        print("This value is too large, try again!")
        print()
```

### Catching Multiple Errors
You can catch different types of exceptions by using multiple `except` blocks.

```python
try:
  ...
except LookupError as e:
  ...
except RuntimeError as e:
  ...
except IOError as e:
  ...
except KeyboardInterrupt as e:
  ...
```

Alternatively, if the handling statements are the same, you can group the exceptions together:

```python
try:
  ...
except (IOError,LookupError,RuntimeError) as e:
  ...
```

### Catching All Errors

To catch any exception, use `Exception` like this:

```python
try:
    ...
except Exception:       # DANGER. See below
    print('An error occurred')
```


### IOError
The following code shows how to handle the recognized IOError in your code.

``` py
#!/usr/bin/python

try:
   fh = open("testfile", "w")
   fh.write("This is my test file for exception handling!!")
except IOError:
   print "Error: can\'t find file or read data"
else:
   print "Written content in the file successfully"
   fh.close()
```

