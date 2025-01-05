---
title: pickle module
---
# Storing objects
One of the best ways to store objects in Python is by using the pickle module. [Pickle](https://docs.python.org/3/library/pickle.html#data-stream-format) is primarily used for serializing and deserializing Python object structures. In simpler terms, it converts a Python object into a byte stream, embedding all the information needed to reconstruct/unpack the object later in our code. This enables the object to be stored in a file, easily transported, and restored later. It can be loaded using `import pickle`.

## Pickle dump
`pickle.dump()` function allow user to stor the the objects. Let create different objects, and store them. 

```python
weights=[20,15,19,21,16]
colors=('red','blue','green','black','white')
colors_set={'red','blue','green','black','white'}
prices = {'BMW': 50,'BENZ': 55,'Ford': 25,'Chevy': 30, 'GM': 28}

import pickle

file = open('backup.pkl','wb')
pickle.dump(weights, file)
pickle.dump(colors, file)
pickle.dump(colors_set, file)
pickle.dump(prices, file)
file.close()

```

## Pickle load
`pickle.load()` is used to retrieve pickled data. 
```python
file = open('backup.pkl','wb')
weights=pickle.load(file)
colors=pickle.load(file)
colors_set=pickle.load(file)
prices=pickle.load(file)
file.close()
```
