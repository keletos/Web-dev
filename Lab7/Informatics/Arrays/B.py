nums = [int(x) for x in input().split()]

for i in range(nums.__len__()):
    if nums[i] % 2 == 0:
        print(nums[i])