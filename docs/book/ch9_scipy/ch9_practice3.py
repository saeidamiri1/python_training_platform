import pandas as pd
import scipy as sp

data = sp.randn(5, 2)  # Create 5x2 matrix of random numbers for toy example
dates = pd.date_range('28/12/2010', periods=5)
df = pd.DataFrame(data, columns=('price', 'weight'), index=dates)
print(df)
sp.mean(data)
sp.median(data)
sp.std(data)

import numpy as np
from sklearn  import datasets

iris=datasets.load_iris()
iris
np.mean(iris,  axis=0)

from numpy import mean
tuple(mean(iris, axis=0))
print(__doc__)
