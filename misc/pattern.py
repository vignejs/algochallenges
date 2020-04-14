n = int(input())
rhr = n * (n + 1)
rhl = rhr - n + 1
lhl = 1
lhr = n + 1
for i in range(n):
    print(
        "*" * i * 2
        + "0".join([str(x) for x in range(lhl, lhr)])
        + '0'
        + "0".join([str(x) for x in range(rhl, rhr + 1)]))
    lhl = lhl + n - i
    lhr = lhr + n - i - 1
    rhl = rhl - (n - i - 1)
    rhr = rhr - (n - i)
