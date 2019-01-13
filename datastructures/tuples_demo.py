# explore tuples
# ~list but it's immutable (can't change the elements)

temp_list = [1, 2, 3]
print(temp_list)

atuple = (1, 2, 3)
print(atuple)

print('Tuple printing test. Tuple:', atuple, 'Element at the index [0]:', atuple[0])

print(atuple[:1:])

print('Tuple .index test. Tuple:', atuple, 'Index of element "3":', atuple.index(3))

print('Tuple .count test. Tuple:', atuple, 'Count elements "1":', atuple.count(1))
