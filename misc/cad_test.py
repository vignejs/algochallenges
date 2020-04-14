from itertools import combinations

min_l = 1
max_l = 1500
min_w = 1
max_w = 1500
count = 0


def get_count(dim, count):
    dim = [max(dim), min(dim)]
    if dim[0] == dim[1] == 1:
        return count + 1
    elif dim[0] == dim[1]:
        return count + 1
    elif dim[0] == 0 or dim[1] == 0:
        return count
    count += dim[0] // dim[1]

    dim = [dim[1], dim[0] % dim[1]]
    return get_count(dim, count)


def count_loop(dim, count):
    while True:
        if dim[0] >= dim[1]:
            dim = [dim[0], dim[1]]
        else:
            dim = [dim[1], dim[0]]

        if dim[0] == dim[1]:
            count = count + 1
            break
        elif dim[0] == 0 or dim[1] == 0:
            break
        count += dim[0] // dim[1]

        dim = [dim[1], dim[0] % dim[1]]
    return count


pos_l = [min_l + l for l in range(max_l - min_l + 1)]
pos_w = [min_w + w for w in range(max_w - min_w + 1)]
pos = set([*pos_w, *pos_l])

for c in combinations(pos, 2):
    count = count_loop(list(c), count)

print(count)
