
# Write a Python function check_amicable_numbers(num1, num2) that accepts two numbers num1 and num2 as arguments and returns True if the given pair of numbers are amicable numbers else return false. Invoke the function and based on return value print the numbers are amicable numbers or not.


def sum_of_proper_divisors(n):
    divisors = [i for i in range(1, n) if n % i == 0]
    return sum(divisors)

def check_amicable_numbers(num1, num2):
    return sum_of_proper_divisors(num1) == num2 and sum_of_proper_divisors(num2) == num1

num1, num2 = 220, 284
if check_amicable_numbers(num1, num2):
    print("The numbers are amicable numbers")
else:
    print("The numbers are not amicable numbers")
