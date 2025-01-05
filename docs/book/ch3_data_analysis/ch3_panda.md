---
title: Panda
---

# Pandas
## Introduction
Pandas is built on top of NumPy, and its functions are highly useful for working with datasets. The shorthand for importing this library is:
```
import pandas as pd
```

## Data-frame
A DataFrame in Pandas is a highly useful format for working with datasets. It is a two-dimensional, size-mutable, and potentially heterogeneous tabular data structure with labeled axes (rows and columns). The following code demonstrates how to create a DataFrame from a dictionary:

```py
var={"A": [1,2,0], "B": [2,3,4]}
df= pd.DataFrame(data=var,index=['A', 'Z', 'C'])
```
One can reorder the index, 

```py
df1= df.reindex(['A','C','Z'])
print(df1)
```

The column labels can be easily modified:
```py
raw_data = {'population': [ 1015.0, 1129.0, 333.0,  515.0],'median_income': [ 1.5, 1.8,  1.7,  3.2]}
df=pd.DataFrame(raw_data, columns = ['population', 'median_income'])
```

In certain situations, it is beneficial to use the data collection time as the index. The following script converts the data to a datetime format and sets it as the index: 
```py
df = df.set_index(pd.to_datetime(['2019-04-01','2019-05-04','2019-06-01','2019-07-02']))
```

Always use `to_datetime` to ensure the data is stored in a proper datetime format. This allows easy conversion to specific components such as year, weekday, and more.

```py
df1['date'] = pd.to_datetime(['2019-04-01','2019-05-04','2019-06-01','2019-07-02'])
df1['date'].dt.weekday
df1['date'].dt.year
```

To create an empty DataFrame, use the following code:
```py
df1=pd.DataFrame(columns = ['population', 'median_income'])
df2=pd.DataFrame()
```

## Adding new column
A column can be easily added to a DataFrame:

```py
df0=pd.DataFrame([38,40,25,33])
df['Ave_hour']=df0
```

The ```assign()``` method can also be used to add new columns to a DataFrame. Additionally, new columns can be created using functions, as shown below:

```py
df=df.assign(Ave_hour=df0)
df=df.assign(PI1=lambda x: x['population']*x['median_income'],PI2=df['population']/df['median_income'] )
```


A column's name can be renamed using the rename() method, as shown below:
```py
df.columns=['population1','median_income','Ave_hour','PI1','PI2']
df=df.rename(columns={'population1': 'pop', 'median_income': 'med_income'},inplace=True)
```

## Apply function on row or column
Using ```df.apply(fun)``` allows you to apply a function to either columns or rows of a DataFrame. Here's an example:

```py
df.apply(np.sum, axis=0)
df.apply(np.sum, axis=1)
```

You can even apply a function to specific columns or rows.

```py
df.apply(lambda x: x['A'] * x['B'], axis=1)
df['productcolmn']=df.apply(lambda x: x['A'] * x['B'], axis=1)


def majority(x):
    if x > 17:
        return True
    else:
        return False

stud_alcoh['legal_drinker'] = stud_alcoh['age'].apply(majority)
```


## Loading CSV data
The function ```pd.read_csv``` is used to import data saved in CSV format. The following example demonstrates how to import a CSV file into Python, with the data being the California housing dataset:

``` py
source ="https://storage.googleapis.com/mledu-datasets/california_housing_train.csv"
CHT = pd.read_csv(source, sep=",")
CHT.head()
```

## Loading big CSV data
If the data is very large, you may need to split it into chunks and perform computations on each chunk.

``` py
chunk_size=100
chunk=[]
for chunk in pd.read_csv('file.csv',chunksize=chunk_size):
   do computation
  chunks.append(chunk)
df = pd.concat(chunks, axis=0)
```

## Generating summary
To view the data types, summary statistics, and general information about the variables in a DataFrame, use ```.dtypes```,  ```.describe()```, and   ```.info()```.

```py
# show the type of variables
CHT.dtypes
# generate summary
CHT.describe()
CHT.info()
```

It is easy to identify and remove duplicates in a DataFrame.
```py
CHT.duplicated()
CHT.drop_duplicates()
```

To check for duplicates in specific columns, specify their names as well.
```py
CHT.duplicated(['longitude'])
CHT.drop_duplicates(['longitude'], keep='last')
CHT.index.duplicated()
```

To truncate the display of data, you can adjust the display options using `pd.set_option()`
```py
pd.set_option('display.max_rows', 50)
pd.set_option('precision', 4)
```

## Data type 
Pandas has different data types;  object (a mix of different type of data), int64 ( interger numbers), float64(floating-point numbers), bool(True/False values), datetime64(Date and time values), category(a finite number of possible values). The following codes show how to define the data type. 

```py
raw_data = {'population': [ 1015.0, 1129.0, 333.0,  515.0],'median_income': [ 1.5, 1.8,  1.7,  3.2], 'class_income': ['low', 'low',  'low',  'high'], 'time':['2019-04-01','2019-05-04','2019-06-01','2019-07-02']}
df=pd.DataFrame(raw_data, columns = ['population', 'median_income','class_income','time'])
df.dtypes
df['population']=df['population'].astype('int64')
df['median_income']=df['median_income'].astype('float64')
df['class_income']=df['class_income'].astype(CategoricalDtype(categories=['low', 'high'], ordered=True))
df['time']=df['time'].astype('datetime64')
df.dtypes
```

## Size of data-frame
The dimension of a DataFrame is 2, which can be accessed using `.ndim`. The number of rows and columns can be obtained with `.shape`.

```py
CHT.ndim
CHT.shape
CHT.shape[0]
CHT.shape[1]
```

## Preview
Beside the function `print`, Pandas can show the first and the last part of data, using ```.head()``` and `.tail()`. 
By passing a number in the parenthesis, one can specify the output.

```py
CHT.head(10)
CHT.tail(10)
CHT.sort_values(by='housing_median_age', ascending=False).head(3)
CHT.columns
```

## Manipulating data-frame
### Subset of Data
To select the data use the name of variable, or specify the indices via `.iloc` and `.loc` (link)[http://pandas.pydata.org/pandas-docs/version/0.22/indexing.html]. `.iloc` is an integer-based and select should use integer index. On contrary, `.loc`   is primarily label based, and may also be used with a boolean array.

```py
CHT.longitude
CHT['longitude']
CHT.iloc[:,1]
CHT.iloc[:,[1,3,4]]
CHT.iloc[:,np.r_[1,3:6]]
```

To select part of row, you can also use `iloc[index of row,:]`, also the rows can be selected using the logical values
```py
CHT.iloc[2:10]
CHT.iloc[2:10,:]
CHT[CHT.iloc[:,1]<34]
```

To retieve part of row, should pass boolean variable, ```.iloc``` does not work boolean variable, and ```.loc``` should be used.  Consider the median_income in our data, by using quartile divid it into three categories.
```py
CHT['famlev'] = ''
C1=CHT.median_income<=CHT.median_income.quantile(.3)
C2=CHT.median_income>=CHT.median_income.quantile(.7)
CHT.loc[C1,'famlev']='L'
CHT.loc[~C1&~C2,'famlev']='M'
CHT.loc[C2,'famlev']='H'
```
Obviously, we can use `&` to bring the `~C1` and `~C2` together. In this case we used `.loc`, obviously we specify column labels to retrieve columns instead of by position.

Note: You can also using [][] apply different conditions on data.  
```py
CHT['median_house_value'][CHT['famlev'] == 'M'].mean()
```

Selecting or searching can be done also using ```np.where``` which evaluate the condition 
```py
CHT_R=CHT[['total_rooms','total_bedrooms']]
CHT_R.where(CHT.total_rooms<1000)
CHT_R.where(CHT.total_rooms<1000,0)
con= CHT_R<1000
CHT_R.where(con, -999)

CHT.idxmin()
CHT.idxmax()
```

Opposite of this `np.where` is `np.mask`, replace it with `np.where` and rerun the codes. 
To drop row and columns use ```.drop```. The ```np.where``` can be used to create a new  column, 
```py
CHT['size']=np.where(CHT.total_rooms<1000, 'small', 'big')
CHT_R=CHT[['total_rooms','total_bedrooms']]
CHT_R.where(CHT.total_rooms<1000)
CHT_R.where(CHT.total_rooms<1000,0)
con= CHT_R<1000
CHT_R.where(con, -999)
```

Find which ones are 'M'
```py
np.where(CHT.loc[:,'famlev'].isin(['M']))
```

`isin` lets you select data whose value "is in" a list of values.
```py
CHT.drop([0,5], axis=0)
CHT.drop('longitude',axis=1, inplace=True)
```

```py
CHT[CHT['size'].str.startswith('b')]
CHT.iloc[: , :-3]
CHT.loc[CHT['size'].isin(['big'])]
```

To replace values, use `df.replace()`

```py
CHT['famlev'].replace('L','Low').replace('M','Middle').replace('H','High')
CHT.drop('longitude',axis=1, inplace=True)
```

Note: the argument ```inplace=True``` apply the change on the original data. To transpose dataframe, run `CHT.T`. To change the  type of column apply `astype(np.int)` on them
```py
CHT.total_rooms.astype(np.int)
```

One can take a random subset of data using 
```py
CHT.sample(4)
```


To delete the columdn, use `del`:
```py
del CHT['famlev']
```

### eval
You can evaluate a Python expression before using it, 


```py
var={"A": [1,2,0], "B": [2,3,4], "C":['A', 'Z', 'C']}
df= pd.DataFrame(data=var)
pd.eval('df.A + df.B')
```

```py
df.eval('D = A + B')
df
```

```py
df.eval('D = A + B', inplace=True)
df
```

Evaluate a Python expression as a string using various backends.

### Select row using query
`query` can be used to to select row, the following code 
Selecting or searching can be done also using ```np.where``` which evaluate the condition 
```py
CHT[CHT.total_rooms<1000)
```

```py
CHT.query('total_rooms<1000')
```

To use a variable inn a panda query use `@`, 
```py
total=1000
CHT.query('total_rooms< @total')
```

You can use f-string to not use `@`:
```py
total=1000
CHT.query(f'total_rooms< {total}')
```




### Select based on data types
`df.select_dtypes([])` return  columns that has a specic type. 
``` py
df.select_dtypes(include='int')
df.select_dtypes(include='bool')
df.select_dtypes(include=['float64'])
```

### delete row or column
```py
CHT.drop([0,2]) # drop first and third rows
CHT.drop(columns=['famlev']) #
CHT.drop(CHT.columns[[0,2]], axis = 1) # drop the first and third column
```

### Combining columns
Columns can easily combine to create a new column

``` py
CHT['famsize']=CHT['famlev']+'-'+CHT['size']
```

### repeat
It is possible to repeat the element in data frame,   

```py
df1 = pd.DataFrame([[1, 2], [3, 4], ['a', 'b']], columns=["A", "B"])
df2 = pd.DataFrame([[5, 6], [7, 8]], columns=["c", "d"])
ab=pd.DataFrame(np.repeat(df1.values, 2, axis=0), columns=df1.columns) # repeat column in sequence
ac=df2.iloc[np.tile(np.arange(len(df2)), len(df1))].reset_index(drop = True) # repeat in total
```

### list comprehension
Simple operation using the list comprehension can be done on data-frame as well.
```py
CHT['size']=['small' if x<100  else 'big'  for x in CHT['total_rooms']]
```

### Summarising
Although `.describe` can give a summary of variables,  more specific summery of variables (columns) can be extracted, see

```py
CHT.count
CHT[CHT.iloc[:,1]<34].nunique()
```

The following table includes the functions.

|Function|Description|
|---|---|
`count`|	Number of non-null observations
`sum`	 | Sum of values
`mean`	|Mean of value
`mad` |	Mean absolute deviation
`median`|	median of values
`min`	 |Minimum
`max`	 |Maximum
`mode`	|Mode
`abs`	| Absolute Value
`prod`	| Product of values
`std`	 |Unbiased standard deviation
`var`	 |Unbiased variance
`sem`	 |Unbiased standard error of the mean
`skew`	| Unbiased skewness (3rd moment)
`kurt`	| Unbiased kurtosis (4th moment)
`quantile`	| Sample quantile (value at %)
`cumsum`	| Cumulative sum
`cumprod`| 	Cumulative product
`cummax`	| Cumulative maximum
`cummin`	| Cumulative minimum
`nunique`| number of unique elements
`value_counts`| Counts of unique values
`cov`| Calculate the covariance between columns
`corr`| Calculate the correlation between columns

#### groupby
The summaries can be obtained using any grouping variables in the data set:

```py
CHT.groupby(['famlev']).groups.keys()
CHT.groupby(['famlev']).groups['H']
CHT.groupby(['famlev']).first()

CHT.groupby(['famlev']).sum()

CHT.groupby(['famlev'])['median_house_value'].sum()
# better output
CHT.groupby(['famlev'])[['median_house_value']].sum()
```

The grouped variables would be assigned as indices, to bring them back as variables use `pf.reset.index()`
```py
CHT.reset_index(drop = True)
```

It is possible to apply even complex function, the following scripts calculate the coefficient of data.

```py
def cv(x):
 return (np.mean(x)/np.var(x))

aggr = {
    'total_rooms':'sum',
    'population': lambda x: cv(x)
}
CHT.groupby('famlev').agg(aggr)
```

The output can be tidied up,

```py
aggr = {
    'total_rooms':['mean','std']
}
grouped = CHT.groupby('famlev').agg(aggr)
grouped.columns = grouped.columns.droplevel(level=0)
grouped.rename(columns={"mean": "total_rooms", "std": "total_rooms"})
grouped.head()
```

To apply the transform on the individual data point in thee data frame, use `.transform()`, let run the standardization on the 
```py
CHT.median_income.transform(lambda x: (x - x.mean())/x.std()) 
```

#### pivot_table
The summarizations can be done using pivot table, 
```py
pd.pivot_table(CHT, index=['famlev'], aggfunc=['mean'])
```

Let consider two variables in the index of pivot table, the result will be a stack table which using `.unstack()`, it convert to stack, see below 

```py
pv_0=pd.pivot_table(CHT, index=['famlev','size'], aggfunc=['mean'])
pv_0.columns = pv_0.columns.droplevel() # drop a level from a multi level comulmn index
pv_0.unstack()
```


Pivot can provide more tools, see below  
```py
df = pd.DataFrame([["a","n1","1"], ["a","n2","2"], ["b","n1","3"], ["b","n2","s4"],["b","n2","s4"]], columns=["meta1", "name", "data"])
df.pivot_table(values='data', index='meta1', columns='name', aggfunc=",".join)
```

#### Iterating over rows
Unlike numpy, pandas is column based, to create numpy array just use  `CHT.to_numpy()`. A simple way tp iterate over row, one can use `.iterrows()` and `.itertuples()`. The `.iterrows()` creates series from row,

```py
for index, row in CHT.iterrows():
    print(row)
```

The `.itertuples()` generates tuple of rows.  
```py
for row2 in CHT.itertuples():
    print(row2)
```





## Merging
Panada is very useful for merging dataset, to achieve merging
data consider the following data sets, where 'id1' and 'id2' include the ids of data.

```py
raw_data = {'id1': range(4),'income': [10,12,14,16]}
dat1 =pd.DataFrame(raw_data, columns = ['id1', 'income'])

raw_data = {'id2': range(6),'pay': [9,11,13,15,17,19]}
dat2 =pd.DataFrame(raw_data, columns = ['id2', 'pay'])
```

Obviously the id variable are not the same, they can be compared using
``` py
dat1['id1'].isin(dat2['id2']).value_counts()
dat2['id2'].isin(dat1['id1']).value_counts()
```

`value_counts()` produce list of unique values and how often they occur in the dataset. 
`pd.merge` can merge different data-frames, the merging can be done based on the identities of left dataset, if there is no match in the right file, Python adds `NaN`.
```py
result = pd.merge(dat1, dat2, left_on='id1', right_on='id2',how='left')
```

On contrary, one can the right dataset as matching,
```py
result = pd.merge(dat1, dat2, left_on='id1', right_on='id2',how='right')
```

Since the ids are not the same, one can do merging based on the intersection of the ids,
```py
result = pd.merge(dat1, dat2, left_on='id1', right_on='id2',how='inner')
```

Merging can also be done based on the union of the ids,
```py
result = pd.merge(dat1, dat2, left_on='id1', right_on='id2',how='outer')
```

Note: If the names of id variables are the same in the both datasets, you can use ```on=id_name``` instead  ```left_on=``` and ```right_on=```.
Note: if you want to identify where the date in rows are from, add  argument ```indicator=True```, then new column named `_merge` would be added to the merged data which show its originate.
``` py
result = pd.merge(dat1, dat2, left_on='id1', right_on='id2',how='outer', indicator=True)
```

To combine row-wise, use `concat`.
```py
result = pd.concat([dat1, dat2],axis=1)
```

To combine column-wise:
```py
result = pd.concat([dat1,dat1], axis=0)
```

note, if dat1 and dat2 are not dataframe, the result will bot be dataframe, so you might use 
```py
result.to_frame()
```

If the dataframes ahve the same columns, they can be combined using  `df1.append(df2)`. 

## Melt
To change from wide to long, we can use `pd.melt(df, id_vars=None, value_vars=None, var_name=None, value_name='value', col_level=None, ignore_index=True)`. 

```py
var={"A": [1,2,0], "B": [2,3,4], "C":['A', 'Z', 'C']}
df= pd.DataFrame(data=var)
pd.melt(df, id_vars=['A'], value_vars=['B', 'C'])
pd.melt(df, id_vars=['A'], var_name="id",value_vars=['B', 'C'],value_name='A_or_B')
pd.melt(df, id_vars=['A'], value_vars=['B', 'C'],var_name="test",value_name='value2',ignore_index=False) # keep orifinal index
pd.melt(df, id_vars=['A'], value_vars=['B', 'C'],var_name="test",value_name='value2',ignore_index=True) # generate new index
pd.melt(df, id_vars=['A'], value_vars=['B', 'C'],var_name="test",value_name='value2',ignore_index=True)
```

If columns are a MultiIndex then use `col_level =0, 1` to decide which level to melt.

## Creating bins
To create bins from the data value, one can use `pd.cut`, it actually creates a categorical variable from continuous variables 

```py
var={"A": [1,2,0,7,9,4,3,1]}
df= pd.DataFrame(data=var)
pd.cut(df.A,3)  # creat three bins
pd.cut(df.A,3,labels=["low",'middle', "high"]) # add label
pd.cut(df.A,3,labels=["low",'middle', "high"], ordered=False) # drop order
pd.cut(df.A,3, labels=False) # drop label
pd.cut(df.A,[0, .25, .5, .75, 1.]) # add the bins manually
```

To generate bins according the quantiles, use `.gcut()`
```py
pd.qcut(df.A,[0, .25, .5, 1.])
```

## interval_range 
The function `interval_range` can eb used to data with range format, such data can be use as index as well. 
```py
pd.interval_range(start=0, end=10, freq=3)
pd.interval_range(start=0, end=10, freq=3, closed='left')
pd.interval_range(start=pd.Timestamp('2021-01-01'),end=pd.Timestamp('2021-01-30'))
pd.interval_range(start=pd.Timestamp('2021-01-01'),periods=4)
```


## Dummy 
It generates a dummy variable from categorial variable 
```py
var={"A": [1,2,0], "B": [2,3,4], "C":['A', 'Z', 'C']}
df= pd.DataFrame(data=var)
pd.get_dummies(df)
pd.get_dummies(df.C)
```

## Factorize
The function `pd.factorize()`  is useful to get distinct value of array or represent the array as numeric, 
Encode the object as an enumerated type or categorical variable.
```py
var=pd.DataFrame({"A": [1,2,0], "B": [2,3,4], "C":['A', 'Z', 'C']})
lab, uniques = pd.factorize(var.C)
lab
uniques
```

Pandas has the function `pd.Categorical()` that can be use to represent a categorical data, the followinf scripts show how pd.factorize can be use on categorical data.
```py
var = pd.Categorical(['a', 'a', 'c'], categories=['a', 'b', 'c'])
lab, uniques = pd.factorize(var)
lab
uniques
```

## Crosstab
Consider housing_median_age and total_rooms, group them using their quantile, then find the cross tabulate of them,
```py
CHT['houlev'] = ''
C1=CHT.housing_median_age<=CHT.median_income.quantile(.3)
C2=CHT.housing_median_age>=CHT.median_income.quantile(.7)
CHT.loc[C1,'houlev']='L'
CHT.loc[~C1&~C2,'houlev']='M'
CHT.loc[C2,'houlev']='H'

CHT['roomlev'] = ''
C1=CHT.total_rooms<=CHT.total_rooms.quantile(.3)
C2=CHT.total_rooms>=CHT.total_rooms.quantile(.7)
CHT.loc[C1,'roomlev']='L'
CHT.loc[~C1&~C2,'roomlev']='M'
CHT.loc[C2,'roomlev']='H'

pd.crosstab(CHT.roomlev, CHT.houlev, margins=True)
```

Now use `famlev` as third variable and find their cross tab.

```py
pd.crosstab([CHT.roomlev, CHT.houlev], CHT.famlev, margins=True)
```

## Accessors
The accessors include the built-in functions that come in handy when you want to do some basic function, list is 
```py
>>> pd.Series._accessors
{'sparse', 'str', 'cat', 'dt'}
```
The `sparse`, `cat`, and `dt` can be used to handles sparse matrices, handles categorical data, and handles date formats.  'str' is very handy to string, see below. 

### String accessor
Pandas has useful functions to work with text data, and it also accepts "regular expressions" and "re" module, a complete description can be 
in (link)[https://pandas.pydata.org/pandas-docs/stable/user_guide/text.html],few examples are given in the below

```py
var=pd.DataFrame({"Name":["Sa", "La", "Ry"],"Family":["Am", "Al", "Am_AL"], "Date":["2019", "2020","2021"]})
var.Family.str.count('Am') # show where it happens (0/1)
var.Family.str.match('Am') # show where it happens (True/False)
var.Family.isin(['Am'])   
var.Family.str.len()       # Compute the length
var.Family.str.isdigit()  # Shows is it number or not. 
var.Family.str.lower()    # Convert to lower case
var.Family.str.upper()    # Convert to  upper case
var.Family.str.replace('Al','Am') # Replace 'Al' with 'Am'
var.Family.str.split("_", expand=True) # Split where "_" observed
var.Family.str.cat(sep=",")            # Concatenate  
var.Family.str.cat(var.Name, join="left",sep=",")   # Concatenate  with another variable
var.columns=var.columns.str.lower() # Convert the column's names to lower case 
```


## Normalize\Standardize
Sometime, we need to scale data, there are diifernt method.

### Z-sccore 
To normalize, we can use `zscore` from `scipy`:  
```py
import pandas pd 
var={"A": [1,2,3,4], "B": [4,3,2,1]}
df= pd.DataFrame(data=var,index=(range(4)))
from scipy import stats
stats.zscore(df)
```

### Box-Cox Transformation
To run Box-Cox Transformation on data, you can use `boxcox` from `scipy`, 'the below run it on aspecific function. 

```py
df['A']=stats.boxcox(df.A)[0]
```

To run on all columsn, run the below code. 
```py
for col in df.columns[0:]:
  df[col]=stats.boxcox(df[col])[0]
```

### Min-Max scaling
An alternative approach to z-score normalization is min-max which scale data 0-1, `minmax_scaling` from `mlxtend` achieve this aim. 

```py
from mlxtend.preprocessing import minmax_scaling
var={"A": [1,2,3,4], "B": [4,3,2,1]}
df= pd.DataFrame(data=var,index=(range(4)))
minmax_scaling(df, columns=["A","B"])
```

This function can be used to numpy's array as weel 

```py
import numpy as np
array = np.array([[1, 4], [2, 3], [3, 2], [4, 1]])
minmax_scaling(array, columns=[0, 1])
```

## Pipeline 
Pipeline in pandas allows to build a sequence of function to run in order on data-frame. 

```py
def categ(x,col):
  x[col].quantile(.3)
  x['lev'] = ''
  C1=x[col]<=x[col].quantile(.3)
  C2=x[col]>=x[col].quantile(.7)
  x.loc[C1,'famlev']='L'
  x.loc[~C1&~C2,'famlev']='M'
  x.loc[C2,'famlev']='H'
  return x

def cv(x):
 return (np.mean(x)/np.var(x))

CHT.pipe(categ, col='median_income').pipe(cv)
```

## Convert to Numpy
Data frame can easily be converted to an array and a matrix: 

```py
CHT.values
CHT.as.matrix
```

## save
One of best format for saving data set is CSV data, the following script save the data as CSV without add row number and name, index=False.

```py
CHT.to_csv("CHT.csv", index=False, encoding='utf8')
CHT.to_excel("CHT.xlsx")
```

## Good References  
http://jonathansoma.com/lede/foundations/
https://github.com/TomAugspurger/effective-pandas
https://www.shanelynn.ie/summarising-aggregation-and-grouping-data-in-python-pandas/
https://chrisalbon.com/python/data_wrangling/pandas_crosstabs/
https://github.com/guipsamora/pandas_exercises
