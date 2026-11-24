import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

hours = np.array([1, 2, 3, 4, 5, 6, 7, 8]).reshape(-1, 1)
marks = np.array([35, 40, 50, 55, 65, 70, 80, 85])

model = LinearRegression()
model.fit(hours, marks)

predicted = model.predict([[6.5]])

print("Predicted Marks:", predicted[0])

plt.scatter(hours, marks, label="Actual Marks")
plt.plot(hours, model.predict(hours), label="Regression Line")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study Hours vs Marks")
plt.legend()
plt.show()