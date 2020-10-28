# How to printf in python

city = 'NYC'
event = 'rock concert'

# bruteforcing

print('Welcome to ' + city + ' and enjoy the ' + event)

# using formatting

print("Welcome to %s and enjoy the %s %4d %3f" % (city, event, 33, 0.1111))

print("Welcome to the {1} and enjoy the {0}".format(city, event))

print("Welcome to the {:!<10} and enjoy the {:_>20}".format(city, event))
