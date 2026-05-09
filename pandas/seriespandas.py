import pandas as pd


# #-----------------------creating series from list, array and dict--------------------------------------------
# label=['a','b','c','d','e']
# mylist=[10,20,30,40,50]
# myarray=[1,2,3,4,5]
# dict={'a':10,'b':20,'c':30,'d':40,'e':50}
# s=pd.Series(label)
# print(s)
# s1=pd.Series(mylist)
# print(s1)
# s2=pd.Series(myarray)
# print(s2)
# s3=pd.Series(dict)
# print(s3)




# #-----------------------creating labled series from list, array and dict--------------------------------------------
# s4=pd.Series(mylist,index=['abc','def','ghi','jkl','mno'])
# print(s4)
# s5=pd.Series(myarray,index=['abc','def','ghi','jkl','mno'])
# print(s5)
# s6=pd.Series(dict,index=['a','b','c','d','e'])
# print(s6)   
# print(s6['a'])  #accessing element from series using index label
# print(s6[0])    #accessing element from series using index position





#------------ṇ-----------creating dataframe from series--------------------------------------------


# data={'name':['Alice','Bob','Charlie','David','Eve'],   
#       'age':[25,30,35,40,45], 
#       'city':['New York','Los Angeles','Chicago','Houston','Phoenix']}
# df=pd.DataFrame(data)
# print(df)


#------------ṇ-----------creating dataframe from series with custom index--------------------------------------------   
data=[
   ['jeet',18,'Delhi',50000],
   ['rohit',22,'Mumbai',60000],
   ['sneha',28,'Bangalore',75000],
   ['anita',32,'Chennai',80000],
   ['vijay',40,'Kolkata',90000]

]
df=pd.DataFrame(data,index=['emp1','emp2','emp3','emp4','emp5'],columns=['Name','Age','City','Salary'])
# print(df)
# print(df.loc['emp1'])  #accessing row using index label
# print(df.iloc[0])     #accessing row using index position

# df["Rank"]=[1,2,3,4,5]  #adding new column to dataframe
# print(df)
# df.drop("Rank",axis=1,inplace=True)  #deleting column from dataframe
# print(df)
dfdelete=df.drop('emp1',axis=0)  #deleting row from dataframe
print(dfdelete)
dfanother=df.loc['emp1':'emp2']
print(dfanother)
print(df.loc[['emp2','emp3']][['Name','City']])  #selecting specific rows and columns from dataframe
