def dupes(s):
    l = list(s)
    d = []
    for i in range(len(l)):
        if l[i] not in d:
            d.append(l[i])
    return "".join(d)


def merge_the_tools(string, k):
    n = len(string)
    nk = n // k
    t = [string[k * i:k * (i + 1)] for i in range(nk)]
    for u in t:
        print(dupes(u))

    # your code goes here


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
