# modules

from methods.methods_ex import get_net_income as gni
import math
from math import sqrt


class ModulesDemo:

    def builtin_methods(self):
        print(math.sqrt(100))
        print(sqrt(100))


m = ModulesDemo()
m.builtin_methods()
print()

gni('Alabama', 1000)
