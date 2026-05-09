import pandas as pd
import numpy as np
# student={
#     "Name":['Alice','Bob','Charlie','David','Eve'],
#     "Age":[25,30,35,40,45],
#     "City":['New York','Los Angeles','Chicago','Houston','Phoenix'],
#     "Class":[10,11,12,10,11],
#     "Grade":['A','B','C','A','B']
# }
# employee={
#     "Name":['Frank','Grace','Heidi','Ivan','Judy'],
#     "Age":[50,55,60,65,70],
#     "City":['Seattle','Boston','Denver','Miami','Atlanta'],
#     "Department":['HR','IT','Finance','Marketing','Sales'],
#     "Salary":[100000,110000,120000,130000,140000]
# }
# df_student=pd.DataFrame(student)
# df_employee=pd.DataFrame(employee)
# print("\n===== STUDENT DATAFRAME =====")
# print(df_student)
# print("\n===== EMPLOYEE DATAFRAME =====")
# print(df_employee)

salary={
    "Name":['Alice','Bob','Charlie','David','Eve'],
    "Salary":[50000,60000,70000,80000,90000]
}
department={
    "Name":['Alice','Bob','Charlie','David','Eve'],
    "Department":['HR','IT','Finance','Marketing','Sales']
}
df_salary=pd.DataFrame(salary)
df_department=pd.DataFrame(department)
print("\n===== SALARY DATAFRAME =====")
print(df_salary)
print("\n===== DEPARTMENT DATAFRAME =====")
print(df_department)
print(pd.merge(df_salary,df_department,on="Name"))