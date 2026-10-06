import pandas as pd

data = {
    "Name": ["A", "B", "C", "C", "D"],
    "Age": [20, 21, None, None, 22],
    "Gender": ["Male", "Female", "Male", "Male", "male"],
    "Marks": [80, 75, 90, 90, None]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

# Handle missing values
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

# Remove duplicate records
df = df.drop_duplicates()

# Correct inconsistent values
df["Gender"] = df["Gender"].str.capitalize()

print("\nCleaned Dataset:")
print(df)