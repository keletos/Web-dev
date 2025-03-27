import math

x = int(input())

if math.pow(2, math.log(x, 2)) == x:
    print("YES")
else:
    print("NO")