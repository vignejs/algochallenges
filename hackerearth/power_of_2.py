import math
n = int(input())

div = [2 ** i for i in range(0, 21)]
div.reverse()
print(div)
for i in div:
    if n % i == 0:
        print(int(math.log2(i)))
        break
