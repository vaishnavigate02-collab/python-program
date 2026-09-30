import pandas as pd


data = {
    "Student Name": ["Amit", "Rahul", "Priya", "Sneha", "Rohan"],
    "Height": [170, 165, 158, 162, 175]
}


df = pd.DataFrame(data)


print("Student Dataset:")
print(df)


print("\nFirst 5 rows:")
print(df.head())

print("\nDataset Information:")
print(df.info())

print("\nNumber of rows and columns:")
print(df.shape)

print("\nColumn names:")
print(df.columns)


print("\nDescriptive Statistics:")
print(df.describe())


print("\nAverage Height:")
print(df["Height"].mean())


print("\nShortest Height:")
print(df["Height"].min())

print("\nTallest Height:")
print(df["Height"].max())
