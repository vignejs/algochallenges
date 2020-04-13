import math
import os
import random
import re
import sys


# Complete the powerSum function below.
def powerSum(X, N):
    s = 0
    count = 1
    m = int(X ** (1 / N))
    it = [i ** N for i in range(1, m + 1)]
    for x in it:
        if s == X:
            return count
        else:
            s += x ** N


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    X = int(input())

    N = int(input())

    result = powerSum(X, N)

    fptr.write(str(result) + '\n')

    fptr.close()
