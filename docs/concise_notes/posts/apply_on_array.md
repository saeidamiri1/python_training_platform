---
date: 2024-10-26
title: How run apply on array
description: How run apply on array
categories:
  - Numpy
authors:
  - saeidamiri1
---

# How run apply on array

```
import numpy as np
x = np.array([[5,2,1,3], [2,1,5]])
fun = lambda t: np.argmax(t)
np.array([fun(xi) for xi in x])
```
