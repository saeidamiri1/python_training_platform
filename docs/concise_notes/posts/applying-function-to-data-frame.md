---
date: 2024-10-26
title: Applying function on data-frame
description: How to apply a function on row or column
categories:
  - Dataframe
  - Numpy
authors:
  - saeidamiri1
---

# Applying function on data-frame
Using ```df.apply(fun)``` can apply a function on columns or row:
<!-- more -->

```
df.apply(np.sum, axis=0)
df.apply(np.sum, axis=1)
```

Even can write a new function and run on columns or rows
```
def prod(col):
    return col['A'] * col['B']

df.apply(prod, axis=1)
df['productcolmn']=df.apply(prod, axis=1)
```