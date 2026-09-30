import pandas as pd
file_path=r"C:\Users\CC\Downloads\annualdata.csv"
df=pd.read_csv(file_path)
print("Dataset imported successfully !\n",df)
print("="*60)

print("1.first 5 rows")
print("="*60)
print(df.head(),"\n")
print("="*60)

print("2.Dataset dimensions")
print("="*60)
print(f"Rows,Columns: {df.shape}\n")

print("3.Columns name and data types")
print("="*60)
print("="*60)
print(df.dtypes,"\n")
print("="*60)

print("4.Concise summary")
print("="*60)
df.info()
print("\n")
print("="*60)

print("5.Missing values check")
print("="*60)
missing_data=df.isnull().sum()
print(missing_data[missing_data>0]if missing_data[missing_data>0]else "No missing values found.")
print("\n")
print("="*60)

print("6.Duplicate rows check")
print("="*60)
print(f"Number of duplicate rows: {df.duplicated().sum()}\n")
print("="*60)

print("7.Numerical summary statistics")
print("="*60)
print(df.describe().T,"\n")
print("="*60)

print("8.Categorical summary statistics")
print("="*60)
print(df.describe(include=['object','category']),"\n")
print("="*60)

print("9.Value count for categorical columns")
print("="*60)
categorical_cols=df.select_dtypes(include=['object','category']).columns


for col in categorical_cols:
    print(f"-----{col}-----")
    print(df[col].value_counts(),"\n")

    print("="*60)


    print("10. Additional Numeric Metric Metrics")
    print("="*60)
    numeric_cols=df.select_dtypes(include=['number']).columns
    metrics_df=df.select_dtypes(include=['number']).columns

    metrics_df=pd.DataFrame({
        'Mean':df[numeric_cols].mean(),
        'Median':df[numeric_cols].median(),
        'variance':df[numeric_cols].var(),
        'skewness':df[numeric_cols].skew(),
    })
    print(metrics_df,"\n")
    print("="*60)
