# Task Given a base- integer, , convert it to binary (base-). Then find and print the base- integer denoting the
# maximum number of consecutive 's in 's binary representation.
#
# Input Format
#
# A single integer, .
#
# Constraints
#
# Output Format
#
# Print a single base- integer denoting the maximum number of consecutive 's in the binary representation of .
dec = 5
r = dec
b = []
while r != 0:
    x = r % 2
    b.append(x)
    r = r // 2
b.reverse()
print(b)
count = 1
clst = []
for i in range(len(b) - 1):
    if b[i] == b[i + 1] == 1:
        count += 1
    if b[i] == 1 and b[i + 1] == 0:
        clst.append(count)
        count = 1
clst.append(count)
print(max(clst))
