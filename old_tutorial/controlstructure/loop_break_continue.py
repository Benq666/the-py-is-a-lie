# break and continue
# else after while will execute only if the loop was finished, i.e. without break

temp_list, x = [], 0
while x <= 12:
    if x % 2 is 0:
        x += 1
        continue
    elif x % 11 is 0:
        break
    else:
        temp_list.append(x)
        x += 1
else:
    print(temp_list)
print(temp_list)
