l = [3,6,2,8,3,8]
print("Original list =", l)

count = 0

for i in l:
    count += i

avg = count/len(l)

print("sum = ", count)
print("average =", avg)

l.sort()


smalll = l[0]
largel = l[-1]

print(smalll)
print(largel)