import pandas as pd

data = {
    "Age": [20,21,19,22,20,21,23,20,19,22,
            21,20,22,19,23,21,20,22,21,19],

    "Gender": ["M","F","M","F","M","F","M","F","M","F",
               "M","F","M","F","M","F","M","F","M","F"],

    "Attendance": [85,90,78,88,92,75,80,95,83,87,
                   89,91,76,84,93,88,79,86,90,82],

    "Study_Hours": [3,4,2,5,6,2,3,5,4,3,
                    4,6,2,3,5,4,2,5,6,3],

    "Internal_Marks": [25,28,22,27,29,21,24,30,26,25,
                       28,29,20,24,30,27,23,28,29,25],

    "Final_Marks": [65,75,55,78,82,50,62,88,70,68,
                    76,85,52,64,90,79,58,81,84,67]
}

df = pd.DataFrame(data)

df.to_csv("student_data.csv", index=False)

print("Data collected successfully.")
print(df)