---
title: Challenges
---

# Challenge

UNDER CONSTRUCTION. 




import pandas as pd
import scipy as sp

data = sp.randn(5, 2)  # Create 5x2 matrix of random numbers for toy example
dates = pd.date_range('28/12/2010', periods=5)
df = pd.DataFrame(data, columns=('price', 'weight'), index=dates)
print(df)
sp.mean(data)
sp.median(data)
sp.std(data)

