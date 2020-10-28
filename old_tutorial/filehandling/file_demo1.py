"""
File i/o

modes:
'w'         'r'        'r+'            'a'
write only  read only  read and write  append
"""

test_list = [1, 2, 3]

test_file = open('test_list_file.txt', 'w')

for item in test_list:
    test_file.write(str(item) + ' line\n')

test_file.close()
