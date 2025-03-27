a = int(input())
b = int(input())
neg = input()

if neg:
    print(a < 0 and b < 0)
else:
    print((a < 0 and b > 0) or (a > 0 and b < 0))