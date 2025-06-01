---
title: Subprocess
---

# Subprocess
The subprocess module allows you to spawn new processes, connect to their input/output/error pipes, and obtain their return codes.

## run
`subprocess.run()` executes a shell command or external program from within a Python script.

```python
from subprocess import run,Popen,PIPE

user_input = "-l"
out = run(["ls", user_input])
if out.returncode == 0:
    print("was a success")
else:  
    print("was unsuccesful")
```

The command must be provided as a list; if it's given as a string, use `.split()` to convert it.

```python
import shlex
proc1="ls -l"
out = run(shlex.split(proc1))
```


If you have a sequence of commands in a Bash script file, you can run it as shown below:

```python
methodproc1 = run(["process_one.sh"], stdout=PIPE)
subprocess.run(["process_two.sh"], stdin=proc1.stdout)
```

## Popen
Use `subprocess.run()` to execute a command and wait for it to finish. If you want to perform other tasks while the process is running, use `subprocess.Popen` instead. To send input to and receive
output from the process, call `Popen.communicate()`. In fact, `subprocess.run()` is a higher-level wrapper around `Popen` and `Popen.communicate()`.

```python
with Popen(["ls", user_input], stdout=PIPE) as proc: 
    out = proc.stdout.readlines()
    print(out)


for file in out:
    print(file.strip())
```

We often use try/except blocks to handle errors, as shown below.

```python
proc = Popen(["ls", user_input], stdout=PIPE)
try:    
    out,err = proc.communicate(timeout=30)
except TimeoutExpired:
    proc.kill()  
    out,err= proc.communicate()

print(out)
print(err)
```

Let's test `ls ~` using  Popen: 


```python
import os 
user_input = "~"  # or any path from user input
expanded_path = os.path.expanduser(user_input)
with Popen(["ls", expanded_path], stdout=PIPE, stderr=PIPE) as proc: 
     print(proc.stderr)
     print(proc.stdout)

with Popen(["ls", expanded_path], stdout=PIPE, stderr=PIPE) as proc: 
     print(proc.stderr.readlines())
     print(proc.stdout.readlines())
```



In larger programs, this is especially useful for writing pipelines. The following function runs an R script without exiting the Python environment.

```python
import subprocess
subprocess.check_call(['/usr/local/bin/Rscript', './Desktop/rtest.R'])
```
To save output of R in Python, run 
```python
Out=subprocess.check_output(['/usr/local/bin/Rscript', './Desktop/rtest.R'])
```


To control error, use try\except: 
```python
try:
    Out=subprocess.check_output(['/usr/local/bin/Rscript', './Desktop/rtest.R'])
except subprocess.CalledProcessError as e:
    print(e.output)
```