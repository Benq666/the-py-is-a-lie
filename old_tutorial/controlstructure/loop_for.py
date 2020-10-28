# for loop

astring = 'A b C d E f G'

for char in astring:
    if char is 'b':
        print('B', end='')
    else:
        print(char, end='')

print()

alist = ['first', 'second', 'third']

for key in alist:
    print(key, end=', ')

print()

adict = {'first': 'one', 'second': 'two', 'third': 'three'}
for key in adict:
    print(key + ' ' + adict[key])

print()

for key, value in adict.items():
    print(key + ' ' + value)
