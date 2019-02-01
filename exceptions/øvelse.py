"""
create a dict
create 3 keys

try to access the key that is not in the dict
handle the exception
"""
import traceback

watermelon = {"Color": "1", "Shape": "2", "Nutrition": "3"}

try:
    print(watermelon["Origin"])
except RuntimeError as ex:
    traceback.print_tb(ex.__traceback__)

finally:
    print("We tried to access the key that is not in the dict, "
          "then we handled the exception, and finally printed "
          "out this message!")
