# testing conditions
import random

random_bool = bool(random.getrandbits(1))

if random_bool is True:
    print(True)
else:
    print(False)

for x in range(0, 10):
    string = random.choice(['grey', 'black', 'blue'])
    if string is 'grey':
        print(str(x) + '. grey')
    elif string is 'black':
        print(str(x) + '. black')
    else:
        print(str(x) + '. blue')
