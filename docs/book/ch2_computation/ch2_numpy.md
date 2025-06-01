---
title: Numpy
---

#  Numpy
Numpy (NUMerical PYthon) provides very useful arrays structure to work with data. 

## Arrays
Numpy's array is a generalization of list discussed in [chapter1](/python-training-platform/book/ch1_primer/ch1_primer.md/), it is more appropriate for the computation.

```{Python, echo = FALSE, message = FALSE}
import numpy as np
weight=[58,89,68,74,62,77,65,65]
weight
weight_arr=np.array(weight)
weight_arr
```

It is like a vector, all elements should have same type, therefore if you add a strict  element, it saves all elements as strict. It also accept multi lists

```{Python, echo = FALSE, message = FALSE}
arr1=np.array([range(i) for i in [1, 2, 3]])
arr1[1]
arr1[1][0]
arr2=np.array([range(i, j+i) for i in [1, 2, 3] for j in [1, 2, 3]])
arr2[1]
arr2[1][0]
```

A constant array can be generated using ```np.full(,) ```

```{Python, echo = FALSE, message = FALSE}
np.full(2, 2.2)
np.full((2,1), 2.2)
np.full((2,2), 2.2)
```

```{Python, echo = FALSE, message = FALSE}
np.repeat(2.2, 2)
np.repeat([2.1,2.2],2)
np.repeat([2.1,2.2], [2, 3])
```

```{Python, echo = FALSE, message = FALSE}
np.arange(1,14,4)
np.arange(21,30,3)
np.arange(2,1,-0.1)
```

To create an array of n values between two values

```{Python, echo = FALSE, message = FALSE}
np.linspace(0, 1, 10)
```

To refer elements of array should use ```[]```

```{Python, echo = FALSE, message = FALSE}
weight[1]# first element
weight[2:]# second elements to the rest
weight[:3]# elements before the third and including the third
```

To refer elements of multi array should use ```[,]```

```{Python, echo = FALSE, message = FALSE}
weight2=np.array([weight_arr,2.20*weight_arr,35.27*weight_arr])
weight2[1,1]
weight2[1:,1:]
weight2[1:,2:]
```

To change the shape
```
weight2.reshape((8, 3))
```

## concatenate
It provides functions to concatenate the arrays

```{Python, echo = FALSE, message = FALSE}
>>> w1 = weight_arr[:4]
>>> w2 = weight_arr[4:]
>>> np.concatenate((w1, w2), axis=0)
array([58, 89, 68, 74, 62, 77, 65, 65])
>>> w1r=w1.reshape(2,2)
>>> w2r=w2.reshape(2,2)
>>> np.concatenate((w1r,w2r), axis=0)
array([[58, 89],
       [68, 74],
       [62, 77],
       [65, 65]])
>>> np.vstack((w1r,w2r))
array([[58, 89],
       [68, 74],
       [62, 77],
       [65, 65]])
>>> np.concatenate((w1r,w2r), axis=1)
array([[58, 89, 62, 77],
       [68, 74, 65, 65]])
>>> np.hstack((w1r,w2r))
array([[58, 89, 62, 77],
       [68, 74, 65, 65]])
```

The array can be split into subsplit

```{Python, echo = FALSE, message = FALSE}
w1, w2, w3,w3,w4 = np.split(weight_arr, 4)
```

## Useful function
Numpy provides very useful bult-in function,  

```{Python, echo = FALSE, message = FALSE}
np.sort(weight2,axis=0)
np.sort(weight2,axis=1)
>>> np.argsort(weight2,axis=0)
array([[0, 0, 0, 0, 0, 0, 0, 0],
       [1, 1, 1, 1, 1, 1, 1, 1],
       [2, 2, 2, 2, 2, 2, 2, 2]])
>>> np.argsort(weight2,axis=1)
array([[0, 4, 6, 7, 2, 3, 5, 1],
       [0, 4, 6, 7, 2, 3, 5, 1],
       [0, 4, 6, 7, 2, 3, 5, 1]])
```       

```{Python, echo = FALSE, message = FALSE}
>>> np.min(weight2)
58.0
>>> np.min(weight2,axis=1)
array([   58.  ,   127.6 ,  2045.66])
>>> np.min(weight2,axis=0)
array([ 58.,  89.,  68.,  74.,  62.,  77.,  65.,  65.])
```

The following list includes some useful functions:  

Function Name| NaN-safe Version|	Description
--- | --- | ---
np.sum	|np.nansum|	Compute sum of elements
np.prod|	np.nanprod|	Compute product of elements
np.mean|	np.nanmean	|Compute mean of elements
np.std	|np.nanstd	|Compute standard deviation
np.var|	np.nanvar|	Compute variance
np.min|	np.nanmin|	Find minimum value
np.max	|np.nanmax|	Find maximum value
np.argmin	|np.nanargmin	|Find index of minimum value
np.argmax	|np.nanargmax	|Find index of maximum value
np.median	|np.nanmedian|	Compute median of elements
np.percentile	 |np.nanpercentile	|Compute rank-based statistics of elements
np.any|	N/A	Evaluate |whether any elements are true
np.all |	N/A	Evaluate |whether all elements are true


The ```isnan``` is useful command to study if the object includes the NA or not.

```{Python, echo = FALSE, message = FALSE}
>>> y=np.array([1, 2, np.nan])
>>> np.isnan(y)
array([False, False,  True], dtype=bool)
```

## Matrix 
Numpy has very strong functions for matrices. 

```{Python, echo = FALSE, message = FALSE}
mat=np.array([i for i in range(9)]).reshape(3,3)
mat.diagonal()
np.diagonal(mat)
mat.trace()
np.trace(mat)
mat.transpose() # transpose
np.transpose(mat)
mat2=np.array([i for i in range(6)]).reshape(3,2)
np.dot(mat,mat2) # dot product 
np.inner(mat,mat) # inner product 
```

More matrical functions can be obtained from  Linear algebra, ```numpy.linalg```, 
```{Python, echo = FALSE, message = FALSE}
a=np.array([[1,2],[3,4]])
np.linalg.inv(a) # inverse
np.linalg.pinv(a) # inverse
np.linalg.det(a)
```
```{Python, echo = FALSE, message = FALSE}
y = np.array([[5.], [7.]])
np.linalg.solve(a, y)
np.linalg.eig(a)
```

Instead generating matrix from array, numpy has ```numpy.matlib``` that directly can be used to generate matrix 

```{Python, echo = FALSE, message = FALSE}
import numpy.matlib as npmat
np.eye(3)
np.zeros((4,2))
np.ones((4,2))
```

Calculate the beta 
XTX = np.dot(X.T, X)
INV = np.linalg.inv(XTX)
beta = np.dot(np.matmul(INV, X.T), y)
beta

## Random number
Numpy has very strong function for generating random number from several statistical distributions. 

```{Python, echo = FALSE, message = FALSE}
np.random.rand(4,2) #Generate n random number from uniform

np.random.randn(4,2) #Generate n random number from standard normal

np.random.randint(low=1,high=20, size=10)

x = np.arange(12).reshape((4 ,3))
np.random.shuffle(x)

a0=['a','b']
a0=np.array(a0)
np.random.choice(a0,size=3, replace=True,p=(.3,.7))
```

## Subsetting
The logical operator is often used to extract subset of
data, using the array can easily achieve selecting subsets.    


```{Python, echo = FALSE, message = FALSE}
>>> x= np.array(["a", "b", "c"])
>>> y= np.array([3, 4, "c"])
>>> set(x).union(y) # union
{'c', '4', 'b', '3', 'a'}
>>> set(x).intersection(y)
{'c'}
>>> set(x)- set(y)
{'b', 'a'}
>>> [x[i]==y[i] for i in  range(len(x))]# the same as is.ellemt in R
[False, False, True]
```


```{Python, echo = FALSE, message = FALSE}
>>> weight=[58,89,68,74,62,77,65,65]
>>> weight=np.array(weight)
>>> weight<74
array([ True, False,  True, False,  True, False,  True,True], dtype=bool)
>>> (weight<74) & (weight==89)
array([False, False, False, False, False, False, False, False], dtype=bool)
>>> weight[(weight<74) & (weight==89)]
array([], dtype=int64)
>>> weight[(weight<74) & (weight==62)]
array([62])
>>> weight[(weight<74) | (weight==62)]
array([58, 68, 62, 65, 65])
>>> weight[~(weight<74) & (weight==62)]
array([], dtype=int64)
>>> weight[~((weight<74) | (weight==62))]
array([89, 74, 77])
```


```{Python, echo = FALSE, message = FALSE}
>>>weight2=np.array([weight_arr,2.20*weight_arr,35.27*weight_arr])
>>> np.sum(weight2 < 127, axis=1)
array([8, 0, 0])
>>> np.any(weight2 < 127)
True
>>> np.sum(weight2 < 127, axis=1)
array([8, 0, 0])
```


## Combined data
The data set might include different data like dataframe in R that each column has data with different format, array can save such data.

```{Python, echo = FALSE, message = FALSE}
>>>weight=[58,89,68,74,62,77,65,65]
>>>gender=['F','F','F','M','M','M','M','M']
>>> data = np.zeros(8, dtype={'names':('sex', 'weight'),'formats':('U10', 'f4')})
>>> data['sex']=gender
>>> data['weight']=weight
>>> data
array([('F',  58.), ('F',  89.), ('F',  68.), ('M',  74.), ('M',  62.),
       ('M',  77.), ('M',  65.), ('M',  65.)],
      dtype=[('sex', '<U10'), ('weight', '<f4')])

>>> data['weight']
array([ 58.,  89.,  68.,  74.,  62.,  77.,  65.,  65.], dtype=float32)
>>> data['weight'][1:3]
array([ 89.,  68.], dtype=float32)     
```

When you define the array, you should define the format as well, data can be save with different format see, ?????

Character|Description|	Example
--- | --- | ---
'b'	|Byte|	np.dtype('b')
'i'	|Signed integer|	np.dtype('i4') == np.int32
'u'	|Unsigned| integer	|np.dtype('u1') == np.uint8
'f'	|Floating point	|np.dtype('f8') == np.int64
'c'	|Complex floating point|	np.dtype('c16') == np.complex128
'S', 'a'|	String	|np.dtype('S5')
'U'	|Unicode string|	np.dtype('U') == np.str_
'V'	|Raw data (void)	|np.dtype('V') == np.void

## masked array
There are many circumstances where one should drop part of it, because of missing, invalid entries, or other reasons. 
Consider the weight and mask weight<70, 

```{Python, echo = FALSE, message = FALSE}
weight_arr=np.array(weight)
weight_m=np.array(np.zeros(len(weight)))
weight_m[weight_arr<70]=1
weight_ma1=np.ma.masked_array(weight_arr, mask=weight_m)
weight_ma1.data
weight_ma1.mask
np.mean(weight_ma1)
````

```{Python, echo = FALSE, message = FALSE}
weight_ma2=np.ma.masked_where(weight_arr<70,weight_arr)
weight_ma2
np.mean(weight_ma1)
```

```{Python, echo = FALSE, message = FALSE}
weight_arr=np.array(weight)
weight_mas=np.ma.masked_where(weight_arr<70,weight_arr)
weight_mas
weight_mas.data
weight_mas.mask

np.ma.masked_array(weight_arr, mask=aa)
```
