---
date: 2024-10-26
title: Data-frame
description:  Data-frame
categories:
  - Panda
authors:
  - saeidamiri1
---

# Data-frame
Data-frame via pandas is very useful format for working with dataset, its structure is two-dimensional size-mutable, potentially heterogeneous
tabular data structure with labeled axes (rows and columns). The following codes create a data-frame from a dictionary.  

<!-- more -->

```
var={"A": [1,2,0], "B": [2,3,4]}
df= pd.DataFrame(data=var,index=['A', 'Z', 'C'])
```

The label column can be easily changed:
```
raw_data = {'population': [ 1015.0, 1129.0, 333.0,  515.0],'median_income': [ 1.5, 1.8,  1.7,  3.2]}
df=pd.DataFrame(raw_data, columns = ['population', 'median_income'])
```

In some circumstances, it is better to consider the time of collecting data as index, the following script changes the data format to the time format and save it as index.  
```
df = df.set_index(pd.to_datetime(['2019-04-01','2019-05-04','2019-06-01','2019-07-02']))
```

To create an empty data-frame, run the following
```
df1=pd.DataFrame(columns = ['population', 'median_income'])
df2=pd.DataFrame()
```

Dimension of data-frame is 2 which can be seen via ```.ndim ```, the number of rows and columns can be obtained using   ```.shape```.  

```
df.ndim
df.shape
df.shape[0]
df.shape[1]
```
