import sys
import math

sys.stdin = open('in', 'r')
nums = list(map(int, input().split()))

a = nums[0]
b = nums[1]

n = math.gcd(a, b)

result = 0

for i in range(1, int(math.sqrt(n)) + 1):

    # if 'i' is factor of n
    if n % i == 0:
        # check if divisors are equal
        if n / i == i:
            result += 1
        else:
            result += 2
# for i in range(1, min(a, b) + 1):
#     if a % i == b % i == 0:
#         n += 1

print(result)
