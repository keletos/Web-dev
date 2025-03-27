nums = [int(x) for x in input().split()]
cnt = 0

for i in range(nums.__len__()):
    if nums[i] > 0:
        cnt += 1

print(cnt)