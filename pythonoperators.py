x = 10

if (type(x) is int):
    print("True")

else:
    print("False")

y = 4.00

if (type(y) is float ):
    print("true")

else:
    print("false")

n = "hello, world"

if (type(n) is str):
    print("True")

else:
    print("False")

a=20
b=20

if(a is b):
    print("a + b have the same identity")

b=30
if( a is not b):
    print("a and b have different identities")