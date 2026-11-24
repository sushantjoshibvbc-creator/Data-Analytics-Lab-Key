import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    'Name': ['Aman', 'Riya', 'Raj', 'Simran', 'Karan'],
    'Hours': [2, 4, 5, 3, 6],
    'Marks': [50, 70, 85, 60, 95],
    'Attendance': [70, 85, 90, 75, 95]
}

df = pd.DataFrame(data)

# 1. Bar Chart
plt.bar(df['Name'], df['Marks'])
plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

# 2. Line Chart
plt.plot(df['Name'], df['Marks'], marker='o')
plt.title("Student Performance")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

# 3. Histogram
plt.hist(df['Marks'], bins=5)
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter Plot
sns.scatterplot(data=df, x='Hours', y='Marks')
plt.title("Study Hours vs Marks")
plt.show()

# 5. Heatmap
sns.heatmap(df[['Hours', 'Marks', 'Attendance']].corr(),
            annot=True)
plt.title("Correlation Heatmap")
plt.show()