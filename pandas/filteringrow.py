import pandas as pd
data={
    "name":['Alice','Bob','Charlie','David','Eve','Frank','Grace'],
    "age":[25,43,35,40,45,50,55],
    "city":['New York','Phoenix','Chicago','Houston','Phoenix','Seattle','Boston'],
    "salary":[50000,60000,70000,80000,90000,100000,110000],
    "date":['2025-01-01','2025-02-10','2025-03-15','2025-04-20','2025-05-25','2025-06-30','2025-07-31'],
    "gender":['F','M','M','M','F','M','F']

}
df=pd.DataFrame(data)
print(df)
print(df[(df["age"]>40) & (df["city"]=="Phoenix")])

