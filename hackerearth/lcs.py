import sys

sys.stdin = open('in', 'r')
strs = list(map(str, input().split()))

lens = [len(s) for s in strs]


def lcs(X, Y):
    m = len(X)
    n = len(Y)

    L = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

    return L[m][n]


print(lcs(strs[0], strs[1]))
