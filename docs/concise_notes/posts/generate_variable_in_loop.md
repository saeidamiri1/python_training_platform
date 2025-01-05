---
date: 2024-10-27
title: How generate variable name using loop item
description: How generate variable name using loop item
categories:
  - Python core
authors:
  - saeidamiri1
---

# How generate variable name using loop item 
If you need to create the variable name using the loop object, use `exec`. 
<!-- more -->
The exec() function executes dynamically created Python code, which can be provided as either a string or a code object:
````
for i in range(4):
    exec(f'var_{i} = [range(i)]')
````

I personally prefer using the dictionary object instead the variable. 
````
var={}
for i in range(4):
    var[f'var_{i}']=range(i)
````







