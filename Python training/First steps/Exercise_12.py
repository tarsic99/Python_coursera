A = int(input())
B = int(input())
N = int(input())
rub = (A * N) + ((B * N) // 100)
kop = B * N % 100
print(rub, kop)
