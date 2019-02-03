"""
With As keywords
"""

print('Simple write')
test_write = open('test_list_file.txt', 'w')
test_write.write('Test line')
test_write.close()

print('\nSimple read')
test_read = open('test_list_file.txt', 'r')
print(str(test_read.read()))

print('\nWith As write')
with open('test_list_file_as.txt', 'w') as test_with_as_write:
    test_with_as_write.write('Test line with as')

print('\nWith As read')
with open('test_list_file_as.txt', 'r') as test_with_as_read:
    print(test_with_as_read.read())
