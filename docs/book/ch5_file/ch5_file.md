---
title: Text files
---
# Text files
Python has strong function to work with file and folders.  

## open
Open has three step; open, read\write, and close file.

The following code, if there is a file, overwrite it otherwise creates the file and add text to it. 
```python
test = open("example.txt", "w")
for i in range(0,10):
    test.write(f"add {i}\n")
test.close()  
```

The entire file can be seen using the following files. 
```python
test = open("example.txt", "r")
print(test.read())
test.close()
```

To append new line use `a`
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


```python
with open("example.txt", "r") as handle:
    for line in handle:
        print(line.strip())

with open("example.txt", "r") as handle:
    print(handle.read())

handle = open("example.txt", "r")
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

The entire file can be read in a file 
```python
f = open('example.txt')
text = f.read()
```

If the file in not in the directory folder, you can recall it 
``` python
import os
p = os.path.join('/home/ubuntu', 'data.csv')

with open(p) as fp:
    data = fp.read()
```

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




## Online file 
A simple way to access to a file online is to use `urllib` 
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


## table
If the data is saved as table, use `pd.read_table`, 
```python
users = pd.read_table('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user', sep='|', index_col='user_id')
users.head()
```

`
## zip file 

```{Python, echo = FALSE, message = FALSE}
import gzip
handle = gzip.open("example_data.fastq.gz", 'rt')
l = next(handle)
print(l)
handle.close()
```

