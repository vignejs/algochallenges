import codewars_test as Test


def socialist_distribution(population, minimum):
    l = len(population)
    if sum(population) / l < minimum:
        return []
    popindex = sorted(range(len(population)), key=lambda k: population[k])
    population.sort()
    t = 0
    for i, p in enumerate(population):
        if p < minimum:
            t += abs(p - minimum)
            population[i] = minimum
        if p >= minimum:
            break
    for i, p in enumerate(population[::-1]):
        ri = l - i - 1

    return [population[i] for i in popindex]


Test.describe("Basic tests")
Test.assert_equals(socialist_distribution(
    [2, 3, 5, 15, 75], 5), [5, 5, 5, 15, 70])
Test.assert_equals(socialist_distribution(
    [2, 3, 5, 15, 75], 20), [20, 20, 20, 20, 20])
Test.assert_equals(socialist_distribution(
    [2, 3, 5, 45, 45], 5), [5, 5, 5, 42, 43])
Test.assert_equals(socialist_distribution([2, 3, 5, 45, 45], 30), [])
Test.assert_equals(socialist_distribution(
    [24, 48, 22, 19, 37], 30), [30, 30, 30, 30, 30])
