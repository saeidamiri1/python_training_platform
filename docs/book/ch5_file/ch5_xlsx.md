---
title: XLSX
---
# XLSX

## Import using Panda
You can the panda library function `read_excel()` to import Excel files into a DataFrame

```Python
import pandas as pd
DF = pd.read_excel('path/file.xlsx', 1) # 1 is the ix of the worksheet
```

## Import Using openpyxl
To read Excel files (.xls format) in Python, you can use the _openpyxl_ package: 

``` Python
import openpyxl
import pandas as pd
dataframe = openpyxl.load_workbook("./data/chapter5/titianic.xlsx")
sheet1 = dataframe['Sheet1']
rows_sheet1 = []
for row_sheet1 in sheet1.iter_rows(values_only=True):
    rows_sheet1.append(row_sheet1)
df_sheet1 = pd.DataFrame(rows_sheet1[1:], columns=rows_sheet1[0])

sheet2 = dataframe['Sheet2']
rows_sheet2 = []
for row_sheet2 in sheet2.iter_rows(values_only=True):
    rows_sheet2.append(row_sheet2)
df_sheet2 = pd.DataFrame(rows_sheet2[1:], columns=rows_sheet2[0])
```

## Combining files 
To combine .xlsx files, use the following code:
```Python
marketing_analyst_names = pd.read_excel("MarketingAnalystNames.xlsx")
sales_rep_names = pd.read_excel("SalesRepNames.xlsx")
senior_leadership_names = pd.read_excel("SeniorLeadershipNames.xlsx")
all_df_list = [marketing_analyst_names, sales_rep_names, senior_leadership_names]
appended_df = pd.concat(all_df_list)
```
Merge all the dataframes in all_df_list, Pandas will automatically append based on similar column names.
 Write the appended dataframe to an excel file

```Python
appended_df.to_excel("AllCompanyNames.xlsx", index=False)
```

Add `index=False` parameter to not include row numbers
