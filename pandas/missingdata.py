import pandas as pd
import numpy as np
data={
    "name":['Alice','Bob',np.nan,'David','Eve'],
    "age":[25,30,35,40,45],
    "city":['New York',np.nan,'Chicago','Houston','Phoenix'],
    "salary":[50000,60000,70000,80000,90000],
    "date":['2025-01-01',np.nan,'2025-03-15','2025-04-20',np.nan],
    "gender":['F','M','M','M','F']

}
df=pd.DataFrame(data)
# print(df)
# print(df.isnull())  #check for missing values
# print(df.isnull().sum())  #count of missing values in each column
# print(df.any())  #check if any missing values in dataframe
# print(df.all())  #check if all values are missing in dataframe
# print(df.fillna("Unknown", inplace=True))  #fill missing values with specified value
print(df.dropna())  #drop rows with missing values
print(df.fillna(200))