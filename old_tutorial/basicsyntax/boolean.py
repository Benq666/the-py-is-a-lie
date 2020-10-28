# Boolean examples

a = True
b = False

# print(a, b)

print('****\n0 is', bool(0))
print('****\n1 is', bool(1))

c = ""
print("empty string is", bool(c))

c = "True"
print('string "' + c + '" is', bool(c))

print("string \"%s\" is %s" % (c, bool(c)))
