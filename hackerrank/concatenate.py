import numpy
import sys

sys.stdin = open('in', 'r')

dim = list(map(int, input().split()))
array_1 = [list(map(int, input().split())) for _ in range(dim[0])]
array_2 = [list(map(int, input().split())) for _ in range(dim[1])]
result = numpy.concatenate((numpy.array(array_1), numpy.array(array_2)), axis=0)
print(result)
