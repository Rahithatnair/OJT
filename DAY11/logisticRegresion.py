import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

# Data
X = np.array([[0.5], [1.0], [1.5], [2.0], [2.5], [3.0], [3.5], [4.0], [4.5], [5.0]])
y = np.array([0, 0, 0, 0, 0, 1, 1, 1, 1, 1])

# Train model
model = LogisticRegression().fit(X, y)

# Predict probabilities
y_pred =model.predict(X)
y_prob = model.predict_proba(X)[:, 1]

# Plot
plt.scatter(X, y, color='blue')
plt.plot(X, y_prob, color='red')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Logistic  Regression')
plt.show()