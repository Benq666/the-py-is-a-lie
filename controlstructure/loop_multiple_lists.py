"""
iterate multiple lists at the same time
"""

alist = [1, 2, 3]
another_list = [4, 5, 6]

for a, b in zip(alist, another_list):
    print(a)
    print(b)
    if a < b:
        print(a)
    else:
        print(b)
