---
title: Inheritance
---


# Inheritance 
## Introduction 
Inheritance allows a class (called a child or subclass) to inherit attributes and methods from another class (called a parent or base class). This enables code reuse and establishes a hierarchical relationship between classes. In other words, it allows a new class to build upon an existing one, inheriting its structure and behavior.

```python
class Parent:
    ...

class Child(Parent):
    ...
```

The new class, Child, is called a subclass.

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

If you need to access a temporary object from the parent class, use the super() function.
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

If `__init__` is defined in a subclass, it is essential to initialize the parent class using super().

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

You can inherit from multiple classes in Python, a feature known as multiple inheritance.

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
