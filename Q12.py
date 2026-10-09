import statistics

# Marks of 20 students
marks = [45, 56, 67, 78, 89, 56, 72, 90, 67, 56,
         81, 75, 67, 88, 92, 56, 70, 67, 85, 60]

# Calculate Mean (Average)
mean = statistics.mean(marks)

# Calculate Median (Middle value)
median = statistics.median(marks)

# Calculate Mode (Most frequently occurring value)
mode = statistics.mode(marks)

# Display the results
print("Marks:", marks)
print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)