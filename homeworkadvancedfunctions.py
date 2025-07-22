n = int(input("Enter a number: "))
odd_numbers = [x for x in range(n) if x % 2 != 0]
even_numbers = [x for x in range(n) if x % 2 == 0]
print("Odd numbers:", odd_numbers)
print("Even numbers:", even_numbers)


fruits = ['apple', 'banana', 'cherry', 'date']
capitalized_fruits = [fruit.capitalize() for fruit in fruits]
print("Updated fruits list:", capitalized_fruits)