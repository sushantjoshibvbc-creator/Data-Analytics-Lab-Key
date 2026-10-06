# Numpy Numbers operations perform ie Aggeration function, matrix 
# Pandas Data Arrange or Manage  ie CSV se extract

import pandas as pd  # Tables + Data Analysis 

# Step 1: Data Collection
data = {
    "Name": ["A", "B", "C", "D", "E"],
    "Study_Hours": [2, 4, 5, 3, 6],
    "Marks": [50, 65, 75, 60, 85]
}

df = pd.DataFrame(data) # convert data into table 

print("1. Collected Data :")
print(df)

# Step 2: Data Cleaning
df = df.drop_duplicates()

# Step 3: Data Analysis
print("\n2. Average Marks :", df["Marks"].mean())
print("3. Maximum Marks :", df["Marks"].max())

# Step 4: Interpretation
print("4. Interpretation :")

if df["Marks"].mean() >= 60:
    print("Overall student performance is satisfactory.")
else:
    print("Overall student performance needs improvement.")
