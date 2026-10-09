import pandas as pd

# Load the CSV dataset
df = pd.read_csv("students.csv")

# 1. Display first 5 records
print("First 5 Records:")
print(df.head())

# 2. Display last 5 records
print("\nLast 5 Records:")
print(df.tail())

# 3. Display dimensions (rows and columns)
print("\nDimensions (Rows, Columns):")
print(df.shape)

# 4. Display column names
print("\nColumn Names:")
print(df.columns)

# 5. Display data types of each column
print("\nData Types:")
print(df.dtypes)

# 6. Check missing values in each column
print("\nMissing Values:")
print(df.isnull().sum())

# 7. Display summary statistics
print("\nSummary Statistics:")
print(df.describe())

# 8. Display basic information about dataset
print("\nDataset Information:")
df.info()