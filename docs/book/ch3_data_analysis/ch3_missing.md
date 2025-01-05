---
title: Missing
---

# Missing 
Python can easily handle the missing, it has different symbols to work with missing: `None` and `np.nan` acting the same. `np.nan` is a float number  so when it used, the type of data change to float number. Numpy uses `NaN` as missing. Panda use `pd.NA` instead `None` and `np.nan`.

``` py
import numpy as np
import pandas as pd 

raw_data = {'income': [10,np.nan,14,16],'pay': [9,11,13,pd.NA],}
dat = pd.DataFrame(raw_data, columns = ['income','pay'])
dat
```

get the number of missing data points per column
``` py
mvc = dat.isnull().sum()
```


How many total missing values do we have?
``` py
total_cells = np.prod(dat.shape)
total_missing = mvc.sum()
```


Percent of data that is missing
``` py
percent_missing = (total_missing/total_cells) * 100
print(percent_missing)
```


## Drop missing
Remove all the rows that contain a missing value
``` py
dat.dropna()
dat.notnull() #let you highlight values which are not empty (NaN)
dat.isnull() #let you highlight values which are  empty (NaN)
dat.notna() #let you highlight values which are not NaN
```

Remove all columns with at least one missing value
``` py
columns_with_na_dropped =dat.dropna(axis=1)
columns_with_na_dropped.head()
```

## Filling missing
They fill with the mean of other values.
```
dat.income.fillna(dat.income.mean())
dat.fillna(dat.mean())
```

replace all NA's with -9
``` py
dat.fillna(-9)
```

[pandas](https://pandas.pydata.org/pandas-docs/stable/missing_data.html) defines different procedures for filling missing, the following code interpolate the NaN.

```
dat.interpolate()
```
Sometimes one needs to define part of data as missing, it can be done using `.apply`
```
dat.income.apply(lambda x: np.nan if x<=14 else x)
```


You can use `math.isnan` to on numpy


``` py
import math
[math.isnan(i) for i in dat.income]
[math.isnan(i) for i in dat.pay]
```
