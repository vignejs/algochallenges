import math


def gcd(a, b):
    return gcd(b, a % b) if a % b is not 0 else b


def is_primitive_right(a, b, c):
    return gcd(a, b) == gcd(b, c) == 1


def isperfect_square(x):
    return math.sqrt(x) - math.sqrt(x) // 1 == 0


