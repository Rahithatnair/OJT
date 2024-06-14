import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

height=np.array([150,160,164,165,173]).reshape(-1,1)
weight=np.array([50,65,63,68,72])

#create a linear regression model for the above dataset
model = LinearRegression()

#lets fit the model with approproate data
model.fit(height,weight)
predicted_weight= model.predict(height)
print(f"intercepts: {model.intercept_}")
print(f"coefficients: {model.coef_[0]}")

#create a scatterplot
plt.scatter(height,weight,color="blue")
plt.plot(height,predicted_weight,color='red')
plt.xlabel('height')
plt.ylabel('weight')
plt.title('Linear Regression')
plt.show()
