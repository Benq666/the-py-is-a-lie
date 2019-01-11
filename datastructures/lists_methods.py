# testing the list built-in methods
# as well as different naming conventions

list1 = [1, 2, 3]

listLength = len(list1)
print(listLength)

list1.append(4)
print(list1)

list1.insert(0, "one")
print(list1)

item_index = list1.index(1)
print(item_index)

removed_item = list1.pop(list1.index("one"))
print(removed_item)
print(list1)
list1.insert(0, 1)

list_part = list1[0:3]
print(list1, list_part)

listPartTwo = list_part + list1[0::2]
print(listPartTwo)

list1.sort(reverse=True)
print(list1)
