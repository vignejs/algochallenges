if __name__ == '__main__':
    students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
    namel = [students[x][0] for x in range(len(students))]
    scorel = [students[x][1] for x in range(len(students))]
    # for _ in range(int(input())):
    #     name = input()
    #     namel.append(name)
    #
    #     score = float(input())
    #     scorel.append(score)
    #
    #     students.append([name, score])

    lowest = sorted(set(scorel))[1]
    sd = dict(students)
    loser = [x for x in sd.keys() if sd[x] == lowest]
    print('\n'.join(sorted(loser)))
