import numpy
import sys

sys.stdin = open('in', 'r')

dim = tuple(map(int, input().split()))

zero = numpy.zeros(dim, dtype=numpy.int)
print(zero)

one = numpy.ones(dim, dtype=numpy.int)
print(one)