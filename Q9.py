import pandas as pd

data = {
    "Age": [20, 21, None, 22, 23],
    "Gender": ["Male", "Female", "Male", "Female", "Male"],
    "Marks": [80, 75, 90, None, 85]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

# Missing values
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

# Convert categorical variable into numerical variable
df["Gender"] = df["Gender"].map({
    "Male": 1,
    "Female": 0
})

print("\nPreprocessed Data:")
print(df)