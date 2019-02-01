"""
exceptions = errors
"""


def exception_handling():
    try:
        a = 10
        b = "20"
        c = 0

        d = (a + b) / c
        print(d)

    except TypeError:
        print("Can't concat int and string")

    except ZeroDivisionError:
        print("Zero Division")


exception_handling()
