import numpy as np
import pandas as pd

# Load dataset
file_path = r"C:\Users\CC\Downloads\employee_data_100.csv"
df = pd.read_csv(file_path)

# Remove duplication
duplication_count = df.duplicated().sum()
print(f"Number of duplicate rows found: {duplication_count}")
df_cleaned = df.drop_duplicates().copy()
print(f"Original shape: {df.shape}, Cleaned shape: {df_cleaned.shape}")

# Handle Missing values :
print("\nMissing values per column:")
print(df_cleaned.isnull().sum())

# Input numeric missing values
median_age = df_cleaned["Age"].median()
df_cleaned["Age"] = df_cleaned["Age"].fillna(median_age)
df_cleaned["Join_Date"] = pd.to_datetime(df_cleaned["Join_Date"])

# Split Full Name into First_Name and Last_Name
df_cleaned[["First_Name", "Last_Name"]] = df_cleaned["Full Name"].str.split(" ", expand=True, n=1)
df_cleaned["Join_Year"] = df_cleaned["Join_Date"].dt.year
df_cleaned = df_cleaned.drop(columns=["Full Name"])

# REORDER COLUMNS LOGICALLY (Fixed names to match DataFrame columns perfectly)
ordered_columns = [
    "Employee_ID",
    "First_Name",
    "Last_Name",
    "Department",
    "Age",
    "Salary",
    "Join_Date",
    "Join_Year"
]
df_cleaned = df_cleaned[ordered_columns]

# OUTPUT
print("\n--------PROCESSING DATAFRAME---------")
print(df_cleaned.dtypes)   
print("\nFinal Cleaned DataFrame Preview:")
print(df_cleaned.head())
