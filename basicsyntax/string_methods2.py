# more string methods

# replace
a = "1abc2abc3abc"
print(a.replace("abc", "cba"))

# substring [)
sub = a[a.index("1"):a.index("3") + 1:2]

print(sub)
