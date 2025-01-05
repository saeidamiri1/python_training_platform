---
title: Debugging
---


## Reading Traceback
The following show how to use `sys` function to find out what error happen, let try a simple mathemtic operation and see what error might happen.    

``` py
list_n = [2,1,0]
for entry in list_n:
        entry=entry*2
        print("The entry is", entry)
        print('DEBUG:', repr(entry))
        r = 1/int(entry)
print('End of code')
```

```bash
python3 temp.py

The entry is 2
The entry is 1
The entry is 0
Traceback (most recent call last):
  File "./temp.py", line 4, in <module>
    r = 1/int(entry)
        ~^~~~~~~~~~~
ZeroDivisionError: division by zero
(venv) samamiri@Sams-MacBook-Pro python-practice0 % 
```

It shows it crashed in the last line, ofc ourse it is not always easy, so copy error and past in Google to get more help. 

## Interactively
To run interactively or REPL (Read-Eval-Print Loop), use option `-i` to keep python alive. 

```bash
python3 -i temp.py
```
when the error occurs, python environment pop up and one can interactively work inside python around error. 


## Warning
If one need to to keep warning, use the warnings module, the warning meesages would store in `sys.stderr`.

``` py
import warnings
list_n = [2,1,0]
for entry in list_n:
    print("The entry is", entry)
    if entry == 0:
            warnings.warn("This is a warning note")
    r = 1/int(entry)
print('End of code')
```

If you want to stop the executation as soon as error happen use  `-W error ` in the running.

``` py
python -W error temp.py
```
To mute all warning use `-W ignore`

``` py
python -W ignore temp.py
```


## Run under debugger
You can manullay add debugger inside you code using ` breakpoint()`, which calls `sys.breakpointhook()` function  which is actually `pdb.set_trace()` from  the `pdb` module. You can also run an entire program under debugger by calling `pdb.set_trace()`.

``` py
list_n = [2,1,0]
for entry in list_n:
    print("The entry is", entry)
    breakpoint()
    r = 1/int(entry)
print('End of code')
```

```bash
python3 -m pdb temp.py
The entry is 2
> ./temp.py(6)<module>()
-> r = 1/int(entry)
(Pdb) 
```
Then you can use the debugger commend to debug the code. you can type `c` to continue running code. `!statement` execute statement, type `!entry` to get the current valur of `entry`

```bash
(Pdb) !entry
2
```

You can use the following code to debug your code.

|Command| Syntax|Description|
|--|--| --|
|help | | Get help|
|w|where|Print stack trace|
|d|down|Move down one stack level|
|u|up|Move up one stack level|
|b loc|break loc|Set a breakpoint|
|s|step|Execute one instruction|
|c|continue|Continue execution|
|l|list|List source code|
|a|arg|Print args of current function|
|!statement||Execute statement|


