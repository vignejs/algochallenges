# Fredo is assigned a new task today. He is given an array A containing N integers. His task is to update all
# elements of array to some minimum value x , that is,  ;  such that sum of this new array is strictly greater than
# the sum of the initial array. Note that x should be as minimum as possible such that sum of the new array is
# greater than the sum of the initial array.
#
# Input Format:
# First line of input consists of an integer N denoting the number of elements in the array A.
# Second line consists of N space separated integers denoting the array elements.
#
# Output Format:
# The only line of output consists of the value of x.
#
# Input Constraints:

import sys

sys.stdin = open('in', 'r')

N = int(input())
nums = list(map(int, input().split()))
s = sum(nums)
l = len(nums)
i = 1
while True:
    if i*l > s:
        ans = i
        break
    else:
        i += 1

print(ans)