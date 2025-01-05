---
title: Challenges
---
# Challenge

### Challenge 1
Write a function to count the number of non-vowel in a string?  

<details><summary>Respond:</summary>
```{Python, echo = FALSE, message = FALSE}
def repit(x):
    num_nvow=num_vow=num_nodig=0
    for char in x: 
            if char in "aeiou":
                num_vow += 1
            elif char.isdigit():
                num_nodig += 1
            else:
                num_nvow +=1
    return(num_nvow,num_vow,num_nodig)
```
</details>

### Challenge 2
 [pi](https://en.wikipedia.org/wiki/Pi) can be estimated using using infinite series. Write a function to estimate it for a given en error.

### Challenge 3
Write a function to calculate the Euclidean distance
<details><summary>Respond:</summary>

```{Python, echo = FALSE, message = FALSE}
Exercise:  distance between two rows
def dis_col(ma,j1,j2):
 n=mat.shape
 d=0
 for i in range(n[0]):
   d+=(mat[i,j1]-mat[i,j2])**2
 return d**.5

def dis_euc(mat):
 n=mat.shape
 di=np.empty((n[1],n[1]))
 for i in range(n[1]):
   for j in range(n[1]):
    if i==j:
     di[i,j]=0
    elif i<j:
      di[i,j]=dis_col(mat,i,j)
    else:
      di[i,j]=di[j,i]      
 return di  

dis_euc(mat)
```

</details>

### Challenge 4
Write a function select a random number between 0 and 100, then you give you hints to find it.


### Challenge 5
Write an iterate function on dictionary.

<details><summary>Respond:</summary>

```{Python, echo = FALSE, message = FALSE}
# A generator expression
d={'Ryan':4,'Leila':65, 'Saeid':90 }
for i,j in d.items():
 print(i,'weight is',j)
```
</details>

### Challenge 6
Write a script to find the number of duplication of items. 

<details><summary>Respond:</summary>
```{python, echo = FALSE, message = FALSE}
x=(1,2,3,2,3,1,3,3)
rep={}
for i in range(1,len(x),1):
  if x[i] not in rep:
        rep[x[i]]=x.count(x[i])
```
</details>

### Challenge 7
Write factorial function 
<details><summary>Respond:</summary>
```{python, echo = FALSE, message = FALSE}
def factorial(n):
 if n==1:
    return 1
 if n<0:
     print(" your number is negative value")
 elif abs(int(n)-n)>0:
 # you can use not(isinstance(n,int))
    print("Not define")
 else:
    return n*factorial(n-1)
```
</details>

### Challenge 8
Write a function return the Fibonacci number

<details><summary>Respond:</summary>
```{python, echo = FALSE, message = FALSE}
def fib(n):
    if n==1:
      return  1
    elif n==2:
      return  1 
    else:
      return fib(n-1)+fib(n-2)

fib(4)

def fib1(n):
    if n==0 or n==1: 
    % if n in [0,1]: 
        return 1
    else:
        return fib1(n-1)+fib1(n-2)

print([fib1(i) for i in range(10)])

def fib2(i):
    a, b=0, 1
    for n in range(1,i+1):
        a,b=b, a+b
        return b

print([fib2(n) for n in range(10)])

def fib_helper(n):
    if n < 2:
        return n
    return fib_helper(n - 1) + fib_helper(n - 2)


def fib(n):
    return fib_helper(n)
```

</details>

### Challenge 9
Write a function get a string and a letter, and find the position of letter 

<details><summary>Respond:</summary>
```{python, echo = FALSE, message = FALSE} 
def find(word, letter):
    index=0
    while index <len(word):
        if word[index]==letter:
            print(index+1)
        index=index+1

word='a'
letter='saeid'
find('saeid','s')
```
</details>

### Challenge 10
The following is a list generated using for, rewrite it using a list comprehension
<details><summary>Respond:</summary>
```{python, echo = FALSE, message = FALSE}
x = []
for i in range(3):
    for j in range(2):
        x.append((i, j))
print(x)
```

```{python, echo = FALSE, message = FALSE}
x=[(i, j) for i in range(3) for j in range(2)]
```
</details>

### Challenge 11
Write a code to display the indices of elements in a list that satisfy a given criterion.
<details><summary>Respond:</summary>

```{python, echo = FALSE, message = FALSE}
x = [7,2,6,1,4,5,7,8,4]
low=3
up=8

[i for i in range(len(x)) if ((x[i]>low) & (x[i]<up))]
```
</details>

### Challenge 12
Explain what the following code does, then simplifies as a list comprehension.

<details><summary>Respond:</summary>
```{python, echo = FALSE, message = FALSE}
x_even = map(lambda x: x*x, filter(lambda x: x%2 == 0, range(10)))
print(list(x_even))
```

```{python, echo = FALSE, message = FALSE}
[x**2 for x in range(5) if x%2 == 0 ]
```
</details>

### Challenge 13
Write a comprehension, get a list and drop 1st, and 3th obs.

<details><summary>Respond:</summary>
```{python, echo = FALSE, message = FALSE}
obs=range(1,10)
[x for (i,x) in enumerate(obs) if i not in (0,2)]
```
</details>

### Challenge 14
Write a comprehension that select number that are divisible by 3 and 5 between 1 and 100

<details><summary>Respond:</summary>
```{python, echo = FALSE, message = FALSE}
obs=range(1,101)
[x for x in obs if x%3==0 and x%5==0]
```
</details>

### Challenge 15
Write a function find unique number. Hint: first sort it, then compare pairwisely and drop the duplicate.

<details><summary>Respond:</summary>
```{python, echo = FALSE, message = FALSE}
def sort0(x):
  x1=sorted(x)
  x_sorted=[x1[0]]
  for i in x1[1:]:
   if i!=x_sorted[-1]:
    x_sorted.append(i)
  return print("unique of ",x, "is", x_sorted)

obs=[1,4,1,4,2,2,1,4,2,5]
sort0(obs)
```
</details>

### Challenge 16
Using map and filter, write a function find cube of odd number between 1 and 20.

<details><summary>Respond:</summary>
```{python, echo = FALSE, message = FALSE}
x0=list(range(20))
list(map(lambda x: x**3,filter(lambda x: x/2!=0,x0)))
```
</details>


### Challenge 17
Drop the duplication from a list With a given list without changing the original order.

<details><summary>Respond:</summary>
```{Python, echo = FALSE, message = FALSE}
def remove_dub(x):
    clean0=[]
    seen0=set()    
    for i in x:
        if i in seen0: 
            next
        else :
            seen0.add(i); clean0.append(i)
    return (clean0)
```
</details>