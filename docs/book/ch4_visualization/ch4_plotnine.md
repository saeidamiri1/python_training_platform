---
title: plotnine
---

# plotnine  -nneed to work

`ggplot2` is a very useful package in R for creating advanced plots. In Python, the `plotnine` library is used to create `ggplot2`-like plots. You can import the module using `import plotnine as p9`. Generating plots in `ggplot2` (plotnine) follows a structured series of steps, which can be accomplished via:

* initialize it

```python
import plotnine as p9
CHD_plot=p9.ggplot(data=CHD)
```
<!-- 
CHD_plot.save("plotnine0.png", dpi=300)
-->

![](plotnine/plotnine0.png)


* Define aesthetics using `aes` and specify your arguments. The most important aesthetics include: `x`, `y`, `alpha`, `color`, `colour`, `fill`, `linetype`, `shape`, `size`, and `stroke`. To create variations of the plot with different parameters, you can assign it to a variable.

```python
CHD_plot=CHD_plot + p9.aes(x='median_income', y='median_house_value')
# or CHD_plot=p9.ggplot(data=CHD,mapping=p9.aes(x='median_income', y='median_house_value'))
CHD_plot.show()
```
<!-- 
CHD_plot.save("plotnine1.png", dpi=300)
-->

![](plotnine/plotnine1.png)

* Specify what you want to display and use the `+` operator to add layers and customize your plot.

```python
CHD_plot=CHD_plot+p9.geom_point()
CHD_plot.show()
```

<!-- 
CHD_plot.save("plotnine2.png", dpi=300)
-->

![](plotnine/plotnine2.png)

You can easily add scale and define label: 

```python
CHD_plot=CHD_plot+ p9.geom_point(alpha=0.15)+ p9.xlab("median_income") +
 p9.ylab("median_house_value") + p9.scale_x_log10() + 
 p9.theme_bw()+ p9.theme(text=p9.element_text(size=10))
```
<!-- 
CHD_plot.save("plotnine3.png", dpi=300)
-->

![](plotnine/plotnine3.png)


* After creating your plot, you can save it to a file in your favourite format

```python
CHD_plot = CHD_plot + p9.geom_point()
CHD_plot.save("CHD_plot.png", dpi=300)
```


##  bar chart
To generate a bar chart, you can use `geom_bar()`

```python
CHD_bar=(p9.ggplot(data=CHD,mapping=p9.aes(x='famlev'))+ p9.geom_bar())
```
<!-- 
CHD_bar.save("plotnine4.png", dpi=300)
-->

![](plotnine/plotnine4.png)

## Plotting distributions
* A boxplot can be created using `geom_boxplot()`:

```python
CHD_dist=(p9.ggplot(data=CHD,
           mapping=p9.aes(x='famlev',
                          y='median_income'))
    + p9.geom_boxplot()
    + p9.scale_y_log10()
 )
```
<!-- 
CHD_dist.save("plotnine5.png", dpi=300)
-->

![](plotnine/plotnine5.png)

* To add points behind the boxplot, you can use geom_jitter() to plot the points with some random noise to avoid overlapping points. This will create a visual representation of the data points behind the boxplot. Here's an example:

CHD_dist=(p9.ggplot(data=CHD,
           mapping=p9.aes(x='famlev',
                          y='median_income'))
    + p9.geom_boxplot()
    + p9.geom_jitter(alpha=0.1, color="green")
    + p9.scale_y_log10()
 )

<!-- 
CHD_dist.save("plotnine6.png", dpi=300)
-->

![](plotnine/plotnine6.png)