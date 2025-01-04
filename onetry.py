rowSize = int(input("enter the number of rows: ")) #4
if rowSize%2 == 0:
    halfDiamRow = int(rowSize/2) #2
else:
    halfDiamRow = int(rowSize/2) + 1
space = halfDiamRow - 1 #1

#loop for upper part
for i in range(1, halfDiamRow + 1):#loop for rows #1,3
    for j in range(1, space + 1):#loop for columns # 1, 2
        print(end=" ")
    space = space - 1 #0 #-1
    num = 1
    for j in range(2*i-1): #1 #3
        #print("i inside loop is", i)
        print(end = str(num))
        num = num + 1
    print() #added new line
space = 1



#loop for lower part
for i in range(1, halfDiamRow): #1, 2
    for j in range(1, space + 1): #1,2
        print(end=" ")
    space = space + 1
    num = 1
    for j in range(1, 2*(halfDiamRow - i)): #1,2 
        print(end=str(num))
        num = num + 1
    print()
