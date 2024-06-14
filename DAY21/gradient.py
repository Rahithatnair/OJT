
x=10
learning_rate= 0.1
num_iteration = 100

#create a loop for gradient descent

for i in range(num_iteration):
    gradient = 2 * x                 #compute our gradient
    x=x-learning_rate*gradient                                # update the x with new parameter that is new x
    print(f"iteration {i+1}:x={x},f(x)={x**2}")
print(f"minimum value of the x: {x}")
