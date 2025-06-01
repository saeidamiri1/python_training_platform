---
title: class and object
---

# Class and object 
## introduction
Python is an object-oriented programming language and provides powerful tools for working with various types of objects. When a suitable data structure is not already available, you can define your own object. An object is simply a collection of data (variables) and functions (methods) that operate on that data. While basic structures like lists can group values, classes allow you to define custom data structures or modify existing ones.

Classes are particularly useful for combining related data and behavior, keeping everything organized and reusable. You can think of a class as a blueprint or a well-structured factory, where each component (like a department) has a clear and well-planned role.

```python
class body(object):
    """Define class"""
    """ we can use weigt and height"""
    def __init__(self, weight,height):
     self.weight=weight
     self.height=height
def bmi_body(b):
    print (' BMI is (%g)' %((b.weight/b.height)))

SAM = body(90,79)
SAM.weight
SAM.height
print (SAM)
bmi_body(SAM)
```    

Or, it can be simplified as follows:

```python
class body(object):
    """Define class"""
    """ we can use wheigt and height"""
def bmi_body(b):
    print (' BMI is (%g)' %((b.weight/b.height)))

SAM = body()
SAM.weight = 90
SAM.height = 79
print (SAM)
bmi_body(SAM)
```

Let's explain it further with an example. In the U.S., dates are typically written as Month/Day/Year. Write a function that converts this format to the Canadian style, which is Day/Month/Year.

```python
class dateg(object):
    """Define class"""
    """Month, Day, Year """
def ca_date(d):
    print (' Canadian date is (%g/%g/%g)' %((d.day,d.month,d.year)))

mybirt = dateg()
mybirt.day = 11
mybirt.month = 11
mybirt.year = 11
print (mybirt)
ca_date(mybirt)
```

A class creates a new local namespace and stores all its attributes, which can include both data and functions.

```python
print(dateg.__doc__)
```

## initialize
Sometimes it's better to initialize variables at the beginning, which can be done using the `__init__` method.

```python
class dateg(object):
    """Define class"""
    """Month, Day, Year """
    def __init__(object,d=1,m=1,y=1):
        object.day=d
        object.month=m
        object.year=y

def ca_date(d):
    print (' Canadian date is (%g/%g/%g)' %((d.day,d.month,d.year)))

mybirt = dateg()
mybirt.day = 11
mybirt.month = 11
mybirt.year = 11
print (mybirt)
ca_date(mybirt)
```

Since the value has limitations, we need to enforce boundaries. This can be done using setter and getter methods.

```python
class body(object):
    def __init__(object,weight,height):
        object.set_weight(weight)
        object.set_hight(height)
  # getter method
    def get_weight(object):
        return object._weight
    def get_height(object):
        return object._height        
    # setter method
    def set_weight(object, value):
        if value < 0:
            raise ValueError("Weight below 0 is not possible.")
        self._weight = value
    def set_height(object, value):
        if value < 0:
            raise ValueError("Height below 0 is not possible.")
        self._height = value
 def bmi_body(b):
    print (' BMI is (%g)' %((b.weight/b.height)))

SAM = body(90,79)
print(SAM)
print(SAM.get_weight)
print(SAM.get_height)
print(SAM.bmi_body)
```

Note: In Python, a leading underscore (_) before a variable name is a convention that indicates it is intended to be private, meaning it should not be accessed directly from outside the class.

Clearly, the code must be written carefully to avoid errors. To help with this, Python provides the property class, which allows you to define getters and setters without creating separate method names. The following example shows how property simplifies access and updates to class attributes.

```python
class body(object):
    def __init__(object,weight=.01,height=.01):
        object.weight=weight
        object.height=height
    def bmi_body(b):
        print (' BMI is (%g)' %((b.weight/b.height)))
    # getter method
    def get_weight(object):
        return object._weight
    def get_height(object):
        return object._height        
    # setter method
    def set_weight(object, value):
        if value < 0:
            raise ValueError("Weight below 0 is not possible.")
        object._weight = value
    def set_height(object, value):
        if value < 0:
            raise ValueError("Height below 0 is not possible.")
        object._height = value
    weight = property(get_weight, set_weight)
    height = property(get_height, set_height)



SAM = body(90,79)
print(SAM)
print(SAM.get_weight())
print(SAM.bmi_body())
```

Using decorators can simplify the structure. A decorator is a function that adds new functionality to another function, which is passed as an argument.

```python
class body(object):
    def __init__(object,weight=.01,height=.01):
        object.weight=weight
        object.height=height
    def bmi_body(b):
        print(' BMI is (%g)' %((b.weight/b.height)))
    @property
    def weight(object):
        return object._weight
    @property
    def height(object):
        return object._height        
    @weight.setter
    def weight(object, value):
        if value < 0:
            raise ValueError("Weight below 0 is not possible.")
        object._weight = value
    @height.setter    
    def height(object, value):
        if value < 0:
            raise ValueError("Height below 0 is not possible.")
        object._height = value


SAM = body(90,79)
print(SAM)
print(SAM.weight)
print(SAM.bmi_body())
```

Let's explain it further with an example. Create a function to generate an email for a new employee.

```python
class Create_employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        print('New Employee: {} - {}'.format(self.fullname, self.email))
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

new_emp_1 = Create_employee('Sam', 'Amiri')
new_emp_1.email
new_emp_1.fullname
```


To practice further, let's write a function to calculate the mean (average) of a list of numbers.

```python
class Mean(object):
  def __init__(self):
    self.vals = []
  def add_value(self, x):
    self.vals.append(x)
  def result(self):
    return sum(self.vals)/len(self.vals)
  def  reset_states(self):
    self.vals = []

aa=Mean()
print(aa)
aa.add_value(3)
aa.add_value(2)
aa.result()
aa.reset_states()
```


## Object presentation 
To display the values of an object's attributes, you can use the `__str__` method, which is an example of [operator overloading](./operator_overloading.md) and is discussed in:

```python
class body(object):
    """Define class"""
    """ we can use weigt and height"""
    def __init__(bd, weight,height):
     bd.weight=weight
     bd.height=height
    def __str__(bd):
     return("weight: {0} Height: {1}".format(bd.weight, bd.height))

SAM = body(90,79)
print(SAM)
SAM.__str__()
```

