def decimal_to_binary(n):
     return bin(n).replace("0b", "") 

number = int(input("Write a number: "))
binary = decimal_to_binary(number) 
print(f"The binary representation of {number} is {binary}")