import pandas as pd
import numpy as np
df=pd.read_csv(r'anime.csv')
# print(df.head())
# print(df.shape)
print(df.loc[4])
def extract_episodes(txt):
    check=False
    data=''
    for i in txt:
        if i==")":
            check=False
            return data
        if check:
            data+=i
        if i=="(":
            check=True
df['Episodes']=df['Title'].apply(extract_episodes)
# # print(df.head())
# print(df['Episodes'])
# print(df['Episodes'].value_counts())
# print(df['Episodes'].str.replace(" eps", ""))

df['Episodes']=df['Episodes'].str.replace(" eps", "").astype(int)
print(df['Episodes'])
print(df)
