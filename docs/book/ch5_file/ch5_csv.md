---
title: CSV
---
# CSV 
Working with CSV in python is very simple 

### Read  

Read the DataFrame from a CSV file, specifying that the first row contains the header or None
```python
df=pd.read_csv('file.csv',heder=1)
df=pd.read_csv('file.csv',header=None)
```

Specifying that a column is dates
```python
df = pd.read_csv('file.csv', parse_dates=['dates'])
```

Select only specific columns.
```python
df = pd.read_csv('file.csv', usecols=['foo', 'bar'])
```

If the first column is not selected, try setting index_col=False
```python
DF=pd.read_csv('file.csv', sep='\t',index_col=False)
```

Adding column names, and therefore an index
```python
  df=pd.read_csv('file.csv',names=['col1','col2','col3'])
```


To skip the  comments:
```python
df = pd.read_csv("DF.txt",comment='#')
```

### export
```python
df.to_csv('births1880.csv',index=False,header=False)
```

###  tab-separated file
To work with a tab-separated values file, we use the csv module. The following code shows how to create a file.
```python
import csv
with open('my_data.csv', 'w') as csvfile:
    fieldnames = ['SampleID','Age','Treatment', 'Weight'] # Create a list with the column
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter='\t')    
    writer.writeheader()
    writer.writerow({"SampleID":"mouse1", "Age":4, "Treatment":"Control", "Weight":3.2})
    writer.writerow({"SampleID":"mouse2", "Age":5, "Treatment":"Control", "Weight":3.6 })
    writer.writerow({"SampleID":"mouse3", "Age":4, "Treatment":"Control", "Weight":3.8 })
    writer.writerow({"SampleID":"mouse4", "Age":4, "Treatment":"ad libitum", "Weight":3.6 })
    writer.writerow({"SampleID":"mouse5", "Age":4, "Treatment":"ad libitum", "Weight":3.7 })
    writer.writerow({"SampleID":"mouse6", "Age":4, "Treatment":"ad libitum", "Weight":3.5 })
```

You can use `.read_csv()` from the Panda module.. 
```python
df=pd.read_csv('my_data.csv', sep='\t')
```

The following code shows how to handle read the file using `r` mode:

```python
with open('my_data.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile, delimiter='\t')
    for row in reader:
        print(f"SampleID:{row['SampleID']}, Age:{row['Age']}, Treatment:{row['Treatment']}, Weight:{row['Weight']}")
```

### blocksize
Dask is a library designed for parallel computing, you can manage large datasets more efficiently using block sizes. It allows you to work with large data by breaking it up into smaller, called partitions. Each partition can be processed in parallel.

```python
import dask.dataframe as dd

df = dd.read_csv('largefile.txt', names=['chr','pos','cov'], sep='\t', blocksize=34000000) # blocksize controls the size of each partition.

print("Descriptors: {0}".format(df['cov'].describe().compute()))
```
