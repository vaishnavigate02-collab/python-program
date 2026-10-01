import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Load data and clean
df = sns.load_dataset("penguins")
print(df.head(10))
df = df.dropna()
print(df.head(10))
print(df.info())

# Create a scatter plot
plt.figure(figsize=(7, 5))
sns.scatterplot(
    data=df,
    x="bill_length_mm",
    y="bill_depth_mm",
    hue="species",
)
plt.title("Scatter plot: Bill Length vs. Bill Depth")
plt.xlabel("Bill Length (mm)")
plt.ylabel("Bill Depth (mm)")
plt.show()

# Create a correlation heatmap
plt.figure(figsize=(6, 5))
numeric_data = df.select_dtypes(include="number")
correlation_matrix = numeric_data.corr()
sns.heatmap(
    correlation_matrix,
    annot=True,
    cmap="coolwarm",
    fmt=".2f",
)
plt.title("Correlation Heatmap")
plt.show()
