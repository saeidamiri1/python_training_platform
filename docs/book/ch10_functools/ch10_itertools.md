# itertools
functools  provides several function for iterations.

```{python, echo = FALSE, message = FALSE}
from itertools  import combinations, permutations,groupby,islice, cycle 
list(combinations([1,2,3], r=2))
print([list(c) for c in combinations([1,2,3], r=2)])

list(permutations('abc'))
print([''.join(p) for p in permutations('abc')])


animals = sorted(['pig', 'cow', 'giraffe', 'elephant','dog', 'cat', 'hippo', 'lion', 'tiger'], key=len)
for k, g in groupby(animals, key=len):
    print(k, list(g))

list(islice(cycle('abcd'), 2, 10))    
```



import itertools as it

my_list = [1,2,3,4,5,6]

combinations = it.combinations(my_list, 3)
permutations = it.permutations(my_list, 3)

[result for result in combinations if sum(result) == 10]

word = 'sample'
my_letters = 'plmeas'

combinations = it.combinations(my_letters, 6)
permutations = it.permutations(my_letters, 6)

for p in permutations:
    # print p
    if ''.join(p) == word:
        print ('Match!')
        break
    else:
        print ('No Match!')



def get_state(person):
    return person['state']

people = [
    {
        'name': 'John Doe',
        'city': 'Gotham',
        'state': 'NY'
    },
    {
        'name': 'Jane Doe',
        'city': 'Kings Landing',
        'state': 'NY'
    },
    {
        'name': 'Corey Schafer',
        'city': 'Boulder',
        'state': 'CO'
    },
    {
        'name': 'Al Einstein',
        'city': 'Denver',
        'state': 'CO'
    },
    {
        'name': 'John Henry',
        'city': 'Hinton',
        'state': 'WV'
    },
    {
        'name': 'Randy Moss',
        'city': 'Rand',
        'state': 'WV'
    },
    {
        'name': 'Nicole K',
        'city': 'Asheville',
        'state': 'NC'
    },
    {
        'name': 'Jim Doe',
        'city': 'Charlotte',
        'state': 'NC'
    },
    {
        'name': 'Jane Taylor',
        'city': 'Faketown',
        'state': 'NC'
    }
]

person_group = it.groupby(people, get_state)

copy1, copy2 = it.tee(person_group)

for key, group in person_group:
    print(key, len(list(group)))
    # for person in group:
    #     print(person)
    # print()





# Concatenate lists:

import itertools

ch = itertools.chain([1, 2], [3, 4])
print(list(ch))

print(list(itertools.repeat([1, 2], 3)))


# Permutations and combinations of list elements:

p = itertools.permutations([1, 2, 3])
print(list(p))

c = itertools.combinations([1, 2, 3], 2)
print(list(c))
