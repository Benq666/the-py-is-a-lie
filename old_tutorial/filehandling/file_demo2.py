"""
File i/o

reading the file
"""

test_file = open('test_list_file.txt', 'r')

print(str(test_file.read()))

test_file.close()

print('Line by line test:')
test_file = open('test_list_file.txt', 'r')
print(str(test_file.readline()))

for x in range(2):
    print(str(test_file.readline()))

test_file.close()
