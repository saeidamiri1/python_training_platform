---
title: Operator Overloading
---

# Operator Overloading

## Introduction
In python you can define a operator to achieve a specific computation, the following shows 
how to add and subtract 

```python
class point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return "({self.x},{self.y})"
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return point(x, y)
    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return point(x, y)
```
functions can recalled vas below: 
```python
p1 = Point(1, 2)
p2 = Point(2, 3)

print(p1+p2)
print(p1.__add__(p2))
print(Point.__add__(p1,p2))
```

Special functions are listed in the below: 

|  |  | ||
|--|--|--||
|`__init__`  | initialize the attributes of the object       | |
|`__str__`   | returns a string representation of the object ||
|`__len__` | returns the length of the object||
|`__call__`| call objects of the class like a normal function||
|`__add__`| adds two objects| `p1 + p2`  |`p1.__add__(p2)`|
|`__sub__` | Subtraction | `p1 - p2` | `p1.__sub__(p2)` |
|`__mul__` | Multiplication | `p1 * p2` | `p1.__mul__(p2)` |
|`__pow__` | Power | `p1 ** p2`  | `p1.__pow__(p2)` |
|`__truediv__` | Division | `p1 / p2` | `p1.__truediv__(p2)` |
|`__floordiv__` | Floor Division | `p1 // p2` | `p1.__floordiv__(p2)` |
|`__mod__` | Remainder (modulo) | `p1 % p2` | `p1.__mod__(p2)` |
|`__lshift__` | Bitwise Left Shift | `p1 << p2` | `p1.__lshift__(p2)` |
|`__rshift__` | Bitwise Right Shift | `p1 >> p2` | `p1.__rshift__(p2)`|
|`__and__` | Bitwise AND | `p1 & p2` | `p1.__and__(p2)` |
|`__or__` | Bitwise OR | `p1 | p2` | `p1.__or__(p2)` |
|`__xor__` | Bitwise XOR | `p1 ^ p2` |  `p1.__xor__(p2)`| 
|`__invert__` | Bitwise NOT | `~p1`  | `p1.__invert__()` |



## call 
When `__init__` is called, the object created and it can be initiated. 
Sometimes, you want to redefine your object which can be done in `__call__`.

``` python
class test(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        print (f'{self.x} {self.y}')
    def __call__(self, y):
        self.y = y
        print (f'__call__ {self.x} {self.y}')

init1 = test(1, 2)
init1.x=2
init1(7)
init1(8)
```

The following show how to use `__call__` to track the numebr of execution.  

```python
class counter:
     def __init__(self, start=0):
         self.count = start
     def __call__(self):
         self.count += 1
         print(f"Current count is {self.count}")

counter = counter()
counter()
```


## iter and next
`iter` and `next` are very useful for go through one by one. `iter` assign an object as an iterator. The next() function returns the next item in an iterator. Its synatx is `next(iterator, default)` , the default is the value return if the iterator reach to its end. 

```
list = iter(["one", "two"])
x = next(list, "end")
print(x)
x = next(list, "end")
print(x)
x = next(list, "end")
print(x)
```

The following show how to generate Fibonachi series. 
```python
class Fib:                                        
    def __init__(self, max):                      
        self.max = max
    def __iter__(self):                           
        self.a = 0
        self.b = 1
        return self
    def __next__(self):                           
        fib = self.a
        if fib > self.max:
            raise StopIteration                   
        self.a, self.b = self.b, self.a + self.b
        return fib       
```
``` python
for n in Fib(1000):
   print(n, end=' ')
```


## classmethod and staticmethod
These are a function in an object's namespace, accessible as an attribute. A class method gets the class (we usually call it cls) as the implicit first argument. A static method gets no implicit first argument (like a regular function).

`@staticmethod` function is nothing more than a function defined inside a class. It is callable without instantiating the class first. It’s definition is immutable via inheritance.

``` python 
from datetime import date
 
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # a class method to create a
    # Person object by birth year.
    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)
    # a static method to check if a
    # Person is adult or not.
    @staticmethod
    def isAdult(age):
        return age > 18
 
person1 = Person('mayank', 21)
person2 = Person.fromBirthYear('mayank', 1996)
 
print(person1.age)
print(person2.age)
```
