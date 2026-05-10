import pandas as pd
import numpy as np
data={
    "datae":['2025-01-01','2025-02-10','2025-03-15','2025-04-20','2025-05-25','2025-06-30','2025-07-31'],
    "product":['A','B','C','A','B','C','A'],
    "region":['North','South','East','West','North','South','East'],
    "sales":[100,200,150,300,250,350,400],
    "units":[10,20,15,30,25,35,40],
    "profit":[20,40,30,60,50,70,80],
    "discount":[5,10,7,15,12,18,20],
    "customer":[1001,1002,1003,1004,1005,1006,1007]
}

df=pd.DataFrame(data)
print(df)
pivot_table=df.pivot_table(values='sales', index='product', columns='region', aggfunc='sum')
print(pivot_table)
pivot_table2=df.pivot_table(values=['profit', 'units'], index='product', columns='region', aggfunc='mean')
print(pivot_table2)
crosstab= pd.crosstab(df['product'], df['region'], values=df['sales'], aggfunc='sum')
print(crosstab)