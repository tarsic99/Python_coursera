N = int(input())
hours = (N // 60) % 24
minutes = (N - hours * 60) % 60
print(hours, minutes)
