
# Write a Python program to Read/Write to a File 

with open('hello.txt', 'w') as file:
    file.write("Hello, this is some content to write to the file.")

with open('hello.txt', 'r') as file:
    content = file.read()
    print("Content read from 'conv.txt':")
    print(content)
