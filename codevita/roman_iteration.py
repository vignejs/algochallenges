from collections import OrderedDict


def write_roman(num):
    roman = OrderedDict()
    roman[1000] = "M"
    roman[900] = "CM"
    roman[500] = "D"
    roman[400] = "CD"
    roman[100] = "C"
    roman[90] = "XC"
    roman[50] = "L"
    roman[40] = "XL"
    roman[10] = "X"
    roman[9] = "IX"
    roman[5] = "V"
    roman[4] = "IV"
    roman[1] = "I"

    def roman_num(num):
        for r in roman.keys():
            x, y = divmod(num, r)
            yield roman[r] * x
            num -= (r * x)
            if num <= 0:
                break

    return "".join([a for a in roman_num(num)])


num = int(input())
bases = {'I': 9, 'V': 22, 'X': 24, 'L': 12, 'C': 3, 'D': 4, 'M': 13}
l = []
while True:
    if 1 <= num <= 3999:
        r = write_roman(num)
        for i in list(set(r)):
            l.append(bases[i])
        base = max(l) + 10
        num = int(r, base)

    else:
        print(num)
        break
