---
date: 2024-10-26
title: Cheat Sheet of Sklearn 
description: A brief of Useful functions of Sklearn
categories:
  - Cheat Sheet
authors:
  - saeidamiri1
---

<!-- ## Contents
- [Sklearn](#Sklearn)
  - [Training and Test set](#Training-And-Test-set)
  - [Preprocessing Data](#preprocessing-data)
  - [Modeling](#Modeling)
    - [Building model](#Building-model)
    - [Fitting model to Data](#Fitting-model-to-Data) 
    - [Predicting](#Predicting)
    - [Evaluation](#Evaluation)  
    - [Tuning Model](#Tuning-Model) -->

# Sklearn 
Sklearn is built for general machine learning.

<!-- more -->

|||
|---|---|
```import sklearn``` | 
```pip3 install sklearn ```|
```python3 -m pip install --upgrade  sklearn``` |

## Training and test set

```from sklearn.model_selection import train_test_split```
|||
|---|---|
```X_train, X_test, Y_train, Y_test =train_test_split(X,Y,test_size=.2)```| Split arrays or matrices to training and testing sets,  |

## Preprocessing Data
```from sklearn import preprocessing```

### Standardization 

Normalize each column individually to unit norm.
|||
|---|---|
```st_scaler = preprocessing.StandardScaler().fit(X_train)```| Calculate the mean (m) and std (s) from X_train columns
```stand_X = st_scaler.transform(X)```|  Standardize X using m and s

### Normalization
Normalize row individually to unit norm.

|||
|---|---|
```nr_scaler = preprocessing.Normalizer().fit(X_train)```| Calculate the mean (m) and std (s) from X_train rows
```normal_X = nr_scaler.transform(X)```|  Normalize X using m and s

### Binarization
Binarize the data for a given threshold.

|||
|---|---|
```bn = preprocessing.Binarizer(threshold=0.0).fit(X)```| Define binarization for a given threshold
```bin_X = bn.transform(X)```| Run binarization on X

### Encoding
Relabel the elements of array to integer number
|||
|---|---|
```le = preprocessing.LabelEncoder()```| Assign the label coding function to le 
```y = le.fit_transform(y)```| Run transformation on y


## Modeling
### Building model

```from sklearn.linear_model import LinearRegression```
|||
|---|---|
```lr = LinearRegression(normalize=True)```| Create linear model|
|```from sklearn.svm import SVC```<br> 
```svc = SVC(kernel='linear')```| Create support vector machine for classification|
|```from sklearn import neighbors```<br> 
```knn = neighbors.KNeighborsClassifier(n_neighbors=4)```| Create Knn |
|```from sklearn.cluster import KMeans``` <br>
```k_means = KMeans(n_clusters=4, random_state=0)```| Create KMeans |

### Fitting model to Data

|||
|---|---|
|```lr.fit(X_train, Y_train)```| Fit linear model|
|```svc.fit(X_train, Y_train)```| fit SVC|
|```knn.fit(X_train, Y_train)```| fit knn|
|```k_means.fit(X_train)```| Fit KMeans|


### Predicting 

|||
|---|---|
|```Y_pred = lr.predict(X_test)```| Predict using linear
|```Y_pred = svc.predict(X_test) ```| Predict using SVC
|```Y_pred = knn.predict_proba(X_test)```| Predict using Knn
|```Y_pred = k_means.predict(X_test)```| Predict using KMeans

### Evaluation 
#### Linear model

```from sklearn.metrics import mean_absolute_error, mean_squared_error,r2_score```
|||
|---|---|
```mean_absolute_error(Y_test, Y_pred)```| Calculate MAE
```mean_squared_error(Y_test, Y_pred)```| Calculate MSE
```r2_score(Y_test, Y_pred)``` | Calculate  R-square

#### Classification

```from sklearn.metrics import accuracy_score,classification_report,confusion_matrix```
|||
|---|---|
```accuracy_score(Y_test, Y_pred)```|Calculate accuracy|
```classification_report(Y_test, Y_pred)```| Calculate different classification metrics|
```confusion_matrix(Y_test, Y_pred)```| Calculate the confusion matrix

#### Clustering

```from sklearn.metrics import adjusted_rand_score,homogeneity_score,v_measure_score```
|||
|---|---|
```adjusted_rand_score(Y_true, Y_pred)```|  Calculate adjusted_rand_score
```homogeneity_score(Y_true, Y_pred)```| Calculate homogeneity_score
```v_measure_score(Y_true, Y_pred)```| Calculate v_measure_score

#### Crosse-validation

```from sklearn.cross_validation import cross_val_score```
|||
|---|---|
|```cross_val_score(lr, X_train, Y_train, cv=2)```| Cross-validation on linear model
|```cross_val_score(knn, X_train, Y_train, cv=4)```|Cross-validation on Knn

### Tuning Model
#### Grid Search

```from sklearn.grid_search import GridSearchCV```
|||
|---|---|
```params = {"n_neighbors": np.arange(1,3),"metric": ["euclidean", "cityblock"]}```| Define parameters
```grid = GridSearchCV(estimator=knn,param_grid=params)```| Define estimator
```grid.fit(X_train, y_train)```| Fit to training set
```print(grid.best_score_)```| print the best score
```print(grid.best_estimator_.n_neighbors)```| Print the estimate of parameters

#### Randomized parameter optimization

```from sklearn.grid_search import RandomizedSearchCV```
|||
|---|---|
```params = {"n_neighbors": range(1,5),"weights": ["uniform", "distance"]}```|  Define parameters
```rand_search = RandomizedSearchCV(estimator=knn, param_distributions=params, cv=4, n_iter=8,random_state=5)```|  Define estimator
```rand_search.fit(X_train, y_train)```| Fit to training set
```print(rand_search.best_score_)```| print the best score
```print(grid.best_estimator_.n_neighbors)```| Print the estimate of parameters


<!-- **[⬆ back to top](#contents)**
## References

### License
Copyright (c) 2019 Saeid Amiri and Leila Alimehr -->
