---
title: Seaborn
---

#  Seaborn

Seaborn provides advanced graphical capabilities for creating sophisticated statistical visualizations with ease. It simplifies the process of generating complex plots from pandas DataFrames using simple commands. Let consider the `CHD_test.csv`, 

```python
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 
CHD=pd.read_csv('./data/CHD_test.csv',index_col=False)
CHD.head()
```
<!-- 
plt.savefig('data.png') 
-->

![](seaborn/data.png)

## Histogram

Standardize the 'median_income' and  'median_house_value' and plot the 

```python
import seaborn as sns
sns.set(color_codes=True)

CHD['median_income'] = (CHD['median_income'] -CHD['median_income'].mean()) / CHD['median_income'].std()
CHD['median_house_value'] = (CHD['median_house_value'] -CHD['median_house_value'].mean()) / CHD['median_house_value'].std()
for col in ['median_income','median_house_value']:
    plt.hist(CHD[col], density=True)
plt.show(block=False)
```
<!-- 
plt.savefig('seaborn1.png') 
-->

![](seaborn/seaborn1.png)


We can get a smooth estimate of the distribution using a kernel density estimation (KDE):
```python
import warnings
warnings.filterwarnings("ignore")
sns.kdeplot(data=CHD, x='median_income', y='median_house_value')
plt.show(block=False)
```

<!-- 
plt.savefig('seaborn2.png') 
-->

![](seaborn/seaborn2.png)


You can create a hexagonally-based histogram using ``jointplot``:
```python
sns.jointplot(data=CHD, x='median_income', y='median_house_value',kind="hex")
```
<!-- 
plt.savefig('seaborn3.png') 
-->

![](seaborn/seaborn3.png)

```python
sns.jointplot(data=CHD, x='median_income', y='median_house_value',kind="kde", hue='famlev')
```

<!-- 
plt.savefig('seaborn4.png') 
-->

![](seaborn/seaborn4.png)



The following illustrates how to draw a box plot for different family levels.
```python
g=sns.catplot(data=CHD, x='median_income', y='famlev', kind="box")
g.set_axis_labels("Income", "Family level");
```
<!-- 
plt.savefig('seaborn5.png') 
-->

![](seaborn/seaborn5.png)

## Pairplots
We can generalize joint plots for multidimensional data, which is very useful for exploring correlations between multiple dimensions of data.
```python
sns.pairplot(CHD, hue='famlev');
```

<!-- 
plt.savefig('seaborn6.png') 
-->

![](seaborn/seaborn6.png)

## Joyplot

Joyplot is a useful plot to compare distributions, the following show how to plot 

```python
sns.set_theme(style="white", rc={"axes.facecolor": (0, 0, 0, 0)})
```

Create the data
```python
rs = np.random.RandomState(1979)
x = rs.randn(500)
g = np.tile(list("ABCDEFGHIJ"), 50)
df = pd.DataFrame(dict(x=x, g=g))
m = df.g.map(ord)
df["x"] += m
```

Initialize the FacetGrid object
```python
pal = sns.cubehelix_palette(10, rot=-.25, light=.7)
g = sns.FacetGrid(df, row="g", hue="g", aspect=15, height=.5, palette=pal)
```

Draw the densities in a few steps
```python
g.map(sns.kdeplot, "x",bw_adjust=.5, clip_on=False,fill=True, alpha=1, linewidth=1.5)
g.map(sns.kdeplot, "x", clip_on=False, color="w", lw=2, bw_adjust=.5)
```

Define and use a simple function to label the plot in axes coordinates
```python
def label(x, color, label):
    ax = plt.gca()
    ax.text(0, .2, label, fontweight="bold", color=color,
            ha="left", va="center", transform=ax.transAxes)
g.map(label, "x")
```

Set the subplots to overlap
```python
g.fig.subplots_adjust(hspace=-.25)
```

Remove axes details that don't play well with overlap
```python
g.set_titles("")
g.set(yticks=[], ylabel="")
g.despine(bottom=True, left=True)
plt.show(block=False)
```

<!-- 
plt.savefig('seaborn7.png') 
-->

![](seaborn/seaborn7.png)



## Displot
This function can be used for visualizing the univariate or bivariate distribution of data,

```python
import seaborn as sns
import matplotlib.pyplot as plt
data1 = np.random.normal(size = 100)
data2 = np.random.normal(size = 100)

var={"A": data1, "B": data2}
df= pd.DataFrame(data=var,index=(range(100)))
sns.displot(data=df,kde=True)
plt.show(block=False)
```
<!-- plt.savefig('seaborn8.png')  -->
![](seaborn/seaborn8.png)