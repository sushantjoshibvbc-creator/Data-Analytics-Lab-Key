import pandas as pd

data = {
    "Name": ["A","B","C","D","E","F","G","H","I","J"],
    "Branch": ["CSE","CSE","IT","IT","ECE",
               "ECE","CSE","IT","ECE","CSE"],
    "Marks": [80,75,90,65,85,70,88,72,78,82]
}

df = pd.DataFrame(data)

# Select 2 students from each branch
sample = df.groupby("Branch", group_keys=False).apply(
    lambda x: x.sample(n=2, random_state=42)
)

print("Stratified Sample:")
print(sample)