---
title: itertor
---

# Itertor
## itertools
itertools provides several functions for efficient iteration. Below is an example of how to use it to generate combinations and permutations:

```python
from itertools  import combinations
list(combinations([1,2,3], r=2))
print([list(c) for c in combinations([1,2,3], r=2)])

from itertools  import permutations
list(permutations('abc'))
print([''.join(p) for p in permutations('abc')])
```

As an exercise, let's write an example that generates the permutations and combinations of the numbers 1 to 6, and then selects those whose elements sum to 9.

```python
import itertools as it

my_list = [1,2,3,4,5,6]
comb = combinations(my_list, 3)
perm = permutations(my_list, 3)

[result for result in comb if sum(result) == 9]
[result for result in perm if sum(result) == 9]
```

### groupby
Let's look at groupby, which groups consecutive items. In the example below, we group animals based on the length of their names.

```python
from itertools  import groupby
animals = sorted(['pig', 'cow', 'giraffe', 'dolphin','dog', 'cat', 'lamma', 'lion', 'tiger'], key=len)
for k, g in groupby(animals, key=len):
    print(k, list(g))

```

Always sort the data before using groupby, otherwise unexpected results may occur. Now, let's group the animals.

```python
animals = ['pig', 'cow', 'giraffe', 'dolphin','dog', 'cat', 'lamma', 'lion', 'tiger']
animals.sort(key=lambda x: x[0])  # Sort by first letter

for k, g in groupby(animals, key=lambda x: x[0]):
    print(k, list(g))
```



### Concatenate lists:
You can use `chain` to combine multiple iterables into a single continuous sequence.

```python
from itertools import chain

ch = itertools.chain([1, 2], [3, 4])
print(list(ch))
```

### repeat
You can use repeat to repeat a single value multiple times:

```python
from itertools import repeat
print(list(repeat([1, 2], 3)))
```

You can repeat a value infinitely by omitting the repeat count, 

```python
from itertools import repeat
for i, item in enumerate(repeat([1, 2])):
    print(item)
    if i == 6:
        break
```



## Generator
A simple way to create an iterator is by using a generator, which yields items one at a time instead of storing the entire sequence in memory.

``` python 
def gen(n):
    print('first one')
    yield n+1
    print('second one')
    yield n+2
    print('third one')
    yield n+3

a = gen(0)
next(a)
next(a)
next(a)
```

We often use yield inside a while loop to create generators that produce values until a condition is met.

``` python
def gen2(n):
    count = 1
    while count <= n:
        yield count
        count += 1

a = gen(0)
next(a)
next(a)
next(a)

b = gen2(5)
for i in a:
    print(i)
```