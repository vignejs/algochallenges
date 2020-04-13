import numpy
import sys

sys.stdin = open('in', 'r')


def arrays(arr):
    # complete this function
    arr = list(map(int, arr))
    arr.reverse()
    return numpy.array(arr, float)


arr = input().strip().split(' ')

result = arrays(arr)
print(result)
