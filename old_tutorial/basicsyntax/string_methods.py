# String methods in Python

# Accessing characters in a string

first = "nyc"
print(first[0], first[1], first[2])

mixed = "MiXeD"
print(mixed, mixed.lower(), mixed.upper(), len(mixed), sep="\n")

numb = 1
string_numb = str(numb)

print(mixed + str(numb), mixed, numb)

# Concat

string1, string2 = "left part", "right part"
print('***\n' + string1 + " " + string2 + " " + str(numb))
print("%s %s %s" % (string1, string2, str(numb)))

