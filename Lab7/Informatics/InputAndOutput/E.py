v = int(input())
t = int(input())

print((v * t) % 109 if (v * t) % 109 >= 0 else (v * t) % 109 + 109)