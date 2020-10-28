# methods continuation


def sum_nums(a, b, c):
    """
    Prints the sum of three numbers from the args
    :param a: first num
    :param b: second num
    :param c: third num
    :return: None
    """
    print(a + b + c)


def sum_nums_return(a, b, c):
    """
    Returns a sum of three numbers from the args
    :param a: first num
    :param b: second num
    :param c: third num
    :return: the sum of a, b and c
    """
    return a + b + c

# returns nothing
x = sum_nums(1, 2, 3)

y = sum_nums_return(1, 2, 3)

print(x)
print(y)
print()


def is_metro(city):
    """
    Checks if the city is a metro or not
    :param city: city to be checked
    :return: True if the city is metro, False otherwise
    """
    metros = ['mow', 'spb', 'zhl']

    if city in metros:
        return True
    else:
        return False


result = is_metro('mow')
print('Is mow a metro?\t' + str(result))
