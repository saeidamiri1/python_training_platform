---
date: 2024-10-26
title: Pipeline
description: How to run pipeline on data-frame
categories:
  - Python core
authors:
  - saeidamiri1
---

# Pipeline
Pipeline in Pandas allows to build a sequence of function to run in order on data-frame.
<!-- more -->

```
source ="https://storage.googleapis.com/mledu-datasets/california_housing_train.csv"
CHT = pd.read_csv(source, sep=",")

def categ(x,col):
  x[col].quantile(.3)
  x['lev'] = ''
  C1=x[col]<=x[col].quantile(.3)
  C2=x[col]>=x[col].quantile(.7)
  x.loc[C1,'famlev']=0
  x.loc[~C1&~C2,'famlev']=1
  x.loc[C2,'famlev']=2
  return x

def cv(x):
 return (np.mean(x)/np.var(x))

CHT.pipe(cv)
CHT.pipe(categ, col='median_income').pipe(cv)
```