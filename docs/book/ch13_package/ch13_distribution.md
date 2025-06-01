---
title: Distribution
---

Here we present the most basic technique to share, for more information look  at [Python Packaging User Guide](https://packaging.python.org).

## setup.py file
In the first step, create `setup.py` file to the top-level of your project: 


```python
# setup.py
import setuptools

setuptools.setup(
    name="mypachage",
    version="0.0.1",
    author="Saeid Amiri",
    author_email="saeid.amiri1@gmail.com",
    description="Training course on python",
    packages=setuptools.find_packages(),
)
```

Create `requirements.txt` and put the necessary package there. Now you can install the package

```python
python3.10 -m pip install ./docs/comp/mypachage
```


If you want to share the source as a ZIP archive, run the command below. It will create a `dist/` directory and store a `.tar.gz` file there.
```python
cd ./docs/comp/mypachage
python3.10 setup.py sdist
```

You can use it to install the package.

```python
python3.10 -m pip install mypachage-0.0.1.tar.gz
```


## Github 
You can share the source on GitHub and share it with others. To install from GitHub, you only need the repository's path.

```python
pip install 'git+https://github.com/saeidamiri1/mypachage'
```

If you want to import a module instead of the entire package, you can do so by.

```python
import urllib.request
url = 'https://raw.githubusercontent.com/saeidamiri1/ESLR/master/PythonCode/ESRL.py'
contents = urllib.request.urlopen(url).read()
exec(contents)
```
