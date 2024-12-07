lower = int(input("enter a lower range: "))
upper = int(input("enter a upper range: "))

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower + 1, upper):
    if num > 1:
        for i in range (2, num):
            if (num % i) == 0:
                break

        else: 
            print(num)