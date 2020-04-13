class Difference:
    def __init__(self, a):
        self.maximumDifference = None
        self.__elements = a

        # Add your code here

    def computeDifference(self):
        element = self.__elements

        element.sort()
        self.maximumDifference = element[-1] - element[0]


# End of Difference class


_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
