---
title: OS
---
# OS
The module `os`  (`import os`) provides many useful functions to work with file and folders. The following provides the current working director

```python 
print(os.getcwd())
```

To change the directory use `os.chdir`: 

```python 
os.chdir('~/folder1')
print(os.getcwd())
```

To join paths, run the following. 
```python
base_path = '/home/ubuntu/'
filename = 'data.csv'
os.path.join(base_path, filename)
```

os.path.abspath(fullpath)

A list of useful function are presented in the below:  

|--|--|
|function | description |
|os.chdir():| Change the directory |
|os.getcwd(): | Get the current directery |
|os.listdir(): |Get a list of files and folders, os.listdir('.')|
|os.mkdir('test'): | make a new directory|
|os.rename('test','new_one'): |rename a directory  or file |
|os.remove('old.txt'):| remove file or directory |
|os.rmdir('old'): | if the directory is empty |
|os.path.exists(path):|	checks whether the given file or directory exists |
|os.path.isdir(path): |	checks whether the given path is a directory |
|os.path.isfile(path):|	checks whether the given path is a file |
|os.path.getsize(path):|	returns file size |
|os.path.dirname(path):|	returns path of folder containing file |
|os.path.expanduser('~'):|	returns path of the home directory |
|os.path.splitext(path) | return file extension|
|os.chmod(file,permission)| Change permission of a file|
|os.path.basename(path) |  Get file name without directory| 

The following code extract the extention of file Get file name without directory
```python 
fullpath = "/python/data.csv"
_, ext = os.path.splitext(fullpath)
ext
```

find all files that match a certain pattern in a directory tree.

``` python
import os, fnmatch
pattern = '*.py'

for path, subdirs, files in os.walk('.'):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                print(os.path.join(path, name))

```

One can can access to the environment variable using  `os.environ`, it is very useful to access user and key 
```python 
db_user = os.environ.get('DB_USER')
db_password = os.environ.get('DB_PASS')
print(db_user)
print(db_password)
```

## system
You can run bash command using `system` function: the following copy
README.md to copy.md. 
```python
 os.system('cp README.md copy.md')
```

```python
os.system("ls -l > result.txt")
```

## shutil
`shutil` provides more opertaions to work with files and folders. 
```python
from shutil import make_archive
make_archive("data.csv", "gztar", "/My Drive/python")
```

## pathlib
`pathlib` module do most of  'os'. 

```python
from pathlib import Path
path = Path("/usr/bin")
list(path.glob("*"))[0:2]
list(path.glob("*.csv"))
list(path.glob("**/*.csv"))
path.cwd()
path.exists()
path.as_posix()
```

## zip
To create a zip file
```py
import zipfile
z = zipfile.ZipFile('archive.zip', 'w')
z.write('testfile1.txt')
z.write('testfile2.txt')
z.close()
```

To see the content 
```py
z = zipfile.ZipFile('archive.zip')
print(z.namelist())
```

To extract all files. 
```
z.extractall('myfolder')
z.close()
```

To extract a specific file. 
```
z.extract(testfile1.txt','myfolder')
z.close()
```

