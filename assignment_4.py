import numpy as np
import pandas as pd

raw_data ={
 "Employee_ID": [101, 102, 103, 104, 105, 106],
    "Full Name": [
        "Alice Smith",

    ],
    "Departement": ["HR", "IT", "Finance", " Finance", "None", "IT", "HR"],
    "Age": [
        "Alice Smith",
        "Bob Jones",
        "Charlie Brown",
        "Charlie Brown",
        "David Miller",
        "Eva Green",
        "Frank Wright",
],
"Department": [ "HR", "IT", "Finance","Finance",None,"IT","HR"],
"Age": [28, 34, np.nan, np.nan, 45, 29, 52],
"Salary": [55000, 72000, 68000, 85000, np.nan, 91000],
"Join_Date": [
    "2021-01-15",
    "2020-03-22",
    "2019-07-11",
    "2019-07-11",
    "2018-11-05",
    "2022-05-01",
    "2015-09-30",
    ],
}

df=pd.DataFrame(raw_data)
print("----ORIGINAL DATA----")
print(df)
print("\n" + "=" * 50 + "\n")
print(df.head())
print("\n" + "=" * 50 + "\n")


# ----------------------------------------------------------------------------------------------------------
# 2. REMOVE DUPLICATES
# --------------------------------------------------------------------------------------------------------
# Check for exact duplicate rows across all or specific columns
duplicate_count = df.duplicated().sum()
print(f"Number of duplicate rows found: {duplicate_count}")

#Drop Duplicates (keeping the first accurate)
df_cleaned = df.drop_duplicates().copy()

print(df_cleaned)
# ------------------------------------------------------------------------------------------------------------
# 3. HANDLE MISSING VALUES (NaN / None)
# ------------------------------------------------------------------------------------------------------------
# Check missing value count per column
print("\nMissing values per column:")
printf(df_cleaned.isnull().sum())

# Statergy A: Impute numerical missing values using median
medain_age = df_cleaned["Age"].median()
df_cleaned["Age"] = df_cleaned["Age"].fillna(medain_age)

#Stratergy B: Impute numerical missing values using Mean
mean_salary = df_cleaned["Salary"].mean()
df_cleaned["salary"] = df_cleaned["Salary"].fillna(mean_salary)

# Stratergy C: Fill categorical missing values with a placeholder or Mode
df_cleaned["Salary"] = df_cleaned["Salary"].fillna("Unassigned")


# ---------------------------------------------------------------------------------------------
# 4.MODIFY DATA STRUCTURES & CLEAN FORMATS
# ---------------------------------------------------------------------------------------------
# A. String cleaning: Strip whitespace and convert text case
df_cleaned["Full Name"] = df_cleaned["Full Name"].str.strip().str.title()

# B. Type conversion: Cast Join_Date string to datetime
df_cleaned["Join_Date"] = pd.to_datetime(df_cleaned["Join_Date"])

# C. Column Splitting: Split 'Full Name' into 'First_Name' and 'Last_Name'
df_cleaned[["First_Name", "Last_Name"]] =  df_cleaned["Full Name"].str.split(",", expand=True)

#D. Feature Enginnering: Extract 'Join_Year' from datetime
df_cleaned["Join_Year"] = df_cleaned["Join_Date"].dt.year

#E. Reorder Columns logically
ordered_columns = [
    "Employee_ID",
    "Full Name",
    "Last_Name",
    "First_Name",
    "Departement",
    "Age",
    "Salary",
    "Join_Date",
    "Join_Year",
]
df_cleaned = df_cleaned[ordered_columns]


# ----------------------------------------------------------------------------------------------------------
# 5. FINAL OUTPUT
# ----------------------------------------------------------------------------------------------------------
print("\n---- PROCESSED DATAFRAME----")
print(df_cleaned)

print("\n---- DATA TYPES INFO -----")
print(df_cleaned.dtypes)
