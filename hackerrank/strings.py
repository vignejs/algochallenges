# Objective Today we're expanding our knowledge of Strings and combining it with what we've already learned about
# loops. Check out the Tutorial tab for learning materials and an instructional video!
#
# Task Given a string, , of length  that is indexed from  to , print its even-indexed and odd-indexed characters as
# space-separated strings on a single line (see the Sample below for more detail).
#
# Note:  is considered to be an even index.
#
# Input Format
#
# The first line contains an integer,  (the number of test cases).
# Each line  of the  subsequent lines contain a String, .
#
# Constraints
#
# Output Format
#
# For each String  (where ), print 's even-indexed characters, followed by a space, followed by 's odd-indexed
# characters.
#
# Sample Input
#
# 2
# Hacker
# Rank
# Sample Output
#
# Hce akr
# Rn ak

# t = int(input())
t = 2
for _ in range(0, t):
    # s = input()
    s = "hacker"
    se, so = "", ""
    for i in range(0, len(s)):
        if i % 2 == 0:
            se = se + s[i]
        else:
            so = so + s[i]

        # se = [se, se + s[i]][i % 2 == 0]
        # so = [so, so + s[i]][i % 2 != 0]

    print(se + " " + so)
