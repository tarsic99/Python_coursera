k = int(input())
n = int(input())
m = int(input())

if n <= k:
    print(2 * m)
elif (n * 2 % k) == 0:
    print(m * (n * 2 // k))
else:
    print(m * (1 + (n * 2 // k)))
