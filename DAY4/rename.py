# Write a Python program that renames a file named ‘old_name.txt to’ ‘new_name.txt’.
import os
old_name = 'text.txt'
new_name = 'hello.txt'

os.rename(old_name, new_name)

print(f"File '{old_name}' renamed to '{new_name}' successfully.")
