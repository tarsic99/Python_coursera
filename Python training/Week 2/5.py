a1 = int(input())
a2 = int(input())
b1 = int(input())
b2 = int(input())
if abs(a1 - b1) <= 1 and abs(a2 - b2) <= 1:
    print('yes')
elif abs(b1 - a1) <= 1 and abs(b2 - a2) <= 1:
    print('yes')
else:
    print('no')
