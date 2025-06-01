
---
title: Debugging
---


## Reading Traceback
The following demonstrates how to use the `sys` function to determine what error occurred. Let's try a simple mathematical operation and see which error might arise.

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

It shows that the program crashed on the last line. Of course, this isn't always easy to diagnose, so you can copy the error message and paste it into Google for more help.

## Interactively
To run interactively or in a REPL (Read-Eval-Print Loop), use the `-i` option to keep Python running.

```bash
python3 -i temp.py
```

When an error occurs, the Python environment pops up, allowing you to interactively work within Python to troubleshoot the error.


## Warning
If you need to keep track of warnings, use the warnings module. The warning messages will be stored in `sys.stderr`.

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

If you want the program to stop execution as soon as a warning occurs, use the `-W error` option when running the script.

``` py
python -W error temp.py
```
To mute all warning use `-W ignore`

``` py
python -W ignore temp.py
```


## Run under debugger
You can manually add a debugger into your code using `breakpoint()`, which calls the `sys.breakpointhook()` function—by default, this invokes pdb.set_trace() from the pdb module. Alternatively, you can run an entire program under the debugger by inserting `pdb.set_trace()` directly.

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

Then you can use debugger commands to step through the code. Type `c` to continue execution. Use !statement to execute a Python statement, and `!entry` to view the current value of the variable `entry`.


```bash
(Pdb) !entry
2
```

You can use the following code to help debug your program.

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


