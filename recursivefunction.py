def factorial(x):
    print(x)
    if x == 0 or x == 1:
        return 1
    else:
        return x * factorial(x - 1) #This updates factorial(x) on line 1
    print(x)


print(factorial(5))