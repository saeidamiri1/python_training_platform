---
date: 2024-10-26
title: Adding new column to data-frame
description: How to add new column to data-frame
categories:
  - Python core
authors:
  - saeidamiri1
---

# Adding new column to data-frame
A column can easily be added to data-frame
<!-- more -->
```
df0=pd.DataFrame([38,40,25,33])
df['Ave_hour']=df0
```

Using ```assign() ``` can also add new columns, new columns can be generated using functions, see below
```
df=df.assign(Ave_hour=df0)
df=df.assign(PI1=lambda x: x['population']*x['median_income'],PI2=df['population']/df['median_income'] )
```

A new column can be added to data-frame
```
df.columns=['population1','median_income','Ave_hour','PI1','PI2']
df=df.rename(columns={'population1': 'pop', 'median_income': 'med_income'})
```