import numpy as np
import pandas as pd

# 1. Create a 1D NumPy array
arr1 = np.array([10, 20, 30, 40, 50])
print("One Dimensional Array:")
print(arr1)

# 2. Create a 2D NumPy array
arr2 = np.array([[1, 2, 3],
                 [4, 5, 6]])
print("\nTwo Dimensional Array:")
print(arr2)

# 3. Perform addition, subtraction and multiplication
a = np.array([10, 20, 30])
b = np.array([2, 4, 5])

print("\nAddition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)

# 4. Create a Pandas DataFrame
data = {
    'Name': ['Aman', 'Riya', 'Rahul', 'Priya',
             'Karan', 'Neha', 'Rohit'],
    'Roll_No': [101, 102, 103, 104, 105, 106, 107],
    'Marks': [85, 72, 90, 65, 78, 95, 55]
}

df = pd.DataFrame(data)

# 5. Display first five records
print("\nFirst Five Records:")
print(df.head())

# 6. Calculate maximum, minimum and average marks
print("\nMaximum Marks:", df['Marks'].max())
print("Minimum Marks:", df['Marks'].min())
print("Average Marks:", df['Marks'].mean())

# 7. Filter students scoring more than 75 marks
print("\nStudents Scoring More Than 75 Marks:")
print(df[df['Marks'] > 75])
