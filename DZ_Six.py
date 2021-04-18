a: float = 2
b: float = 3
c: float = 0.1
day = 1
while a < b:
    a += a * c
    day += 1
    print(day, "-й День: ", a )