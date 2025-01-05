# SciPy
https://github.com/krother/Python3_Package_Examples/tree/master/scipy
SciPy is built on top of Numpy and developed for Scientific Computation. 

## file format
SciPy has function for import\export data in a wide range of format:  Matlab, Arff, Wave, Matrix Market, IDL, NetCDF, TXT, CSV. 

```{Python, echo = FALSE, message = FALSE}
import numpy as np
from scipy import io as spio

x=np.eye(2)
spio.savemat('examp.mat', {'col1': x[0],'col2': x[1]}) 
x_2 = spio.loadmat('examp.mat', struct_as_record=True)
x_2['col1']
```
## Matrix 
It has useful functions for linear algebra.

```{Python, echo = FALSE, message = FALSE}
from scipy import linalg as splinalg
x=np.eye(2)
splinalg.inv(x) 
splinalg.eig(x)
splinalg.pinv(x)
splinalg.solve(x)
```
## Combinatorics
## Gamma function 
## Statistics (scipy.stats)
## Optimization (scipy.optimize)
## Integration (scipy.integrate)
## Good References  

https://docs.scipy.org/doc/scipy/reference/index.html
https://scipy-lectures.org/intro/scipy.html