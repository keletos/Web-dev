n = int(input())

if n % 2 != 0:
    print("Weird")
elif n > 20:
    print("Not Weird")
elif n in range(2, 5):
    print("Not weird") 
elif n in range(6, 20):
    print("Weird")
