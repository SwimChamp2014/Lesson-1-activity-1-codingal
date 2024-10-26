# Get user input
input_str = input("Enter a character: ")

# Check if the input is an alphabet letter
if input_str.isalpha():
    print(f"'{input_str}' is an alphabet letter.")
else:
    print(f"'{input_str}' is not an alphabet letter.")
