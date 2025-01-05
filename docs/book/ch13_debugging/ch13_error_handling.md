
# Error Handling

The `try.. except` statement allows your program to catch errors and act on them instead of terminating the program. To handle error in your code in a way to catch errors and act on them instead of terminating the program. you can use `try ... except` in your code which introduced in ..., 
its structure is as below






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
The assert is very useful for debugging to test a condition in your code, if condition not TRUE, the program will raise an AssertionError.

``` py
while True:
        num = int(input("Enter a number: "))
        assert num % 2 == 0 , "Not an Even numebr" 
        reciprocal = 1/num
        print(reciprocal)
```

``` py
while True:
    try:
        num = int(input("Enter a number: "))
        assert num % 2 == 0 , "BBB"
    except:
        print("Not an even number!")
        break
    else:
        reciprocal = 1/num
        print(reciprocal)
```

## Exception configuration


### Exception class
We can find error withous using `sys`. Since every exception in Python inherits from the base Exception class, we can also perform the above task in the following way:

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
This error happen when you assign a value to an index that is
 beyond the valid range of indices in the list.

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
You can define your own types of Exceptions:

```python
i_num = int(input("Enter a number: "))
if i_num < number:
    raise RuntimeError(f'{i_num} is small')
```

You can use raise with try. let consider define function to give error if the input number is less or greater than zero: first define the base class to transfer the erro

``` py
class Error(Exception):
    """Base class for other exceptions"""
    pass
```

Then specift the errors and pass the eroor to them 

``` py
class ErrorTooSmall(Error):
    """Raised when the input value is too small"""
    pass

class ErrorTooLarge(Error):
    """Raised when the input value is too large"""
    pass
```

Now run the following to 
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

You can catch different kinds of exceptions using multiple `except` blocks.

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

Alternatively, if the statements to handle them is the same, you can group them:

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
The following code shows how to handle the recognise IOError  in code. 

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



## Challenge

class SalaryNotInRangeError(Exception):
    """Exception raised for errors in the input salary.
    Attributes:
        salary -- input salary which caused the error
        message -- explanation of the error
    """
    def __init__(self, salary, message="Salary is not in (5000, 15000) range"):
        self.salary = salary
        self.message = message
        super().__init__(self.message)
    def __str__(self):
        return f'{self.salary} -> {self.message}'


salary = int(input("Enter salary amount: "))
if not 5000 < salary < 15000:
    raise SalaryNotInRangeError(salary)


