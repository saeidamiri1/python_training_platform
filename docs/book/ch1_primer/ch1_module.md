---
title: Module
---

# Module
Any Python source file with the `.py` extension can be imported into Python's environment. Therefore, it is common practice to organize code by creating a separate file and importing it when needed. For instance, you can create a file named `primer.py`.

``` python
#primer.py
import os
print(os.getcwd())

def letterGrade(score):
    if score >= 90:
        letter = 'A'
    elif score >= 80:
        letter = 'B'
    elif score >= 70:
        letter = 'C'
    elif score >= 60:
        letter = 'D'
    else:
        letter = 'F'
    return letter

names = ['Sam Amiri', 'Leila Alimehr','Ryan Amiri']   
```

<!-- cd '/Users/samamiri/Library/CloudStorage/GoogleDrive-saeid.amiri1@gmail.com/My Drive/python/python-practice0/mkdocs2/codes/' -->
Now import the created module, 

``` python
import primer
primer.letterGrade(88)
print(primer.names)
```


If the file containing the functions is not in the current working directory, you can use the sys module to add its directory to the system path. Here's an example:

``` python
import sys
sys.path.append('/path_to_file/')

import primer
```

You can refer to the [package section](/package/overview.md)) section to learn more about organizing and packaging functions.