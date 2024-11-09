a=int(input(""))
b=int(input(""))
c=int(input(""))

avgspeed = a+b+c / 3 
print(f"The average speed is {avgspeed}")

if a > b and c > b:
    print(f"{a} and {c} are greater than {b}")
          
if a > b and c <= b:
    print(f"{a} is greater than {b}, but {c} is not greater than {b}")

if a <= b and c > b:
    print(f"{c} is greater than {b}, but {a} is not greater than {b}")

if a <= b and c <= b:
    print(f"Neither {a} nor {c} is greater than {b}")