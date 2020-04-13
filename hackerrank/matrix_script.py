import math
import os
import random
import re
import sys

sys.stdin = open('in', 'r')

nm = input().split()

n = int(nm[0])

m = int(nm[1])

matrix = []
s = ''
for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
for i in range(m):
    for j in range(n):
        s += matrix[j][i]
print(s)
