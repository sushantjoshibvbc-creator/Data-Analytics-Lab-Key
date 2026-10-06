import pandas as pd

# Create dataset of 100 students
data = {
    "Roll_No": range(1, 101),
    "Marks": range(50, 150)
}

df = pd.DataFrame(data)

# Select random sample of 20 students
sample = df.sample(n=20, random_state=42)

print("Random Sample of 20 Students:")
print(sample)