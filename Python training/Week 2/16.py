a = int(input())
b = int(input())
c = int(input())

if a == b == c:
    print(3)
elif (a == b and a != c) or (a == c and a != b) or (b == c and a != c):
    print(2)
else:
    print(0)
