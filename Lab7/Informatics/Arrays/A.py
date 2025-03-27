import math

nums = [int(x) for x in input().split()]

for i in range (math.ceil(nums.__len__() /2)):
    print(nums[i])
    i += 2