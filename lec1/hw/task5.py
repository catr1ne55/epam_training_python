a = int(input())
b = int(input())
if a < b:
    a, b = b, a
while True:
    rn = a % b
    if rn % b == 0:
        print(b)
        break
    a = b
    b = rn
