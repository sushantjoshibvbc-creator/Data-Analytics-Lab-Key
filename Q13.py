import numpy as np
import statistics

# Given dataset
data = [10, 20, 30, 40, 50, 60, 70, 80]

# Calculate Range
data_range = max(data) - min(data)

# Calculate Variance (Population)
variance = statistics.pvariance(data)

# Calculate Standard Deviation (Population)
std_dev = statistics.pstdev(data)

# Calculate Quartiles
Q1 = np.percentile(data, 25)
Q2 = np.percentile(data, 50)
Q3 = np.percentile(data, 75)

# Calculate Interquartile Range
IQR = Q3 - Q1

# Display results
print("Range:", data_range)
print("Variance:", round(variance, 2))
print("Standard Deviation:", round(std_dev, 2))
print("Q1 (First Quartile):", Q1)
print("Q2 (Second Quartile / Median):", Q2)
print("Q3 (Third Quartile):", Q3)
print("Interquartile Range:", IQR)