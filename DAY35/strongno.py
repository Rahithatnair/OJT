
# Write a Python function check_strong_number(num) that accepts a positive integer as argument and returns True if the number is strong number else false. Invoke the function and based on return value print the number is strong number or not.A number is said to be strong number, if the sum of factorial of each digit of the number is equal to the given number.

def check_strong_number(num):
    def factorial(n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * factorial(n - 1)
    
    digit_factorial_sum = sum(factorial(int(digit)) for digit in str(num))
    return digit_factorial_sum == num

num = 145
if check_strong_number(num):
    print("The number is a strong number")
else:
    print("The number is not a strong number")
