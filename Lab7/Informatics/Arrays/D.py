nums = [int(x) for x in input().split()]

for i in range(1, nums.__len__()):
    if nums[i-1] < nums[i]:
        print(nums[i]) 