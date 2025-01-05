---
title: class and object
---

# Class and object 
## introduction
Python is an object-oriented programming language, and has strong tools working with different objects. If the structure is not defined, one can create own object (An object is simply a collection of data (variables) and functions ) which can be done using list;  
the class can be used to present new structure for your data or change the existing one. It is very useful to tie  a certain data and functions together that act on the data; it is actually a pack of collection stuff like factory that has different department with well-planed task.    

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

Or it can be simpified to

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

Example: American present the data as
Month/Day/Year. Write a fucntion represent it with Candaian style.

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

The class creates a new local namespace and stores all its attributes which may be data or functions.  

```python
print(dateg.__doc__)
```

## initialize
Sometime is better to initialize the variables in the begining, it can be done using `__init__`
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

Since the value has a limitation, we need to add a boundary to it. It can be done using the seeter and getter: 

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

Note: In Python, the underscore `_` at the beginning  means it is a private variable.

Obviously, the code must be written carefully, otherwise it generates many errors. To overcome the problem, one can use the `property` class. The following code shows how `property`avoid creating new names for the getters and setter. 


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

Using the decorators can simplify the structure, a decorator is function that add new functionality to a function that is passed as arguments


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

Example: Create a function create email for a new employee, 

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


Write a function to calculate mean  

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
To present the values object attributes, one can use the `__str__`, which is a [operator overloading](./operator_overloading.md) and is discussed in : 

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

