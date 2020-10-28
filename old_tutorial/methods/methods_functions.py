# max(), min(), abs(), type()


def largest_number(*args):
    print(max(args))
    return max(args)


x = largest_number(1, 2, 3, 100, -10, -20, 0)


def smallest_number(*args):
    print(min(args))
    return min(args)


y = smallest_number(1, 2, 3, 100, -10, -20, 0)


def absolute_number(xx):
    print(abs(xx))
    return abs(xx)


z1 = absolute_number(-10)
z2 = absolute_number(10)


print(type(99))
print(type(type))
print(type(abs))

print('{}\n{}\n{}\n' .format(type(99), type(type), type(abs)))
