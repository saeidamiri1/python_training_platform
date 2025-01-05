---
title: Inheritance
---



# Inheritance 
## Introduction 
You transfer the the existing class to a new one, it structure is 
```python
class Parent:
    ...

class Child(Parent):
    ...
```

The new class Child is called a subclass. 

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name 
        self.shares = shares
        self.price = price
    def cost(self):
        return(self.shares*self.price)
    def sell(self, nshares):
        self.shares -= nshares


class MyStock(Stock): 
    def panic(self):
        self.sell(self.shares)

s = MyStock('GOOG', 100, 490)
s.shares
s.sell(20)
s.shares
s.panic()
```

IF you need a temporary object from the parent class by the keyword, use the super() function 
```python
class MyStock3(Stock):
    def cost(self):
        actual_cost = super().cost()
        return(f'1.2 * {actual_cost}')

s = MyStock('GOOG', 100, 490)
s.shares
s.sell(20)
s.shares
s.cost()
```


If `__init__` is defined, it is essential to initialize the parent. 

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
    def cost(self):
        return(self.shares*self.price)


class MyStock(Stock):
    def __init__(self, name, shares, price, factor):
        super().__init__(name, shares, price)
        self.factor = factor
    def cost(self):
        return self.factor * super().cost()

s = MyStock('GOOG', 100, 490,5)
s.cost()
```

You can inherit from multiple classes, 

```python
class Mother:
    ...

class Father:
    ...

class Child(Mother, Father):
    ...
```


```python
class Stock_n:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

class Stock_sp:
    def __init__(self,name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
    def cost(self):
        return(self.shares*self.price)


class MyStock(Stock_n,Stock_sp):
    def __init__(self, name, shares, price, factor):
        super().__init__(name,shares, price)
        self.factor = factor
    def cost(self):
        return self.factor * super().cost()


s = MyStock('GOOG', 100, 490,5)
s.cost()
```
