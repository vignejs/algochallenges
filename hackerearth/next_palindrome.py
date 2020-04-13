n = int(input())
while True:
    s_str = list(str(n))
    if s_str == s_str[::-1]:
        print(int("".join(s_str)))
        break
    n += 1
