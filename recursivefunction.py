def factorial(x):
    print(x)
    if x == 0 or x == 1:
        return 1
    else:
        return x * factorial(x - 1) #using factorial repeats the cycle
    print(x)


print(factorial(5))