# positional parameters
import random


def sum_nums(a, b, c):
    """
    Prints the sum of three numbers from the args
    :param a: first num
    :param b: second num
    :param c: third num
    :return: None
    """
    return a + b + c


def sum_nums_positional(a, b, c=3):
    """
    Prints the sum of three numbers from the args
    :param a: first num
    :param b: second num
    :param c: third num
    :return: None
    """
    return a + b + c


x = random.randint(0, 95)
y = random.randint(0, 95)
print(sum_nums_positional(1, 2, 3))
print(sum_nums_positional(1, 2))
print()
print(sum_nums_positional(x, y, 0))
