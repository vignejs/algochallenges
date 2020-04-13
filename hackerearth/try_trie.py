import sys

sys.stdin = open('in', 'r')
_ = int(input())
nums = list(map(int, input().split()))


def decToBinary(n):
    binaryNum = []

    while n > 0:
        binaryNum.append(n % 2)
        n = n // 2

    return "".join(map(str, binaryNum[::-1]))


bins = [list(decToBinary(i)) for i in nums]
# for i in range(4):
#     s = 0
#     for j in
# twos = [2**i for i in range()]
print(bins)

total = 0
power = 0

for i in bins:
    count = 0
    two = 2 ** power
    for j in i:
        if j == "1":
            count += 1
        if count == two:
            break

    total += count
    power += 1

while True:
    power = 0
    two = 2 ** power

    for i in range(len(bins)):

        if bins[i][power] == "1":
            count += 1

