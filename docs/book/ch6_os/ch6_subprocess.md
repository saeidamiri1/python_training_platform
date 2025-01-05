---
title: Subprocess
---

# Subprocess
The subprocess module enable run shell command  

```{python, echo = FALSE, message = FALSE}
user_input = "-l"
out = subprocess.run(["ls", user_input])
if out.returncode == 0:
    print("was a success")
else:  
    print("was unsuccesful")
```

If you have sequence bash file, you can run the as below 

```{python, echo = FALSE, message = FALSE}
methodproc1 = subprocess.run(["process_one.sh"], stdout=subprocess.PIPE)
subprocess.run(["process_two.sh"], stdin=proc1.stdout)
```

Run execute and wait until it finish, if you want do other stuuf while the process running use `popen`, and you should call Popen.communicate() to pass and receive data to your process. i.e. subprocess.run() just wraps Popen and Popen.communicate(). 



instead run, one can Popen, which 

It can be done using `popen`

with Popen(["ls", user_input], stdout=PIPE) as proc: 
   out = proc.stdout.readlines()
   print(out)

for file in out:
    print(file.strip())



proc = subprocess.Popen(["ls", user_input], stdout=PIPE)
try:    
    out,err = proc.communicate(timeout=30)
except TimeoutExpired:
    proc.kill()  
    out,err= proc.communicate()


with Popen(["ls", "/a/bad/path"], stdout=PIPE, stderr=PIPE) as proc: 
     print(proc.stderr)
     print(proc.stdout)

with Popen(["ls"], stdout=PIPE, stderr=PIPE) as proc: 
     print(proc.stderr.readlines())
     print(proc.stdout.readlines())


the commenda must be as list, so if it is as a string, use split

import shlex
proc1="ls -l"
with Popen(shlex.split(proc1), stdout=PIPE, stderr=PIPE) as proc: 
     print(proc.stderr.readlines())
     print(proc.stdout.readlines())




 in other program, it is very useful for writting pipe lines, the follwoing function run an script written in R, without exiting Python.  

```{python, echo = FALSE, message = FALSE}
import subprocess
subprocess.check_call(['/usr/local/bin/Rscript', './Desktop/rtest.R'])
```
To save output of R in Python, run 
```{python, echo = FALSE, message = FALSE}
Out=subprocess.check_output(['/usr/local/bin/Rscript', './Desktop/rtest.R'])
```


import subprocess

try:
    subprocess.check_output("ls",shell=True)
except subprocess.CalledProcessError as e:
    print(e.output)