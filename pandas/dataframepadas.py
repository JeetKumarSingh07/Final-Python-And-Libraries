import pandas as pd 
print(pd.__version__)

import pandas as pd
import numpy as np

# =========================================================
# CREATE DATAFRAME
# =========================================================

data = {
    "Name": ["Prince", "Rahul", "Aman", "Neha", "Karan"],
    "Age": [20, 21, 22, np.nan, 24],
    "City": ["Delhi", "Mumbai", "Pune", "Delhi", "Mumbai"],
    "Department": ["IT", "HR", "IT", "Finance", "HR"],
    "Salary": [50000, 60000, 70000, 80000, 90000],
    "Date": ["2025-01-01", "2025-02-10", "2025-03-15", "2025-04-20", "2025-05-25"]
}

df = pd.DataFrame(data)

# =========================================================
# VIEW DATA
# =========================================================

print("\n===== ORIGINAL DATAFRAME =====")
print(df)

print("\n===== HEAD =====")
print(df.head())

print("\n===== TAIL =====")
print(df.tail(3))

print("\n===== SHAPE =====")
print(df.shape)

print("\n===== COLUMNS =====")
print(df.columns)

print("\n===== INFO =====")
print(df.info())

print("\n===== DESCRIBE =====")
print(df.describe())

# =========================================================
# SELECTING DATA
# =========================================================

print("\n===== SINGLE COLUMN =====")
print(df["Name"])

print("\n===== MULTIPLE COLUMNS =====")
print(df[["Name", "Salary"]])

print("\n===== SELECT ROW USING LOC =====")
print(df.loc[0])

print("\n===== SELECT USING ILOC =====")
print(df.iloc[1])

print("\n===== SPECIFIC VALUE =====")
print(df.loc[0, "Name"])

# =========================================================
# FILTERING
# =========================================================

print("\n===== FILTER AGE > 21 =====")
print(df[df["Age"] > 21])

print("\n===== MULTIPLE CONDITIONS =====")
print(df[(df["Salary"] > 60000) & (df["City"] == "Mumbai")])

# =========================================================
# ADDING COLUMNS
# =========================================================

df["Bonus"] = df["Salary"] * 0.10

print("\n===== ADD BONUS COLUMN =====")
print(df)

# =========================================================
# UPDATE VALUES
# =========================================================

df.loc[0, "Age"] = 25

print("\n===== UPDATED AGE =====")
print(df)

# =========================================================
# DELETE COLUMN
# =========================================================

temp_df = df.drop("Bonus", axis=1)

print("\n===== AFTER DELETING BONUS =====")
print(temp_df)

# =========================================================
# MISSING VALUES
# =========================================================

print("\n===== NULL VALUES =====")
print(df.isnull())

print("\n===== NULL VALUE COUNT =====")
print(df.isnull().sum())

print("\n===== FILL NULL VALUES =====")
print(df.fillna(0))

# =========================================================
# SORTING
# =========================================================

print("\n===== SORT BY SALARY ASC =====")
print(df.sort_values("Salary"))

print("\n===== SORT BY SALARY DESC =====")
print(df.sort_values("Salary", ascending=False))

# =========================================================
# RENAME COLUMN
# =========================================================

renamed_df = df.rename(columns={"Name": "Employee_Name"})

print("\n===== RENAMED COLUMN =====")
print(renamed_df)

# =========================================================
# GROUPBY
# =========================================================

print("\n===== GROUPBY DEPARTMENT =====")
print(df.groupby("Department")["Salary"].mean())

# =========================================================
# MERGE DATAFRAMES
# =========================================================

df1 = pd.DataFrame({
    "ID": [1, 2, 3],
    "Name": ["Prince", "Rahul", "Aman"]
})

df2 = pd.DataFrame({
    "ID": [1, 2, 3],
    "Salary": [50000, 60000, 70000]
})

merged_df = pd.merge(df1, df2, on="ID")

print("\n===== MERGED DATAFRAME =====")
print(merged_df)

# =========================================================
# CONCAT DATAFRAMES
# =========================================================

concat_df = pd.concat([df1, df2])

print("\n===== CONCAT DATAFRAME =====")
print(concat_df)

# =========================================================
# DUPLICATES
# =========================================================

print("\n===== DUPLICATES =====")
print(df.duplicated())

print("\n===== REMOVE DUPLICATES =====")
print(df.drop_duplicates())

# =========================================================
# APPLY FUNCTION
# =========================================================

df["Age"] = df["Age"].apply(lambda x: x + 1)

print("\n===== APPLY FUNCTION =====")
print(df)

# =========================================================
# VALUE COUNTS
# =========================================================

print("\n===== VALUE COUNTS =====")
print(df["City"].value_counts())

# =========================================================
# UNIQUE VALUES
# =========================================================

print("\n===== UNIQUE VALUES =====")
print(df["City"].unique())

print("\n===== NUMBER OF UNIQUE VALUES =====")
print(df["City"].nunique())

# =========================================================
# STRING OPERATIONS
# =========================================================

print("\n===== UPPERCASE NAMES =====")
print(df["Name"].str.upper())

print("\n===== NAME CONTAINS 'P' =====")
print(df[df["Name"].str.contains("P")])

# =========================================================
# DATE OPERATIONS
# =========================================================

df["Date"] = pd.to_datetime(df["Date"])

print("\n===== YEAR FROM DATE =====")
print(df["Date"].dt.year)

# =========================================================
# INDEX OPERATIONS
# =========================================================

print("\n===== SET INDEX =====")
print(df.set_index("Name"))

print("\n===== RESET INDEX =====")
print(df.reset_index())

# =========================================================
# BOOLEAN INDEXING
# =========================================================

print("\n===== SALARY > 60000 =====")
print(df[df["Salary"] > 60000])

# =========================================================
# AGGREGATE FUNCTIONS
# =========================================================

print("\n===== SUM =====")
print(df["Salary"].sum())

print("\n===== MEAN =====")
print(df["Salary"].mean())

print("\n===== MAX =====")
print(df["Salary"].max())

print("\n===== MIN =====")
print(df["Salary"].min())

# =========================================================
# PIVOT TABLE
# =========================================================

pivot = pd.pivot_table(
    df,
    values="Salary",
    index="Department",
    aggfunc="mean"
)

print("\n===== PIVOT TABLE =====")
print(pivot)

# =========================================================
# CROSSTAB
# =========================================================

cross = pd.crosstab(df["Department"], df["City"])

print("\n===== CROSSTAB =====")
print(cross)

# =========================================================
# SAMPLE
# =========================================================

print("\n===== RANDOM SAMPLE =====")
print(df.sample(2))

# =========================================================
# QUERY
# =========================================================

print("\n===== QUERY AGE > 22 =====")
print(df.query("Age > 22"))

# =========================================================
# MEMORY USAGE
# =========================================================

print("\n===== MEMORY USAGE =====")
print(df.memory_usage())

# =========================================================
# CHANGE DATATYPE
# =========================================================

df["Age"] = df["Age"].astype(float)

print("\n===== CHANGED DATATYPE =====")
print(df.dtypes)

# =========================================================
# EXPORT FILES
# =========================================================

df.to_csv("output.csv", index=False)

# Uncomment if openpyxl installed
# df.to_excel("output.xlsx", index=False)

print("\n===== FILE EXPORTED SUCCESSFULLY =====")