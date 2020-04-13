import numpy
import sys

sys.stdin = open('in', 'r')

dim = list(map(int, input().split()))

result = numpy.eye(dim[0], dim[1])
print(result)