# Test dictionary
test_dict = {'Codingal': 3, 'is': 2, 'best': 2, 'for': 2, 'Coding': 1}

# Print the dictionary
print("Test Dictionary:", test_dict)

# Ask user to enter the value to check
val = int(input("Enter the value you want to check the frequency of: "))

# Count and display the frequency of the entered value
frequency = list(test_dict.values()).count(val)
print(f"The frequency of value {val} is: {frequency}")
