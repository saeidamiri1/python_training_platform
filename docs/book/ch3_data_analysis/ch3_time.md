---
title: Time 
---

# Time
Here, we explain two time-related modules in Python.

## datetime module
The `datetime` module  provide functions to work with the date format, which they can be used to maniuplate and parsing a dates and time. 

``` py
import  datetime
todays_date = datetime.date.today()
print(todays_date)
now = datetime.datetime.now()
print(now)
```

You can a general date object to represents a date (year, month and day).

``` py
dt = datetime.date(2024, 1, 2)
print(dt)
print(dt.year,dt.month,dt.day)
```

You can a general time object to represents a time (hour, minute, second and microsecond).

``` py
tm = datetime.time(12,3,4,5)
print(tm)
print(tm.hour,tm.minute,tm.second,tm.microsecond)
```

In a general you can you datetime object, 

``` py
dtm = datetime.datetime(2024, 1, 2,12,3,4,5)
print(dtm)
print(dtm.year,dtm.month,dtm.day,dtm.hour,dtm.minute,dtm.second,dtm.microsecond)
```

You can change the structure of time, using  `strftime`; US format mm/dd/yyyy, UK's format dd/mm/yyyy

``` py
print(dtm.strftime("%m/%d/%Y, %H:%M:%S"))
print(dtm.strftime("%d/%m/%Y, %H:%M:%S"))
```
%Y - year, %m - month, %B - month in full name, %d - day, %H - hour, %M - minute, %S - second. 
The output is in string  format. You can reform tha sting format to datetime format. 


``` py
date_string = "25 January, 2024"
date_string

date_object = datetime.datetime.strptime(date_string, "%d %B, %Y")
date_object
```


You can find different between time, 
``` py
now_dtm = datetime.datetime.now()
dtm = datetime.datetime(2024, 1, 2,12,3,4,5)

diff_dtm = now_dtm - dtm
diff_dtm
print(diff_dtm)
```
Obviously the output the timedelta objects, to compute the total second of seconfd you can use `diff_dtm.total_seconds()`


You can handle the timezone in Python, 

``` py
import pytz
now_dtm = datetime.datetime.now()
tz_NY = pytz.timezone('America/New_York') 
datetime_NY = datetime.datetime.now(tz_NY)
print("Local:", now_dtm)
print("NY:", datetime_NY)
```

### numerial format
#### timestamp
A unix timestamp is the number of second between a particular date and January 1, 1970, at UTC. You can convert date to the timestamp() method.

``` py
now = datetime.datetime.now()
print(now)
ts=datetime.datetime.timestamp(now)
print(ts)
```

You can convert a timestamp to a date using the fromtimestamp() method.

``` py
timestamp = datetime.datetime.fromtimestamp(ts)
print("Date =", timestamp)
```
#### ordinal
Other approach to work with number instead data forma is to us the proleptic Gregorian ordinal of the date, where January 1 of year 1 is 1. 

``` py
date1 = datetime.date(1, 1, 1)
date2=date1.toordinal()
print(date2)
```

and back:

``` py
print(datetime.date.fromordinal(date2))
```


### Panda date

``` py
import numpy as np
import pandas as pd 
X1=["2023-1-1","2023-2-1","2023-3-1","2023-4-1"]
X2=[10,11,12,13]
raw_data = {'X1': X1,'X2': X2}
df=pd.DataFrame(raw_data)
df
```

``` py
df.dtypes
df.X1 = pd.to_datetime(df.X1)
df
df.dtypes
```

``` py
pd.to_datetime(df['X1']).dt.day
pd.to_datetime(df['X1']).dt.month
pd.to_datetime(df['X1']).dt.year
```

``` py
df = df.set_index('X1')
df
df.index.is_unique
df.sort_index(ascending = True).head()
```

To work on read data let consider Dow Jones Index:  

``` py
dow_jones = pd.read_csv('data/dow_jones_index/dow_jones_index.data')
dow_jones.head(20)
dow_jones.info()
```

Select 'stock','date','open','high','low'
``` py
dow_jones=dow_jones.loc[:,['date','stock','open','high','low']] 
```

Assign week number as index 
``` py
import datetime
def to_week(x):
  return datetime.datetime.strptime(x, '%m/%d/%Y').strftime("%V")
```

Apply the function to_week on the column data 
``` py
dow_jones['week']=dow_jones['date'].apply(to_week)
dow_jones = dow_jones.set_index('week')
dow_jones=dow_jones.drop(['date'], axis=1)
```

Drop doller sign from columns and change them to numeric
``` py
for i in dow_jones.columns[1:]:
    dow_jones[i]=dow_jones[i].str.strip('$').astype(float)
```

Compute the mean for each week:

``` py
dow_jones.iloc[:,1:4].groupby(dow_jones.index).mean()
```

## time module
The `time` module provide various time-related function for time access, to get the current time: 

``` py
import time 
print(time.asctime())
time.localtime()
print(time.strftime('%a %d.%m.'))
```

Pause the execution of a program for two seconds:
``` py
time.sleep(2) 
```

You can create a simple code to check running time. 

``` py
import time
start_time = time.time()
some code 
print("--- %s seconds ---" % (time.time() - start_time))
```

timeit is a module to check running of small code. 
