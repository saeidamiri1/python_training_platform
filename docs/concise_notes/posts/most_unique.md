---
date: 2024-10-26
title: How find most most unique item
description: How find most most unique item
categories:
  - Python core
authors:
  - saeidamiri1
---

# How find most most unique item
If you need to count of each unique item from an object, use module `collections` module, the following code return the 3 most common items from the given object:
````
from collections import Counter
c = Counter(l)
c.most_common(3)
````
