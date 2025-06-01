---
title: Text files
---
# Text files
Python has strong function to work with file and folders.  

##  Manipulating
To access a text file in Python, you need to: 1) open the file, 2) read\write it, and 3) close the file.
### Write
The following code creates a new file and writes text to it; if the file already exists, it will be overwritten
```python
test = open("example.txt", "w")
for i in range(0,10):
    test.write(f"add {i}\n")
test.close()  
```
As you can see here we use 'w' mode, which means Write-only. Overwrites file if it exists; creates new if it doesn’t. 


Lines can be added easily to file.  
```python
lines = ['first line\n', 'second line\n']
open('my_file.txt','w').writelines(lines)
```

Table can be added to file as below: 
```python
names = ['Emily', 'Bob', 'Charlie']
ages = [23, 45, 67]

f = open('my_file.txt', 'w')
for name, age in zip(names, ages):
    line = f'{name};{age}\n'
    f.write(line)
f.close()
```

### Append
To append new line use `a` mode, you can use  `.write()` or `writelines()`: 
```python
test = open("example.txt", "a")  # append mode
test.write("Today \n")
test.close()
```

```python
test = open("example.txt", "a")
L = ["This is just example Delhi \n", "in Python \n"]
test.writelines(L) 
test.close()
```

### Read
The entire file can be viewed using the following code; as you can see, we use the 'r' mode.
```python
test = open("example.txt", "r")
print(test.read())
test.close()
```

The entire file can be read in a file 
```python
f = open('example.txt')
text = f.read()
f.close()
```

You can access each line of the file element by element as follows:

```python
with open("example.txt", "r") as handle:
    for line in handle:
        print(line.strip())

with open("example.txt", "r") as handle:
    print(handle.read())
```
In Python, the next() function is used to retrieve the next item from an iterator.

```python
handle = open("example.txt", "r")
line = next(handle)
print(line)    
line = next(handle)
print(line)    
```

If the columns are separated using ;, the file can be separated as 
``` python
for line in open('my_file.txt'):
    columns = line.strip().split(';')
    first = columns[0]
    last = columns[1]
    age = int(columns[2])
```

If the file in not in the directory folder, you can recall it 
``` python
import os
p = os.path.join('/home/ubuntu', 'data.csv')

with open(p) as fp:
    data = fp.read()
```




## Online file 
A simple way to access to a file online is to use `urllib` module, 

```{Python, echo = FALSE, message = FALSE}
import urllib.request
url = "https://raw.githubusercontent.com/ucdavis-bioinformatics-training/2020-Bioinformatics_Prerequisites_Workshop/master/Intro_to_Python/example_data.fastq.gz"
urllib.request.urlretrieve(url, 'example_data.fastq.gz')
```

```{Python, echo = FALSE, message = FALSE}
import os
# to check whether file is in the working path
os.path.isfile("example_data.fastq.gz")
# to check the size of file
os.path.getsize("example_data.fastq.gz")
```

## zip file 
To handle the zip file, use the gzip module, as shown below.
```{Python, echo = FALSE, message = FALSE}
import gzip
handle = gzip.open("example_data.fastq.gz", 'rt')
l = next(handle)
print(l)
handle.close()
```


## table
If the data is saved as table, use `pd.read_table`, 
```python
users = pd.read_table('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user', sep='|', index_col='user_id')
users.head()
```
