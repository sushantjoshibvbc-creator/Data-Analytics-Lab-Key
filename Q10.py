import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler

data = {
    "Marks": [50, 60, 70, 80, 90],
    "Attendance": [60, 70, 80, 90, 100]
}

df = pd.DataFrame(data)

# Normalization
scaler = MinMaxScaler()
df["Marks_Normalized"] = scaler.fit_transform(df[["Marks"]])

# Standardization
standard_scaler = StandardScaler()
df["Marks_Standardized"] = standard_scaler.fit_transform(
    df[["Marks"]]
)

# Aggregation
print("Average Marks:", df["Marks"].mean())

# Discretization
df["Marks_Category"] = pd.cut(
    df["Marks"],
    bins=[0, 60, 80, 100],
    labels=["Low", "Medium", "High"]
)

print("\nTransformed Dataset:")
print(df)