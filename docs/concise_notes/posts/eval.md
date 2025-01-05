---
title:  eval Function
description: eval Function
date: 2024-11-21
categories:
  - Notes
---


# eval Function
The `eval()` function evaluates the specified expression (code), and runs it. The syntax is as below

<!-- more -->

``` python 
eval(expression, globals, locals)
```

|Parameter| Description|
|---|--|
|expression |	A String that will be evaluated as Python expression|
|globals (Optional)| A dictionary that holds global parameters|
|locals (Optional)| A dictionary that holds local parameters|



Let's drop the extra quote.
```
>>> x = '"55"'
>>> eval(x)
'55'
```

The following performs the specified operations:
```
>>> x = 2
>>> eval('x * x +3')
7
```


Let's transfer a dictionary of functions and simply choose from it.
``` python 
list = {'Plus': lambda x, y: x + y, 'Minus': lambda x, y: y - x}
print(eval('Minus(2,8)', list))
```

``` python
>>> list = {'Plus': lambda x, y: x + y, 'Minus': lambda x, y: y - x}
>>> print(eval('Minus(2,8)', list))
6
```