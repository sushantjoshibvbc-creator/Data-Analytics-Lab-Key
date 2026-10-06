import pandas as pd

# Create dataset of 100 customers
data = {
    "Customer_ID": range(1, 101),
    "Purchase": range(100, 200)
}

df = pd.DataFrame(data)

# Required sample size
sample_size = 10

# Calculate sampling interval
interval = len(df) // sample_size

# Select every kth record
sample = df.iloc[::interval].head(sample_size)

print("Systematic Sample:")
print(sample)