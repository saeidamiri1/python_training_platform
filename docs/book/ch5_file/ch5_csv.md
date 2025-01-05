---
title: CSV
---
# CSV 
Working with CSV in python is very simple 

### read  
read-in the data frame from csv file specifying that the first row is the header
```{Python, echo = FALSE, message = FALSE}
df=read_csv('/Users/ernesto/Google_Drive/PYTHON_LEARN/births1880.csv',heder=1)
df=read_csv('/Users/ernesto/Google_Drive/PYTHON_LEARN/births1880.csv',header=None)
```

read-in the data frame and specifying that 2 columns are dates
```{Python, echo = FALSE, message = FALSE}
df = pd.read_csv('pizza.csv', parse_dates=['dates'])
```

read-in the data frame and use only some columns
```{Python, echo = FALSE, message = FALSE}
df = pd.read_csv('pizza.csv', usecols=['foo', 'bar'])
```

if first column is not picked, try with index_col=False
```{Python, echo = FALSE, message = FALSE}
DF=pd.DataFrame.from_csv('/Users/ernesto/projects/IGSR/16_12_16/cov_DF.txt', sep='\t',index_col=False)
```


read-in the data.frame from csv file adding column names, and therefore an index
```{Python, echo = FALSE, message = FALSE}
  df=read_csv('/Users/ernesto/Google_Drive/PYTHON_LEARN/births1880.csv',names=['col1','col2','col3'])
```


### blocksize

```{Python, echo = FALSE, message = FALSE}
import dask.dataframe as dd

df = dd.read_csv('files/out.cov', names=['chr','pos','cov'], sep='\t', blocksize=34000000) # blocksize controls the size of each partition.

print("Descriptors: {0}".format(df['cov'].describe().compute()))
```


### export
```{Python, echo = FALSE, message = FALSE}
df.to_csv('births1880.csv',index=False,header=False)
```

###  How create a tab-separated values file  
```{Python, echo = FALSE, message = FALSE}
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
The created file can be imported using the following code

```{Python, echo = FALSE, message = FALSE}
with open('my_data.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile, delimiter='\t')
    for row in reader:
        print(f"SampleID:{row['SampleID']}, Age:{row['Age']}, Treatment:{row['Treatment']}, Weight:{row['Weight']}")
```


###  tsv file:
```{Python, echo = FALSE, message = FALSE}
df=pd.DataFrame.from_csv('/Users/ernesto/projects/IGSR/16_12_16/cov_DF.txt', sep='\t')
```
read-in the data frame from file and skipping comments:
```{Python, echo = FALSE, message = FALSE}
df = pd.read_csv("DF.txt",comment='#')
```


