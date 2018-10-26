a, b, c = int(input()), int(input()), int(input())
x, y, z = int(input()), int(input()), int(input())

a1 = (a // x) * (b // y) * (c // z)
a2 = (a // x) * (b // z) * (c // y)
a3 = (a // y) * (b // x) * (c // z)
a4 = (a // y) * (b // z) * (c // x)
a5 = (a // z) * (b // x) * (c // y)
a6 = (a // z) * (b // y) * (c // x)

d1, d2, d3, d4, d5, d6 = sorted([a1, a2, a3, a4, a5, a6])
print(d6)
