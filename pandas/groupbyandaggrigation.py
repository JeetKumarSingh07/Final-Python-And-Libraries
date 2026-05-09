import pandas as pd
import numpy as np
data={
    "name":['Alice','Bob','Charlie','David','Eve','Frank','Grace'],
    "age":[25,43,35,40,45,50,55],
    "city":['New York','Phoenix','Chicago','Houston','Phoenix','Seattle','Boston'],
    "salary":[50000,60000,70000,80000,90000,100000,110000],
    "date":['2025-01-01','2025-02-10','2025-03-15','2025-04-20','2025-05-25','2025-06-30','2025-07-31'],
    "gender":['F','M','M','M','F','M','F']
}
df=pd.DataFrame(data)
# print(df)
# print(df.groupby("city")["salary"].mean())  #group by city and calculate mean salary
# print(df.groupby("gender")["age"].max())  #group by gender and calculate max age
# print(df.groupby("city")["age"].min())  #group by city and calculate min age
# print(df.groupby("gender")["salary"].sum())  #group by gender and calculate total salary
# print(df.aggregate({"age":"sum","salary":"sum"}))  #aggregate age sum and salary sum
print(df['age'].agg(['min','max','mean']))  #aggregate age min, max and mean