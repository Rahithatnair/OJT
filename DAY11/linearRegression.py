import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression       
X = np.array([[1], [2], [3], [4], [5]])     
y = np.array([2, 3.5, 2.8, 4.6, 5.0])         

 
model = LinearRegression()
model.fit(X, y)

y_pred = model.predict(X)

plt.scatter(X, y, color='blue')
plt.plot(X, y_pred, color='red')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Linear Regression')
plt.show()
  