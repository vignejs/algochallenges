import sys

sys.stdin = open('in', 'r')
T = int(input())
for _ in range(T):
    n = int(input())
    sideLength = list(map(int, input().split()))
    stack = []
    # end = [sideLength[0], sideLength[-1]]
    # bottom = max(end)
    # sideLength.remove(bottom)
    # stack.append(bottom)
    for _ in sideLength:

        if sideLength[0] <= sideLength[-1]:
            bottom = sideLength[-1]
            sideLength.pop(-1)
        else:
            bottom = sideLength[0]
            sideLength.pop(0)

        if True if not stack else bottom <= stack[-1]:
            stack.append(bottom)
        else:
            print("No")
            break
    else:
        print("Yes")
