for i in range(1,10):
    if i%2 == 0 and i%3 == 0:
        print("The number", i, "is divisible by 2 and 3")
    elif i%3 == 0:
        pass
    elif i%2 == 0:
        print(i)
    
    else:
        print("The number", i, "is not divisible by 2 or 3")
    