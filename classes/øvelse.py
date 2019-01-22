"""
Some practise with classes and inheritance

1. create a class Fruit
1.a) define three methods
1.b) init, nutrition, fruit_shape (print whatever)
2. create a child class, fruit instance
2.a) define three methods (print whatever)
2.b) init, nutrition, color
3. call all the methods
"""


class Fruit(object):

    nutrition_value = 1000

    def __init__(self):
        print("The {} instance was created" .format(
              self.__class__.__name__))

    def nutrition(self):
        print("The nutrition of the {} is {} Kcal" .format(
              self.__class__.__name__, self.nutrition_value))

    def fruit_shape(self):
        print("The shape of the {} is round" .format(
              self.__class__.__name__))


class Apple(Fruit):

    def __init__(self):
        super(Apple, self).__init__()
        self.nutrition_value = 500

    def nutrition(self):
        super(Apple, self).nutrition()

    def color(self):
        print("The color of {} is red" .format(
              self.__class__.__name__))


fruit = Fruit()
fruit.nutrition()
fruit.fruit_shape()
print()

apple = Apple()
apple.nutrition()
apple.fruit_shape()
apple.color()
