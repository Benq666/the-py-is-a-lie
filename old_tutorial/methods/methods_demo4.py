# scope of vars

t = 1


def test_method(t):
    print("Local t is {}" .format(t))
    t = 2
    print('New local t is {}' .format(t))


print('Global t is {}' .format(t))
test_method(t)
print('Global t is {}\n' .format(t))
t = 1


def test_method_global():
    global t
    print('Local t is {}' .format(t))
    t = 2
    print('New local t is {}' .format(t))


print('Global t is {}' .format(t))
test_method_global()
print('Global t is {}' .format(t))
