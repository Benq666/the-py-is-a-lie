# parent and child classes, overriding vars and methods, extending parent methods


class Human(object):

    parent_var = "This is a parent var inside parent class"

    def __init__(self):
        print("The {} instance was created" .format(self.__class__.__name__))

    def sleep(self):
        print("The {} fell asleep" .format(self.__class__.__name__))

    def wakeup(self):
        print("The {} woke up" .format(self.__class__.__name__))

    def parent_method(self):
        print("This is a parent method inside the parent class")

    def print_parent_var(self):
        print(self.parent_var)


class Man(Human):

    parent_var = "This is a parent var inside child class"

    def __init__(self):
        super().__init__()

    def parent_method(self):
        print("This is a parent method inside the child class")

    def sleep(self):
        super(Man, self).sleep()
        print("And the child is sleeping too")


human = Human()
human.sleep()
human.wakeup()
man = Man()
man.sleep()
man.wakeup()
print()

human.parent_method()
man.parent_method()
print()

human.print_parent_var()
man.print_parent_var()
print()

human.sleep()
man.sleep()
