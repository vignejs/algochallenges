n = int(input())


def decToBinary(n):
    binaryNum = []

    while n > 0:
        binaryNum.append(n % 2)
        n = n // 2

    return "".join(map(str, binaryNum[::-1]))


s = len(decToBinary(n)) // 2
i = decToBinary(n)[-s:] + decToBinary(n)[s:-s] + decToBinary(n)[:s]
print(int(i, 2))
