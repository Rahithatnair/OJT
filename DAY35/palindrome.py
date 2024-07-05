#  Write a Python Function is_palindrome(num) that accepts an integer num as argument and returns True if the num is palindrome else returns false. Invoke the function and based on return value print the output.

def is_palindrome(num):
    num_str = str(num)
    return num_str == num_str[::-1]

num = 12321
if is_palindrome(num):
    print("Given number is a palindrome")
else:
    print("Given number is not a palindrome")

num = 12345
if is_palindrome(num):
    print("Given number is a palindrome")
else:
    print("Given number is not a palindrome")
