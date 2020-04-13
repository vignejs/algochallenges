import sys

sys.stdin = open('in', 'r')


def minion_game(string):
    vowels = "AEIOU"
    stuart = 0
    kevin = 0
    l = len(string)

    for i in range(l):
        if string[i] not in vowels:
            stuart += l - i
            # comb = [string[i:i + j + 1] for j in range(l - i)]
            # print(comb)

        if string[i] in vowels:
            kevin += l - i
            # comb = [string[i:i + j + 1] for j in range(l - i)]
            # print(comb)

    if kevin < stuart:
        print("Stuart", stuart)
    elif kevin > stuart:
        print("Kevin", kevin)
    else:
        print("Draw")

    # your code goes here


if __name__ == '__main__':
    s = input()
    minion_game(s)
