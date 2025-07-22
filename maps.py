first_list = [1,2,3]
second_list = [4,5,6]
result = map(lambda x, y: x + y, first_list, second_list)
print("The addition of the two lists is: ")
print(list(result))

#using map
nums = [1,2,3,4,5]
def sq(n):
    return n*n
square = list(map(sq, nums))
print("The squares of the numbers inside of the list are: ")
print(square)