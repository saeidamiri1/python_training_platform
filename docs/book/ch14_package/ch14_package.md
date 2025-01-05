---
title: Package
---

As we discussed in [module](../primer/module.md),  any python source called module. Here we discussed packages which is actually a collection of modules.

The folder .. includ an example of a simple package, you can see 

``` py
# To this
pachage_temp/
    __init__.py
    main.py
    sub1/
        __init__.py
        sub1_mod1.py
    sub2/
        __init__.py
        sub2_mod2.py
```

For any folder you need to have  `__init__.py` which may be empty, it makes Python treat directories containing it as modules.
The code inside `__init__.py` runs automatically when we import the package. A package serves as namespace for space which can be multilevel imports. Now can run the code as below 

``` py
cd ./mypachage
import mypachage.main as  mym
mym.func1()

from mypachage.main import func1
func1()

import mypachage.sub1.mod1 as mys
mys.func2()
```


After running, python create the file `__pycache__` that's sitting in your directory. This contains pre-compiled Python modules from before. You can remove it.

## __init__.py
As you notice, to call function we need to call function via module, to extract function, one can add module\submodules in `__init__` which imported when it run: 

``` py
# in __init__.py
print("Initializing __init__ from mypachage")
from .main import *
```

Now one can import the function directly. 
``` py
from mypachage1 import func1
```

## __name__ == '__main__':
At the end of module, we add   `if __name__ == '__main__':` the code after it executes only when you run entire code, hence it does not execute execute when you import function from it

``` py
python3 ./mypachage1/main.py
```
