import pandas as pd # Data Calci

data = {
    "Name": ["Alex", "Ironman", "Thor", "Hulk", "Batsman"],
    "Roll_No": [101, 102, 103, 104, 105],
    "Marks": [85, 72, 91, 65, 78],
    "Attendance": [90, 82, 95, 75, 88]
}

df = pd.DataFrame(data) # convert data into table 

print("Student Dataset:")
print(df)

# Data
print("\nData:")
print(df["Marks"].tolist())

# Information
print("\nInformation:")
print("Average Marks:", df["Marks"].mean())
print("Average Attendance:", df["Attendance"].mean())

# Knowledge
print("\nKnowledge:")
top_student = df.loc[df["Marks"].idxmax(), "Name"]
print(top_student, "has the highest marks.")
