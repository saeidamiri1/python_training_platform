---
title:  Global variables in imported module
description: Global variables in imported module
date: 2024-11-21
categories:
  - Notes
---


# Global variables in imported module
If you want to handle a global variable in an imported module, simply add it to the builtin module. Let's assume that `VAR` is a global variable in the `fun1` function within the test module:

```
import builtins
import test
builtins.VAR = 3
test.fun1()
```