num = int(input("Give the base: "))
exponent = int(input("Give the exponent: "))
result = 1

for i in range(exponent):
    result = result * num

print("The result is", result)
