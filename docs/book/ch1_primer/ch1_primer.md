---
title: Primer
---

# Python primer 
## Getting Started
### Library\module

A library or module is a collection of data, functions, and tools packaged for performing specific tasks. Python includes standard library modules, such as `re`, which are available by default when Python is installed. Since these libraries are pre-installed, their functions can be easily accessed in Python by importing the corresponding module.


```python
>>> import re
>>> re
<module 're' from '/opt/homebrew/Cellar/python@3.11/3.11.9/Frameworks/Python.framework/Versions/3.11/lib/python3.11/re/__init__.py'>
>>> 
```

Other modules come from third-party libraries, which can be installed using `pip`, Python's package management system. To install a library, simply type its name in the terminal following the pip install command, like this: `pip install library_name`.

```python
pip install numpy
import numpy
numpy
```
Third-party modules are typically stored in a dedicated `site-packages` directory. If the module is hosted on GitHub, you can easily install it by using `pip` with the module's repository URL.

```python
pip install git+https://github.com/mwaskom/seaborn.git
```

### comments
By putting `#` infront a line, Python ignores running them, or put ```'''`` a line befor and after text. 

By placing a `#` at the beginning of a line, Python treats it as a comment and ignores it during execution. Alternatively, you can use triple quotes (`'''` or `"""`) before and after a block of text to create multi-line comments or docstrings.
```
'''
It does not run
'''
```

### Working directory
The working directory is the folder that Python actively accesses to read or save files and interact with objects. This directory is referred to as the "working directory."

``` python
import os
os.getcwd()
```

To change the current working directory, use `os.chdir(path)`. To retrieve all files in the current directory as a list, use `os.listdir(os.getcwd())`.

### scalar
A single value is called a scalar. To store this value, you assign it a meaningful name, referred to as a variable. This is done using an assignment statement with the `=` operator. The following example assigns a numerical value and a string to two different variables:

```python
pi0=3.14
pi1='approximate with two digits'
```

The assignment can be done in a flexible manner,

```python
p=(4,3)
x, y=p

dat=[2,4, 4, (3,2,4)]
da1, dat2, dat3,d4=dat
d4
x=1
x+=2 # x=x+2
x*=2 # x=x*1
x**=2 # x=x**2
```

A variable name can contain both letters and numbers, but it must not begin with a number. It's important to use meaningful names for your variables. The value assigned to a variable can be of various basic built-in types, such as integer, float, string, and boolean. A boolean represents a logical value, typically either `True` or `False`.

```python
>>> x1=1
>>> x2=2.0
>>> x3='3'
>>> x4=True
>>> type(x1)
<class 'int'>
>>> type(x2)
<class 'float'>
>>> type(x3)
<class 'str'>
>>> type(x4)
<class 'bool'>
```

## Data Structures
Python provides a variety of useful data structures, such as lists, sets, and dictionaries. Additionally, Python allows programmers to define custom data structures using a feature called classes.

### list
A list is a sequence of values assigned to a variable. The individual values within a list are called elements or items. You can access the elements of a list using square brackets.

```python
weights=[20,15,19,21,16] 
type(weights)
colors=['red','blue','green','black','white']
colors
a,*b,c=[1,2,3,4]
```

To join the element use `"".join()`

```python
",".join(colors)
```

Use square brackets, `[]`, to index a list and access its elements.

```python
colors[1:3]
colors[:3]
colors[3:]
colors[-1]
colors[1]
colors[:-1]
colors[::-1]
colors[::2] # even indexes
```

The following script demonstrates how to reverse, add new objects, and sort the elements of a list.

```python
colors.reverse()
colors

colors.extend('blue')
colors

colors.extend(['blue'])
colors

sorted(colors)
colors.sort()
colors.sort(key=len)
colors
```

Finding the index of elements and counting their occurrences is very simple. See the example below.

```python
colors.index('blue')
colors.count('blue')
```

To change the element of list use `replace`:

```python
a = 'hello, world!'
a[2]='z'
a.replace('l', 'z', 1)
a.replace('l', 'z')
```

### Tuple
A tuple is a sequence of objects, similar to a list, but it is immutable. To define a tuple, Python uses parentheses:

```python
>>> colors=('red','blue','green','black','white')
>>> type(colors)
<class 'tuple'>
>>> colors[1:3]
('blue', 'green')
```

To access the contents of a tuple, use square brackets, just like a list. While lists and tuples may look similar, the key difference is that the elements of a tuple are immutable, meaning once a tuple is created, its contents cannot be modified.

``` python
>>> colors[1]
'blue'
>>> colors[1]='yellow'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
```
A brief comparison of mutable and immutable types, along with their applications, can be found below: [here](https://www.afternerd.com/blog/difference-between-list-tuple/).


### Set 
Set is a collection of elements without order and index, the same as defined in Algebra. Duplication of elements in set does not make sense, so Python drops the duplication automatically. Use the curly bracket ({) to create the set:

```python
colors={'red','blue','green','black','white'}
type(colors)
```

You can add a new object to a set using `add`, and to add multiple objects, use `update`. To remove elements, use `remove` or `discard`. Both methods remove elements, but `discard` does not raise an error if the element does not exist in the set, whereas remove will.


``` python
colors.add('pink')
colors.update(['purple','orange'])
colors.remove('pink')
colors.remove('pink')
colors.discard('pink')
```

To delete elements from a set, use `clear`, and to remove the set completely, use `del`. To check if an element exists in a set, use the `in` keyword. The functions `len` and sorted can also be applied to sets:

```python
'blue' in colors
len(colors)
sorted(colors)
```

The functions `intersection`, `union`, `difference`, `issubset`, and `issuperset` can be applied on sets:  

```python
'blue' in colors
len(colors)
sorted(colors)
{'red','blue'}.intersection({'red','white'})
{'red','blue'}.union({'red','white'})
{'red','blue'}.difference({'red','white'})
{'red'}.issubset({'red','white'})
{'red'}.issuperset({'red','white'})
```

To create a frozen set, use `frozenset`. A frozen set is immutable, meaning its elements cannot be changed. It can be used as an element in another set or as a key in a dictionary.

### Dictionary
A dictionary is a generalized form of a list, but unlike a list, its indices (keys) can be of any data type. A dictionary maps a set of keys to a corresponding set of values. A dictionary consists of keys and values, where the key acts as the index, and the value is the associated item. In Python, a dictionary is a collection of unique key-value pairs. You construct a dictionary using curly brackets {}, separating keys and values with colons : and each key-value pair with commas ,. Keys must be quoted. You can print the dictionary by referencing it in a print statement.



```python
prices = {
   'BMW': 50,
   'BENZ': 55,
   'Ford': 25,
   'Chevy': 30,  
   'GM': 28
}

prices.values()
prices.keys()
prices.items()
```

The dictionary is very simple to manipulate,  

```python
student={'A':10, 'B':20, 'AB':100 }
student.values()
student.keys()
student['C']=45
student[45]=34
del student['C']
```

Note that dictionaries are unordered, meaning the order in which keys are added does not necessarily reflect the order in which they will be retrieved or displayed.

``` python
dic1={
'x1' : 1,
'x2' : 2,
'x3' : 3 }

dic2={
'y1' : 10,
'x1' : 11,
'x2' : 2 }

dic1.keys() & dic2.keys()
dic1.keys() - dic2.keys()
dic1.items() & dic2.items()
```

To get the value for a specific key if it exists, and assign a default value if it doesn't, use the `get()` method.

```python
dic1.get('x1') 
dic1.get('x4',0) 
```

Example: Create a list where each element is a dictionary.


``` python
team = [
    {
        'name': 'Saeid',
        'city': 'Toronto',
    },
    {
        'name': 'Leila',
        'city': 'Torronto',
    },
    {
        'name': 'Ryan',
        'city': 'Montreal',
    },
```

### Other
One of the most practical data structures is the array, which is an extension of the list and is implemented in NumPy. For more details, see  [chapter2](/python-training-platform/book/ch2_numpy/ch2_overview/). Additionally, you can define your own custom data structure using classes to suit your specific needs.

## Conditionals

### Boolean value
The values True (T) and False (F) are referred to as logical values in Python, with corresponding integer values of 1 and 0, respectively. Run the following code and explain what it does.


```python
>>> 8<9
True
>>> 9<8
False
>>> x=3
>>> y=9
>>> x<y
True
>>> x>y
False
>>>
>>> X=range(-3,3)
>>> [X[i]<2 for i in range(6)]
[True, True, True, True, True, False]
>>> sum([X[i]<2 for i in range(6)])
5
>>> sum(X)
-3
```

One of the main applications of logical operators is to extract specific elements. See the following code examples:

```python
>>> weight=[58,89,68,74,62,77,65,65]
>>> [weight[i]<74 for i in range(len(weight))]
[True, False, True, False, True, False, True, True]
>>> weight<74
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: '<' not supported between instances of 'list' and 'int'
```

Clearly, `weight<74` does not work with a list. [chapter2](/python-training-platform/book/ch2_numpy/ch2_overview/)  discusses the array functionality provided by NumPy, which allows for such operations.

```python
>>> weight=numpy.array(weight)
>>> weight<74
array([ True, False,  True, False,  True, False,  True,True], dtype=bool)
>>> (weight<74) & (weight==89)
array([False, False, False, False, False, False, False, False], dtype=bool)
>>> weight[(weight<74) & (weight==89)]
array([], dtype=int64)
>>> weight[(weight<74) & (weight==62)]
array([62])
>>> weight[(weight<74) | (weight==62)]
array([58, 68, 62, 65, 65])
>>> weight[~(weight<74) & (weight==62)]
array([], dtype=int64)
>>> weight[~((weight<74) | (weight==62))]
array([89, 74, 77])
```

### Control Structure
Commands with control structures often include conditional statements that use comparison operators (>, <, =>, <=, ==, !=, ~, is). 

```python
>>> 3<4
True
>>> 3!=4
True
>>> 3==4
False
>>> 3 is 4
False
>>> 'hi' == 'h' + 'i'
True
>>> 'HI' != 'hi'
True
>>> [1, 2] != [2, 1]
True
>>> ~True
-2
>>> ~False
-1

```

The structure of the `if` statement is as follows: If the condition (`cond`) is satisfied, the corresponding expression (`cons.expr`) is executed; otherwise, the alternative expression (`alt.expr`) is executed.

```python
if(cond)
 cons.expr 
elif (condition) 
 alt.expr 
else 
alt.expr
```

```python
x=4
y=4

if x<y: 
  print('x is less than y')
elif x>y:
 print('x greater than y')
else: 
 print('x and y are equal')
```

To insert a value inside a string, use the f-string format.

```python
if x<y: 
  print( f'{x} is less than {y}')
elif x>y:
 print(f'{x}greater than {y}')
else: 
 print(f'x={x} and y={y} are equal')
```

Variables can be combined using the logical operators `or`, `and`, and `not`.
```python
a or b
a and b
not a
(a or b) and not (c or d)
```

The `in` operator can also be used with lists and strings.
```python
'a' in ['a', 'b']
'a' in ['c', 'b']
```


See [chapter2](/python-training-platform/book/ch2_numpy/ch2_overview/) for more information about logical values.


### Try except

When there is a possibility of an error, it is better to use `try` and `except`. The try block tests the code for errors, and if an error occurs, the program moves to the except block. If no error occurs, it proceeds to the else block. Its structure is very simple as below

```py
try:
    code in this block if things go well
except:
    code in this block run if things go wrong
```


```python 
x='Just test'
try:
  print(x)
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

try:
  print(y)
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
```

You can catch specific error types, but here we present a generic except block. We discuss handling specific errors in [Chapter 13](python-training-platform/book/ch13_debugging/ch13_error_handling/), which makes debugging the code easier.

## Function
In programming, a function is a sequence of statements that performs a computation. A function has three main parts: arguments, the function body (script), and the output. Python has two types of functions: built-in functions, which are part of the core Python language or included in packages, and user-defined functions, which are written by the user.

### Built-in function
Python includes a number of core functions that are always available. For more details, [see](https://docs.python.org/3/library/functions.html)

``` python
x=[1,2,3]
type(x)
len(x)
min(x)
```

To round a value, use the `round(value, digits)` function, where value is the number to be rounded and digits specifies the number of decimal places.

```python
round(0.12345,2)
round(0.12345,3)
```

### User function
A function has three main parts: arguments, the function body (script), and output. It has a simple structure.

```python
def name (argument):  
  script
  return output
```

For instance, write a function that takes two arguments, adds them together, and returns the result.

```python
def sum0 (x,y):  
  s0=x+y
  return s0
```

If you do not specify the arguments explicitly, use a * argument to accept a variable number of arguments.

``` python
def sum0 (x,*y):  
  s0=x+mean(y)
  return s0
```

You can define a default value for an argument by assigning a value to it in the function definition. This value will be used if no argument is provided when the function is called.
```python
def sum0 (x,y=1):  
  s0=x+y
  return s0
```

You can define an optional argument by assigning a default value to it in the function definition:
```python
def sum0 (x,y=None):  
     if y is None:
       return x
     else:
       return x+y
```

```python
def letterGrade(score):
    if score >= 90:
        letter = 'A'
    elif score >= 80:
        letter = 'B'
    elif score >= 70:
        letter = 'C'
    elif score >= 60:
        letter = 'D'
    else:
        letter = 'F'
    return letter
```    

### In-line function
A simple function can be written in a single line.
``` python
sum0 = lambda x, y: x + y
sum0(2,3)
```


Such a function is more suitable for use inside other operations. The following example takes the first and last names, then sorts them according to the last name:

```python
names = ['Sam Amiri','Ryan Amiri']
sorted(names, key=lambda name: name.split()[-1].lower())
>>> sorted(names, key=lambda name: name.split()[-1].lower())
['Sam Amiri', 'Ryan Amiri']
>>> sorted(names)
['Ryan Amiri', 'Sam Amiri']
```

Example: Write a function to return the derivative for a given expression with respect to dx: 
```python
def der(f,dx):
    def _fun0(x):
     return((f(x+dx)-f(x))/dx)
    return(_fun0)
der0=der(lambda x: x**2,0.1)
der0(x=2)
``` 

### Map and Filter
Python provides access to higher-order functions, which allow functions to operate on other functions, either by taking a function as an argument or by returning a function. The most popular higher-order functions are `map` (which applies a function to each element) and `filter` (which applies a function and returns the element if it evaluates to True). Additionally, reduce can be imported from the functools module (`from functools import reduce`).

```python
x=[-1,0,1]
list(map(abs, x))
list(filter(lambda x: x <= 0,x))
 ```

Example: Write a function to divide two numbers. If the denominator is zero, terminate the function and display a notification.

``` python
def divide(x, y):
  try:
    x / y
  except: 
   print('Can not divide by zero!')
  else:
   return x / y

divide(3,1)
divide(3,0)
```

The function can also be rewritten using `raise`, which triggers an error and stops the function.

``` python
def divide(x, y):
    """Divide Function"""
    if y == 0:
        raise Exception('Can not divide by zero!')
    return x / y


map(lambda x: x + 1, range(10))
filter(lambda x: x > 5, range(10))
reduce(lambda out, x: out + x, range(10))   
```


### Argument
To pass an undefined number of arguments as a list or dictionary, you can use *args and **kwargs, respectively. For example, if you have a function like this:

```python
def printlist(*args):
     print (args)
     print(args[1])

printlist(1, 2, 3, 4, 5)

def printdict(**kwargs):
    print (kwargs)

printdict(name="SA", course="STAT")


def printdict(name,**kwargs):
    print(name)
    print((kwargs))


d={'name':"SA",'course':"STAT",'grade':3}
printdict(**d)

def func0(**kwargs):
  for i, item in kwargs.items():
        print(f"{i}: {item}")
    print(kwargs['a'])

func0(**d)

def func(*args, **kwargs):
    print(args[1])
    print(kwargs['a'])

func(1, 2, a=3, b=4)
```

## Iteration
Python is equipped with powerful tools for repeating commands or generating sequences of numbers. The $:$ symbol is used to produce a series of numbers between two specified values.

### Range
```python
range(3,15)
```

To generate a series of numbers from one value to another with a specific increment.

```python
>>> np.arange(8, 20,1)
array([ 8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])
>>> np.arange(21,30,3)
array([21, 24, 27])
>>> np.arange(2,1,-0.1)
array([ 2. ,  1.9,  1.8,  1.7,  1.6,  1.5,  1.4,  1.3,  1.2,  1.1])
```

specific element can be repeated a defined number of times.

```python
>>> [2,3]*2
[2, 3, 2, 3]
>>> numpy.repeat([2, 3],[2,3])
array([2, 2, 3, 3, 3])
>>> numpy.repeat(["A", "B"],[2,3])
array(['A', 'A', 'B', 'B', 'B'],dtype='<U1')
```

### For
The most useful command for iteration is `for`, which repeats specified commands a defined number of times. Run the following code to see how it works:

```python 
>>> for r in range(1,5):
...  print(r**3)
...
2
1
0
7

 >>> for i in [2,3,1,7]:
...  print(i**3)
...
1
0
2
4
```  

```python
>>> score=[10, 15, 7, 20]
>>> for i in (range(0,4)):
...  if (score[i]<10):
...       print("fail")
...  else:
...        print("pass")
...
pass
pass
fail
pass

for i, item in enumerate(score):
  print(i,item)
```

```python
>>> for i in range(0,4):
...   if score[i]<10:
...       print("fail")
...   elif(score[i]>=10&score[i]<14):
...       print("middle")
...   elif(score[i]>=14&score[i]<17):
...        print("good")
...   elif(score[i]>=17):
...       print("BEST")
...
middle
middle
fail
middle
```

```python
for i, j in zip(a, b):
    print(i,j)
```

### While
The `while` command runs until the condition specified is met.


```python
>>> x=8
>>> i=0
>>> while(x<12):
...   i=i+1
...   x=x+x/8
...   print(i,x)
...
1 9.0
2 10.125
3 11.390625
4 12.814453125
```

Conversely, the repeat command continues until the condition specified within the commands is met. In the following code, the loop continues until the condition `(x > 12)` is no longer true:


```  python  
>>> x=8
>>> i=0
>>> while True:
...  i=i+1
...  x=x+x/8
...  print(i,x)
...  if (x>12):
...    break
...
1 9.0
2 10.125
3 11.390625
4 12.814453125
```

Example: Write a simple function to select the prime numbers between 1 and 100 (though not the most efficient approach).

```python
num0=[1]
for num in range(2,100):      
    if 0 not in num%np.array(range(2, num)):
     num0.extend([num])

print(num0)     
```

Example: Write a simple function to select pairs of unequal numbers between 1 and 3.

```python
combs=[]
for x in range(3):
 for y in range(3):
  if x!= y:
    combs.append((x,y))
```

The code can be simplified using list comprehension.

```python
[(x,y) for x in range(3) for y in range(3) if x!=y]
```

Example: Generate numbers between 1 and 10 and store them in different Python data structures.

```python
# A generator expression

print ((x for x in range(10)))

# A list comprehension
print ([x for x in range(10)])

# A set comprehension
print ({x for x in range(10)})

# A dictionary comprehension
print ({x: x for x in range(10)})
```


## Variable 
To check the existing variables, use `globals()`. The environment within a function is `local`, and it can be accessed using `locals()`.

```python
def foo():
    name="SA"
    print (locals())

foo()

print (locals())
print (globals()) 
```
[scope and namespace](/Volumes/F/python_training_platform0/python_training_platform/docs/book/ch1_primer/ch1_scope_and_namespace.md) discusses in more detail the regions in the code.


## String
Python has several function to work with string, in this subsection, we go through some basic in  working with strings. 

```python
var1='Hello Python 3, it is my 1st sentence'
var2='I like it!'
var1[0]
var1[0]*2
var1[0:6]
var1+','+var2
'H' in var1 
'z' not in var1 
var2.capitalize()
var1.count('o')
var1.count('o',0,6)
var1.expandtabs(tabsize=200)
```

`find()` the position of the substring, `rfind()` finds the last occurrence of the specified value.
```python
var1.find('t')
var1.find('t',0,50)
var1.rfind('t',0,50)
var1.find('q',0,50)
```

Checks whether the string consists of alphanumeric characters, alphabetic, numeric digits, lowercase, space, lower, or upper: 

```python
var1.isalnum()
var1.isalpha()
var1.isdigit()
var1.isnumeric()
var1.isspace()
var1.islower()
var1.isupper()
```

You can check whether is the string is numeric or decimal?  
```python
str = "2009"  
str.isdecimal()
```


```python
len(var)
'_'.join(["a", "b", "c"])
```

You can add the space at the right or left:  

```python
var1.ljust(50, '0') 
var1.rjust(50, '0')
```

```python
var1.lower()
var1.upper()
var1.swapcase()


max(var1)
min(var1)
```
Replace a string with an alternative string,  in the below all `o` replace with 3, in the second one just second occurrence will be replaced. 
```python
var1.replace('o','J')
var1.replace('o','J',2)
```


```python
str1.rindex(str2)
str1.index(str2)
str1.find(str2)
```

You can remove the leading, trailing and duplicate spaces: 
```python
var1.rstrip()
var1.lstrip()
var1.strip()
```


You can split the strig with withspace
```python
var1.split('e',1)
var1.split(',',1)
```

Also splits the string at line breaks and returns a list of lines in the string.

```python
str="It is \n line"
str.splitlines() 
```




Fill left with zero 
```python
str.zfill(50)
```

Check whether the string starts\end with a specific string.
```python
var1.startswith('H')
var1.endswith('e', 1, 100)
```

