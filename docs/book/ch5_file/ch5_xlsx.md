---
title: XLSX
---
# xlsx

### Import xlsx into Pandas
```{Python, echo = FALSE, message = FALSE}
import pandas as pd
DF = pd.read_excel('path/file.xlsx', 1) # 1 is the ix of the worksheet
```

To read Excel files (.xls format) in Python, you can use the _xlrd_ package, which is a popular library for working with Excel files. However, newer Excel formats (.xlsx), the _openpyxl_ library was more commonly used. 
```
import openpyxl
import pandas as pd
dataframe = openpyxl.load_workbook("../data/titianic.xlsx")
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

```
import xlrd
xls_book = xlrd.open_workbook('../data/titianic.xlsx')
sheet1=xls_book['Sheet1']
sheet2=xls_book['Sheet2']
data_sheet1 = []
for i in range(sheet1.nrows):
    row_sheet1 = []
    for j in range(sheet1.ncols):
        row_sheet1.append(sheet1.cell_value(i, j))
    data_sheet1.append(row_sheet1)
df_sheet1 = pd.DataFrame(data_sheet1[1:], columns=data_sheet1[0])
data_sheet2 = []
for i in range(sheet2.nrows):
    row_sheet2 = []
    for j in range(sheet2.ncols):
        row_sheet2.append(sheet2.cell_value(i, j))
    data_sheet2.append(row_sheet2)
df_sheet2 = pd.DataFrame(data_sheet2[1:], columns=data_sheet2[0])
```

### Combining files 
```{Python, echo = FALSE, message = FALSE}
marketing_analyst_names = pd.read_excel("MarketingAnalystNames.xlsx")
sales_rep_names = pd.read_excel("SalesRepNames.xlsx")
senior_leadership_names = pd.read_excel("SeniorLeadershipNames.xlsx")
all_df_list = [marketing_analyst_names, sales_rep_names, senior_leadership_names]
appended_df = pd.concat(all_df_list)
```
Merge all the dataframes in all_df_list, Pandas will automatically append based on similar column names.
 Write the appended dataframe to an excel file

```{Python, echo = FALSE, message = FALSE} 
appended_df.to_excel("AllCompanyNames.xlsx", index=False)
```

Add `index=False` parameter to not include row numbers
