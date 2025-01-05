---
date: 2024-10-26
title: Generating frequency
description: Frequency in Python
categories:
  - Python core
authors:
  - saeidamiri1
---

# Generating frequency

Here we demonstrate how generate frequency table from the data. 
<!-- more -->



## Data frame 
First creates a dataframe, then use `value_counts`, `groupby`, `crosstab`, and `pivot. 
```
import numpy as np
import pandas as pd

n = 50 
group = ["High", "Low"] 
size = ["Small", "Medium", "Large"] 
data = pd.DataFrame({'Size': np.random.choice(size,n), 'Group': np.random.choice(group,n)})
``` 
### value_counts
```
frq_data=data.value_counts(["Group", "Size"])
frq_data.to_csv('frq_data.csv', sep=',', header=True,index=True, encoding='utf8')
```

### using groupby
```
data.groupby(["Group", "Size"]).size()
data.groupby(["Group", "Size"]).size().reset_index(name="Freq")
```

### crosstab
```
pd.crosstab(data.Group,data.Size,margins = True)
pd.crosstab(data.Group,data.Size,margins = False)
```

### pivot
```
data.pivot_table(index=['Group','Size'], aggfunc='size')
```


### Plot 
####  Mosaic plot
```
import matplotlib.pyplot as plt
from statsmodels.graphics.mosaicplot import mosaic
mosaic(data, ["Group", "Size"], title='DataFrame as Source')
plt.show()
```

####  Chord Diagram
```
from pycirclize import Circos
matrix_df=pd.DataFrame(pd.crosstab(data.Group,data.Size,margins = False))
circos = Circos.initialize_from_matrix(
    matrix_df,
    space=5,
    cmap="tab10",
    label_kws=dict(size=12),
    link_kws=dict(ec="black", lw=0.5, direction=1),
)
circos.savefig("chroddiagram.png")
```



## list 
```
lst = ['apple', 'banana', 'apple', 'orange']

from collections import Counter
Counter(lst)
Counter(data['Group'])

counts = [(word, lst.count(word) / len(lst)) for word in set(lst)] 
[{word: lst.count(word) / len(lst)} for word in set(lst)] 

def relative_frequency(lst, element):
    return lst.count(element) / float(len(lst))
```



<!-- **[⬆ back to top](#contents)**

### License
Copyright (c) 2021 Saeid Amiri -->