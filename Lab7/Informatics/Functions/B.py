def power(a, n):
    ans = 1
    for i in range(n):
        ans *= a
    return ans

a = int(input())
n = int(input())

print(power(a, n))