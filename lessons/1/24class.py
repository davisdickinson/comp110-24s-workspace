x: int = 2
y: int = 9

if x % 2 == 0:
    print("A")
    if x == 2:
        print("B")
else:
    if x < y:
        print("C")
if x ** 2 == y:
    print("D")