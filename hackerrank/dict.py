n = int(input())
l = []
for _ in range(0, n):
    l.append(tuple(map(str, input().rstrip().split())))

d = {n: p for (n, p) in l}
# print(d)
while True:
    s = input()
    if s == "\n":
        break
    if s in d:
        print("{}={}".format(s, d[s]))
    else:
        print("Not found")
