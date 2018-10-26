n = int(input())
a = [1, 21, 31, 41, 51, 61, 71, 81, 91]
b = [2, 3, 4, 22, 23, 24, 32, 33, 34, 42, 43, 44, 52, 53, 54, 62, 63, 64,
     72, 73, 74, 82, 83, 84, 92, 93, 94]
if n in a:
    print(str(n) + " korova")
elif n in b:
    print(str(n) + " korovy")
else:
    print(str(n) + " korov")
