import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

transactions = [
    ['Milk', 'Bread', 'Butter'],
    ['Bread', 'Butter'],
    ['Milk', 'Bread'],
    ['Milk', 'Butter'],
    ['Milk', 'Bread', 'Butter']
]

te = TransactionEncoder()
data = te.fit(transactions).transform(transactions)

df = pd.DataFrame(data, columns=te.columns_)

# Frequent Itemsets
frequent_items = apriori(
    df, min_support=0.4, use_colnames=True
)

print("Frequent Itemsets:")
print(frequent_items)

# Association Rules
rules = association_rules(
    frequent_items,
    metric="confidence",
    min_threshold=0.5
)

print("Association Rules:")
print(rules[['antecedents', 'consequents', 'support', 'confidence']])