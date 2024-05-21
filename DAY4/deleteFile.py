# Write a python program to Delete a file

import os

file_path = "text.txt"

if os.path.exists(file_path):
    os.remove(file_path)
    print(f"File '{file_path}' has been deleted successfully.")
else:
    print(f"File '{file_path}' not found.")


