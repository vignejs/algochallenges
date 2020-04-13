import sys

sys.stdin = open('in', 'r')

n = int(input())
nums = list(map(int, input().split()))
l = []
j = 0
for i in range(len(nums)):
    if j == 0:
        l.append(nums[i])
        j += 1
    elif l[j - 1] < nums[i]:
        l.append(nums[i])
        j += 1
    else:
        continue

print(" ".join(map(str, l)))
