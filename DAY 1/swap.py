
# Write a Python program to swap two numbers without using a temporary variable.

num1 = int(input("enter a number "))
num2 = int(input ("enter another number "))
print("original number",num1,num2)
num1=num1+num2
num2=num1-num2
num1=num1-num2
print("swapped number",num1,num2)