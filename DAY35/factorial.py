
#  Write a Python function factorial(num) which returns the factorial of a given number.

def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

print(factorial(5))  

