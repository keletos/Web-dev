nums = [int(x) for x in input().split()]

for i in range(1, nums.__len__()):
    if (nums[i-1] > 0 and nums[i] > 0) or nums[i-1] < 0 and nums[i] < 0:
        print(nums[i-1], " ", nums[i])
        break