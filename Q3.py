import pandas as pd

# 1. Discovery
print("1. Discovery : Analyze student performance.")

# 2. Data Preparation
data = {
    "Student": ["A", "B", "C", "D", "E"],
    "Study_Hours": [2, 4, 5, 3, 6],
    "Marks": [50, 65, 75, 60, 85]
}

df = pd.DataFrame(data)

# 3. Model Planning
print("\n2. Data Preparation completed.")

# 4. Model Building
average_marks = df["Marks"].mean()

print("\n3. Average Marks:", average_marks)

# 5. Communicate Results
print("\n4. Communication :")
print("Students with higher study hours generally have higher marks.")

# 6. Operationalize
print("\n5. Operationalize :")
print("Use the analysis to improve student study planning.")
