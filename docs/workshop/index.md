# Data Analysis using Python
## About this short workshop
This workshop provides valuable insights for individuals starting their data analysis journey with Python. We will be using IPython notebooks that are compatible with both Visual Studio Code (VSCode) and Jupyter environments. To access the workshop, click on the provided link, which will open in Google Colab.

## contents
- [Part I](#part-i) 
- [Part II](#part-ii) 
- [Data set](#data-set) 


## Part I
* [Starting With Data](./notebooks/01-starting-with-data.ipynb) (notebook on colab [`01-starting-with-data.ipynb`](https://colab.research.google.com/github/saeidamiri1/Python-for-Data-Analysis/blob/main/notesbooks/01-starting-with-data.ipynb))
  * [Exercise 1](./exercises/01-exercise.ipynb) (Exercise on colab [`01-excercise.ipynb`](https://colab.research.google.com/github/saeidamiri1/Python-for-Data-Analysis/blob/main/exercises/01-excercise.ipynb))
* [Working With Data](./notebooks/02-working-with-data.ipynb) (notebook on colab [`02-working-with-data.ipynb`](https://colab.research.google.com/github/saeidamiri1/Python-for-Data-Analysis/blob/main/notesbooks/02-working-with-data.ipynb))
  * [Exercise 2](./exercises/02-exercise.ipynb) (Exercise on colab [`02-exercise.ipynb`](https://colab.research.google.com/github/saeidamiri1/Python-for-Data-Analysis/blob/main/exercises/02-exercise.ipynb))
* [Manipulating data-frame](./notebooks/03-manipulating-data-frame.ipynb) (notebook on colab [`03-manipulating-data-frame.ipynb`](https://colab.research.google.com/github/saeidamiri1/Python-for-Data-Analysis/blob/main/notesbooks/03-manipulating-data-frame.ipynb))
  * [Exercise 3](./exercises/03-exercise.ipynb) (Exercise on colab [`03-exercise.ipynb`](https://colab.research.google.com/github/saeidamiri1/Python-for-Data-Analysis/blob/main/exercises/03-exercise.ipynb))

## Part II
* [Summarizing](./notebooks/04-summarizing.ipynb) (notebook on colab [`04-summarizing.ipynb`](https://colab.research.google.com/github/saeidamiri1/Python-for-Data-Analysis/blob/main/notesbooks/04-summarizing.ipynb))
  * [Exercise 4](./exercises/04-exercise.ipynb) (Exercise on colab [`04-exercise.ipynb`](https://colab.research.google.com/github/saeidamiri1/Python-for-Data-Analysis/blob/main/exercises/04-summarizing.ipynb))
* [Merging data-frame](./notebooks/05-merging-data-frame.ipynb) (notebook on colab [`05-merging.ipynb`](https://colab.research.google.com/github/saeidamiri1/Python-for-Data-Analysis/blob/main/notesbooks/05-merging-data-frame.ipynb))
  * [Exercise 5](./exercises/05-exercise.ipynb) (Exercise on colab [`05-exercise.ipynb`](https://colab.research.google.com/github/saeidamiri1/Python-for-Data-Analysis/blob/main/exercises/05-exercise.ipynb))
* [Visualization](./notebooks/06-visualization.ipynb) (notebook on colab [`06-visualization.ipynb`](https://colab.research.google.com/github/saeidamiri1/Python-for-Data-Analysis/blob/main/notesbooks/06-visualization.ipynb))
  * [Exercise 6](./exercises/06-exercise.ipynb) (Exercise on colab [`06-exercise.ipynb`](https://colab.research.google.com/github/saeidamiri1/Python-for-Data-Analysis/blob/main/exercises/06-exercise.ipynb))

## Data set
### California housing dataset 
In this context, we make use of a tailored version of the California housing dataset for practice. This dataset is stored as a `.csv` file, where each row contains information about a particular strict. The columns in the dataset represent:


| Columns        |       
-----------------| 
`longitude`
`latitude`       
`housing_median_age`
`total_rooms`
`total_bedrooms`
`households`
`median_income`
`median_house_value`

The first two rows of `data/HTC.csv` look line as below:

```
"longitude","latitude","housing_median_age","total_rooms","total_bedrooms","population","households","median_income","median_house_value"
-114.310000,34.190000,15.000000,5612.000000,1283.000000,1015.000000,472.000000,1.493600,66900.000000
-114.470000,34.400000,19.000000,7650.000000,1901.000000,1129.000000,463.000000,1.820000,80100.000000
```
### Titanic dataset 
For this exercise, we utilize the Titanic dataset, which is stored as a `.csv`  file. In this dataset, each row contains information about a specific passenger, while the columns represent:


| Columns        |       |
-----------------| ----| 
`PassengerId` |  Passenger id
`Survived`      | 0 = No; 1 = Yes
`Pclass` | Passenger Class (1 = 1st; 2 = 2nd; 3 = 3rd)
`Name` |  Passenger name
`Sex` |  Passenger gender
`Age` |  Passenger age
`SibSp` | Number of Siblings/Spouses Aboard
`Parch` | Number of Parents/Children Aboard
`Ticket` | Ticket Number
`Fare` |  Passenger fare
`Cabin` |   Cabin number
`Embarked` | Port of Embarkation (C = Cherbourg; Q = Queenstown; S = Southampton)



