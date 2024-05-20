
# Write a Python program to calculate the factorial of a number using a lambda function and reduce function.

from functools import reduce

factorial = lambda n: reduce(lambda x, y: x * y, range(1, n + 1))

number = int(input("Enter a number: "))
print("The factorial of", number, "is:", factorial(number))
