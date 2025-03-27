import math

x = int(input())

i = 0
while True:
    if math.pow(2, i) > x:
        break
    else:
        print(math.pow(2, i))
    i += 1