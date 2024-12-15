var = 10 

for i in range(10):
    print (i)
    for j in range(2, 10, 1):
        print (j)
        if var % 2 == 0:
            var += 1
            print ("var", var)
    var += 1
    print ("var1", var)

else:
    print ("inside else")
    var += 1
print(var)
