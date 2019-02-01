"""
exceptions part 2
"""


def exception_handling2():
    try:
        a = 1
        b = 2
        c = 0

        d = (a + b) / c
        print(d)
    except:
        print("This is a test exception")
        raise Exception("fix this stuff")
    else:
        print("All is fine")
    finally:
        print("This block is always executed")


exception_handling2()
