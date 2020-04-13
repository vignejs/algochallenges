# Objective Today, we're building on our knowledge of Arrays by adding another dimension. Check out the Tutorial tab
# for learning materials and an instructional video!
#
# Context
# Given a  2D Array, :
#
# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# We define an hourglass in  to be a subset
# of values with indices falling in this pattern in 's graphical representation:
#
# a b c
#   d
# e f g
# There are  hourglasses in , and an hourglass sum is the sum of an hourglass' values.
#
# Task
# Calculate the hourglass sum for every hourglass in , then print the maximum hourglass sum.
#
# Input Format
#
# There are  lines of input, where each line contains  space-separated integers describing 2D Array ; every value in
#  will be in the inclusive range of  to .
#
# Constraints
#
# Output Format
#
# Print the largest (maximum) hourglass sum found in .
#
# Sample Input
#
# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 2 4 4 0
# 0 0 0 2 0 0
# 0 0 1 2 4 0
# Sample Output
#
# 19
# Explanation
#
#  contains the following hourglasses:
#
# 1 1 1   1 1 0   1 0 0   0 0 0
#   1       0       0       0
# 1 1 1   1 1 0   1 0 0   0 0 0
#
# 0 1 0   1 0 0   0 0 0   0 0 0
#   1       1       0       0
# 0 0 2   0 2 4   2 4 4   4 4 0
#
# 1 1 1   1 1 0   1 0 0   0 0 0
#   0       2       4       4
# 0 0 0   0 0 2   0 2 0   2 0 0
#
# 0 0 2   0 2 4   2 4 4   4 4 0
#   0       0       2       0
# 0 0 1   0 1 2   1 2 4   2 4 0
# The hourglass with the maximum sum () is:
#
# 2 4 4
#   2
# 1 2 4

import random

x = [random.randint(-9, 9) for _ in range(9000)]
zero = [0 for _ in range(10000)]
# noinspection PyCompatibility
xzero = [*x, *zero]
if __name__ == '__main__':
    arr = [[random.choice(xzero) for _ in range(6)] for _ in range(6)]
    print(arr)
    # for _ in range(6):
    #     arr.append(list(map(int, input().rstrip().split())))
    arr3 = []
    for i in range(0, 4):
        for j in range(0, 4):
            arr3.append([arr[n][j:j+3] for n in range(i, i + 3)])
    print(arr3)
    x = []
    for t in range(0, 16):
        x.append(sum(arr3[t][0] + arr3[t][2] + [arr3[t][1][1]]))
    print(max(x))
