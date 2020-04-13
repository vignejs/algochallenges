import random

returnDate = list(map(int, input().split()))
dueDate = list(map(int, input().split()))
# returnDate = [random.randint(0, 31), random.randint(0, 12), random.randint(0, 3000)]
# dueDate = [random.randint(0, 31), random.randint(0, 12), random.randint(0, 3000)]
print(returnDate)
print(dueDate)
fine = 0

if (returnDate[0] - dueDate[0]) > 0:
    fine = 15 * (returnDate[0] - dueDate[0])
if (returnDate[0] - dueDate[0]) < 0:
    fine = 0
if (returnDate[1] - dueDate[1]) > 0:
    fine = 500 * (returnDate[1] - dueDate[1])
if (returnDate[1] - dueDate[1]) < 0:
    fine = 0
if (returnDate[2] - dueDate[2]) > 0:
    fine = 10000
if (returnDate[2] - dueDate[2]) < 0:
    fine = 0
print(fine)

# Input (stdin)Download
# 31 8 2004
# 20 1 2004
# Expected OutputDownload
# 3500
