import sys

sys.stdin = open('in', 'r')

if __name__ == '__main__':
    N = int(input())
    l = []
    for _ in range(N):
        command = input().split()
        if command[0] == "insert":
            i, e = int(command[1]), int(command[2])
            l.insert(i, e)
        if command[0] == "print":
            print(l)
        if command[0] == "remove":
            e = int(command[1])
            l.remove(e)
        if command[0] == "append":
            e = int(command[1])
            l.append(e)
        if command[0] == "sort":
            l.sort()
        if command[0] == "pop":
            l.pop()
        if command[0] == "reverse":
            l.reverse()
        else:
            continue
