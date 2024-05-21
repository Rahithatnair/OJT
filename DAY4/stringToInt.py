
# Write a Python program with a function that converts a string to an integer. Handle exceptions within the function and print appropriate error messages.

def string_to_integer(string):
    try:
        return int(string)
    except ValueError:
        return None
inputs = ["123", "456", "abc", "789", "10"]
for input_str in inputs:
    result = string_to_integer(input_str)
    print(f"Conversion result for '{input_str}': {result}")