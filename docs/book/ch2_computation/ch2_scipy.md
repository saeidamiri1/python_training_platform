# SciPy

SciPy is built on top of NumPy and is designed for scientific computation. It offers many built-in functions beyond what we have covered here—this is just a brief introduction. The best resource for learning SciPy is its [official tutorial](https://docs.scipy.org/doc/scipy-1.9.0/index.html). SciPy includes a number of subpackages that organize functions based on their application areas.

## Matrix 
It provides useful functions for linear algebra operations, which are compiled implementations of standard libraries such as BLAS (Basic Linear Algebra Subroutines) and LAPACK (Linear Algebra PACKage).

```Python
from scipy import linalg
x=np.eye(2)
linalg.det(x) # determinant of a square matrix:
linalg.inv(x)  # the inverse of a square matrix
linalg.eig(x) # generalized eigenvalue
linalg.pinv(x) # Compute the (Moore-Penrose) pseudo-inverse of a matrix
a = np.array([[3, 2, 0], [1, -1, 0], [0, 5, 1]])
b = np.array([2, 4, -1])
linalg.solve(a,b) # Solves the linear equation set a @ x == b for the unknown x for square a matrix.
```

## Statistics (scipy.stats)
`scipy.stats` contains fundamental tools for statistical analysis, including descriptive statistics, hypothesis testing, and probability distributions.

### Descriptive statistics 
The `scipy.stats` subpackage provides functions to summarize and describe the main features of a dataset. In the example below, we compute the mean, median, mode, variance, and standard deviation of the data.

```Python
from scipy import stats
data = [1, 2, 3, 4]
mean = stats.tmean(data)
median = stats.scoreatpercentile(data, 50)
mode = stats.mode(data) 
variance = stats.tvar(data) 
std_deviation = stats.tstd(data)
```

### Continuous distributions
In the example below, we explore the normal distribution by generating an array of x values between -2 and 2, along with a random sample from the distribution. We then compute the probability density function (PDF) and cumulative distribution function (CDF).

```Python
from scipy import stats
mean0 = 0
std_dev0 = 1
size0 = 10 
samples = stats.norm.rvs(loc=mean0, scale=std_dev0, size=size0)

x = np.linspace(2, 2, 5)
pdf = stats.norm.pdf(x, mean, std_dev)
cdf = stats.norm.cdf(x, mean, std_dev)
```

In the next, we look at the exponential distribution, 

```Python
lambda0 = 1
samples = stats.expon.rvs(scale=1/lambda0, size=size0)

x = np.linspace(0, 10, 5)

pdf = expon.pdf(x, scale=1/lambda0)
cdf = expon.cdf(x, scale=1/lambda0)
```

### Discrete probability distributions
In the below, we look at the binomial distribution $Bionom(10,0.3)$

```python 
n0, p0 = 10, 0.3
size0=20
sample = stats.binom.rvs(n=n0, p=p0, size=size0)

x = np.arange(0, 4)
pmf = binom.pmf(x, n0, p0)
cdf = binom.cdf(x, n0, p0)
```

Next is the poisson distribution,

```python 
mu0 = 3
size0 = 20 
samples = stats.poisson.rvs(mu=mu0, size=size0)

x = np.arange(0, 10)

pmf = stats.poisson.pmf(x, mu=mu0)
cdf = stats.poisson.cdf(x, mu=mu0)
```

### Statistical tests 
For example, let's generate 100 random samples from a standard normal distribution, which has a mean of 0 and a standard deviation of 1. We then fit maximum likelihood estimation of the unknown parameters (stats.norm.fit): 

```Python
from scipy import stats
dist = stats.norm(loc=0, scale=1)
sample = dist.rvs(size=100) 
loc, scale = stats.norm.fit(sample) 
loc
```

We can perform hypothesis tests that produce a test statistic and a p-value, helping us assess the statistical significance of our results.

```Python
stat, p_value  = stats.normaltest(sample)
print(f"t-statistic: {stat:.3f}")
print(f"p-value: {p_value:.3f}")
```

To perform a statistical test between two samples, let's start by generating the samples.

```python 
group1 = stats.norm.rvs(loc=mean, scale=1, size=size0)
group2 = stats.norm.rvs(loc=mean, scale=1.2, size=100)
stat, p_value = stats.ttest_ind(group1, group2)
print(f"t-statistic: {stat:.3f}")
print(f"p-value: {p_value:.3f}")
```

Next, we examine the Chi-Squared test, which is performed on a contingency table. We'll first create the table using NumPy, and then run the statistical test.

``` python 
data = np.array([[5, 8], [10, 6]])
chi2_stat, p_val, dof, expected 
res= stats.chi2_contingency(data)

print(f"Chi-squared statistic: {res.statistic:.4f}")
print(f"p-value: {res.pvalue:.4f}")
print(f"Degrees of freedom: {res.dof}")
print(f"Expected values: \n{res.expected_freq}")
```

## Integration (scipy.integrate)
You can compute the integral of a given function using `scipy.integrate`, which offers various numerical integration methods.

### Quadrature
scipy.integrate.quad uses a quadrature approach to compute the numerical integral of a function which has one variable. You need to define the function and the integration range. Let's compute the following integral:
$$
\int_0^1 x^2 dx
$$


```Python
from scipy import integrate
x2 = lambda x: x**2
integral, error = integrate.quad(x2, 0, 1)
integral
error
np.allclose(integral, 1**3 / 3) 
```

Let compute the integral of  $\int_0^{\pi/2} \cos(x) dx$:

```Python
integral, error = integrate.quad(np.cos, 0, np.pi/2)
integral
error
np.allclose(integral, 1)
```

### Double Integral
scipy.integrate.dblquad can be used to calculate double integrals.

```Python
fx = lambda x, y: 4*x**2*y
integral, error = integrate.dblquad(fx, 0, 1,2,4)
integral
error
```

### Multiple Integral
scipy.integrate.nquad can be used to calculate multiple integrals.

```Python
fx = lambda x, y, z: 4*x**2*y*z
ranges=[[0,1],[2,4],[3,5]]
integral, error = integrate.nquad(fx,ranges)
integral
error
```

### Initial Value Problems
The integration of a differential equation can be performed using the solve_ivp function. Let's consider the following example:

$$
\dfrac{y}{t}=f(y,t)
$$

from an initila time $t_0$ and initial state  $y(t=t_0)=t_0$, up to a final time $t_f$.  Let's consider the equation $\dfrac{y}{t}=3 y$ with the initial condition $y(t=0)=1$ on the interval $0<t<2$. 

```Python
import scipy as sp 
def f(t, y):
    return 3 * y
t_span = (0, 2)  # time interval
t_eval = np.linspace(*t_span)  # times at which to evaluate `y`
y0 = [1,]  # initial state
res = sp.integrate.solve_ivp(f, t_span=t_span, y0=y0, t_eval=t_eval)
res
import matplotlib.pyplot as plt
plt.plot(res.t, res.y[0])
plt.show()
```

## Optimization (scipy.optimize)
scipy.optimize provides a collection algorithms for solving optimization problems. It can be used to minimize or maximize functions, find function roots, and fit models to data. 

### Root Finding
scipy.optimize.root_scalar() can be used to find a root of a function. Let's consider a case where the function and its derivative exist, along with an initial guess for the solution.

```Python
def f(x):
    return (x-2)*(x+3)
def df(x):
    return 2*x + 1
x0 = 0  # guess
res = sp.optimize.root_scalar(f, x0=x0, fprime=df)
res
```

It is possible to find the root of a function over a specified interval.

```Python
res = sp.optimize.root_scalar(f, bracket=(-10, 0))
res.root
```

In the multivariate case, you can use scipy.optimize.root() to find the roots of a system of equations.

```Python
def f(x):
    return [x[0] + x[1] - 3 ,
            x[0]**2 - x[1]-3]
res = sp.optimize.root(f, x0=[0, 0])
```

### Curve fitting
scipy.optimize.curve_fit uses non-linear least squares to fit a function to data. To illustrate curve fitting, let's consider the following example function:

```Python
def func(x, a, b, c):
    return a * np.exp(-b * x) + c

a,b,c=2,1,3
```

Let's generate some dat 

```Python
xdata = np.linspace(0, 10, 100)
y = func(xdata, 2, 1, 3)
y_noise = 0.1 *stats.norm.rvs(loc=0, scale=1, size=xdata.size)
ydata = y + y_noise
```

The parameters can be estimated through approximation:
```Python
params, _ = optimize.curve_fit(func, xdata, ydata, p0=[1, 1, 1])
```

### interpolate 
scipy.interpolate is used to estimate values of an unknown function and can be applied to compute its integral, derivative, or inverse. Let's create a dataset and add some noise to it.

```Python
rng = np.random.default_rng()
xdata = np.linspace(0, 2*np.pi, 100)
funct = np.sin(xdata)
noise = stats.norm.rvs(loc=0, scale=0.5, size=100)
ydata = funct + noise
```

Now we can fit a model to the data

```Python
int_sm = sp.interpolate.make_smoothing_spline(xdata, ydata)
int_xdata = np.linspace(0, 2*np.pi, 300)
int_fit = int_sm(int_xdata)
```

make_smoothing_spline smooths the data and does not necessarily pass through all the points. To force the curve to pass through every point, use make_interp_spline instead.

```Python
int_in = sp.interpolate.make_interp_spline(xdata, ydata)
```

### Minimize
In general, you can find the minimum of a function using scipy.optimize.minimize(). Let's consider the function $f(x_0, x_1) = (x_0-3)^2 + (x_1-1)^3$

```Python
def f(x):
    return (x[0] - 3)**2 + (x[1] - 1)**3

res = sp.optimize.minimize(f, x0=[0, 0])
res
```

## Input/output
SciPy offers functions for importing and exporting data in a wide variety of formats, including MATLAB, ARFF, WAV, Matrix Market, IDL, NetCDF, TXT, and CSV.

```Python
import numpy as np
from scipy import io

x=np.eye(2)
io.savemat('examp.mat', {'col1': x[0],'col2': x[1]}) 
x_2 = io.loadmat('examp.mat', struct_as_record=True)
x_2['col1']
```
