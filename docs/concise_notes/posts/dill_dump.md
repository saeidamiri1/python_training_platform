---
date: 2024-10-26
title: How to save all objects
description: How to save all objects
categories:
  - Python core
authors:
  - saeidamiri1
---

# How to save all objects

```
import dill
# to save session
dill.dump_session('backup_2021_10_22.db')
# to load 
backup_restore = dill.load_session('backup_2021_10_22.db')
```




