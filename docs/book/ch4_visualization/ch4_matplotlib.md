---
title: Matplotlib
---

# Matplotlib
Python offers sophisticated plotting capabilities. Plotting can be approached in two ways:
- Non-Pythonic Approach: This approach relies on external libraries like `matplotlib`, which provides user-friendly tools for interactive plotting. A common shorthand for importing this module is `import matplotlib.pyplot as plt`.
- Pythonic Approach: In this method, an empty object is created, and plots are constructed programmatically, then assigned to the empty object using code.

In the below, you can see how to run code 

## Scatter plot
The most commonly used plot is the scatter plot, see the following scripts that generate random number and plot

``` python
import matplotlib.pyplot as plt
import numpy as np
n = 100
x = 2 * np.random.rand(n)
y=2*x+np.random.rand(n)
plt.scatter(x, y)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Scatter Plot')
plt.show(block=False)

```
<!-- 
plt.savefig('matplotlib1.png') 
-->

![](matplotlib/matplotlib1.png)

Indeed, you can customize the appearance of a scatter plot using various [arguments](https://matplotlib.org/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D):<br />
- Size of point (`s`): you can adjust the size of the points, for example,  `s=10` make the point smaller,
- colour (`c`): You can specify the color of pointy. For example, `c=red` will make the points red. 
- [`marker`](https://matplotlib.org/api/markers_api.html): you can choose different marker styles for points. For example `marker=s` w ill use squares for presenting points. 


```python
plt.scatter(x, y, s=20 /(.2+x) , c='green', marker="s")
plt.show(block=False)
```
<!-- 
plt.savefig('matplotlib2.png') 
-->
![](matplotlib/matplotlib2.png)

In this example, we've customized the scatter plot to use red square for data points which obviously smaller x get bigger square. You can further explore the links provided for more marker styles and line properties in matplotlib. The following figure displays a more sophisticated plot. 

```python
xy=x**2+y**2
select=xy<1
plt.scatter(x, y, alpha=0.3)
plt.scatter(x[select], y[select],facecolor='none',edgecolors='red')
plt.show(block=False)
```
<!-- 
plt.savefig('matplotlib3.png') 
-->
![](matplotlib/matplotlib3.png)


Fit a linear model to a sample data.
```python
plt.scatter(x, y, alpha=0.5, color='orchid') 
plt.suptitle('Scatter Plot') 
plt.tight_layout(pad=2);
plt.grid(True)
fit = np.polyfit(x, y, deg=1) 
plt.plot(x, fit[0]*x + fit[1], '-',color='red', linewidth=2)
plt.show(block=False)
```
<!-- 
plt.savefig('matplotlib4.png') 
-->

![](matplotlib/matplotlib4.png)

If you want to save the figure to a file, put the script
between

```python
plt.savefig('name.png')
```

## line
Using ```plt.plot``` can plot the line, to explain let consider timesries data: 

```python
import pandas as pd
x=pd.period_range('2019-11-06', periods=12*10,freq='M').to_timestamp()
y = np.random.randn(len(x)).cumsum()
y=abs(min(y))+y
plt.plot(x, y, label='ED')
plt.title('Example Data') 
plt.xlabel('Date') 
plt.ylabel('Y')
plt.grid(True)
plt.figtext(1,0, 'note',ha='right', va='bottom')
plt.legend(loc='best', framealpha=0.5,prop={'size':'small'})
plt.tight_layout(pad=1)
plt.gcf().set_size_inches(10, 5)
plt.show(block=False)
plt.close()
```
<!-- 
plt.savefig('matplotlib5.png') 
-->
![](matplotlib/matplotlib5.png)

To excercise, let write a function to plot the following function

$$
f(x) = \begin{cases}
    sin(x),       & x\leq \pi/2,\\
    cos(x)  & x> \pi/2.\\
  \end{cases}
$$

```python
x=np.arange(0,np.pi,np.pi/100)
y=np.where(x<np.pi/2,np.cos(x),np.sin(x))
plt.plot(x,y)
```
<!-- 
plt.savefig('matplotlib6.png') 
-->

![](matplotlib/matplotlib6.png)

The other approach is to use two function instead one, it can be done using the following script,

```python
x=np.arange(0,np.pi,np.pi/100)
y=np.where(x<np.pi/2,np.cos(x),np.sin(x))
x0=x[x<np.pi/2]
plt.plot(x0,np.cos(x0), linestyle='--',label='cos(x)')
plt.axis([0,np.pi,0,1])
x1=x[(x>=np.pi/2)]
plt.plot(x1,np.sin(x1), linestyle='--',label='sin(x)')
plt.legend()
# it can be done using
# plt.plot(x0,np.cos(x0), '--',x1,np.sin(x1), '--')
```

<!-- 
plt.savefig('matplotlib7.png') 
-->

![](matplotlib/matplotlib7.png)

The argument ```plt.axis()``` defines axes limits, it can also be done using  ```plt.xlim(,)```, ```plt.ylim(,)```.  The style of line is define in ```'--'```, other styles are


Type|	Description
--- | --- 
'-' or 'solid'|	solid line
'--' or 'dashed'|	dashed line
'-.' or 'dashdot'|	dash-dotted line
':' or 'dotted'|	dotted line
'None' or ' '	|	draw nothing

There are more options for axis, for instance ```plt.axis('equal')```  and  ```plt.axis('tight')```. The labels and title  can be added to plot using ```plt.axes()```, 

```python
plt.axes(xlim=(0, 10), ylim=(-2, 2),xlabel='x', ylabel='sin(x)', title='A Simple Plot')
plt.plot(x, np.sin(x), '-')
plt.show(block=False)
plt.close()
```

<!-- 
plt.savefig('matplotlib8.png') 
-->

![](matplotlib/matplotlib8.png)

The following plot lines with different markers

```python
n = 5
linestyles = ['-', '--', '-.', ':']
markers = list('ov^<>')
x = np.linspace(0, 100, 10)
for i in range(n): 
  y = x + x/5*i + i
  st = linestyles[i % len(linestyles)]
  ma = markers[i % len(markers)] 
  plt.plot(x, y,label='Line '+str(i+1)+' '+st+ma, marker=ma,linestyle=st)
plt.grid(True)
plt.axis('tight')
plt.legend(loc='best', prop={'size':'small'}) 
plt.show(block=False)
plt.close()
```

<!-- 
plt.savefig('matplotlib9.png') 
-->

![](matplotlib/matplotlib9.png)


## Pythonic line
The following codes shows how pythonic approach can be applied to generate several plots; first generate an empty figure from the global Figure factory, then generate your plot and assign to figure. 

```python
fig = plt.figure()
for i in range(1,10):
  x=pd.period_range('2019-11-06', periods=12*10,freq='M').to_timestamp()
  y = np.random.randn(len(x)).cumsum()
  y=abs(min(y))+y
  plt.plot(x, y, label='ED%s'%i)
  plt.title('Example Data') 
  plt.xlabel('Date') 
  plt.ylabel('Y')
  plt.grid(True)
  plt.legend(loc='best', framealpha=0.5,prop={'size':'small'})
  fig = plt.figure(i) # get the figure
plt.show()
```

You can close figures according the number `plt.close(fig.number)`,  all figures `plt.close(all)`,  the current one `plt.close()`. Note, plt.cla clears the current axes, plt.clf() clears the current figure, and the plt.close() closes the entire window.


## subplot
Figures can be plotted in one figure using ```.subplot(#row,#col,position) ```, 

```python
x = np.linspace(0, 16, 800)
plt.subplot(2, 2, 1)
plt.plot(x, np.sin(x))
plt.title("Fig1")
plt.xlim(0,1.5*np.pi)
plt.xlabel("X-axis")
plt.ylabel("sin(x)")
plt.subplot(2, 2, 2)
plt.plot(x, np.cos(x))
plt.subplot(2, 2, 3)
plt.plot(x, np.sin(x)*np.cos(x))
plt.subplot(2, 2, 4)
plt.plot(x, np.sin(x)+np.cos(x))
plt.show(block=False)
```
<!-- 
plt.savefig('matplotlib10.png') 
-->

![](matplotlib/matplotlib10.png)

You can not use `plt.axes()` for subplot. 
