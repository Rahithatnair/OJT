
# Write a Python program that reads a file and prints its content. Handle ‘FileNotFoundError’ and ‘PermissionError’ exceptions.

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            print("File content:")
            print(file.read())
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except PermissionError:
        print(f"Error: Permission denied to read the file '{file_path}'.")

file_path = input("Enter the path of the file: ")
read_file(file_path)
