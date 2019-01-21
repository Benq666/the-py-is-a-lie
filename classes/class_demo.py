# OOP


class Human(object):
    arms = legs = []
    gender = ''
    age = 0

    def __init__(self, gender, age):
        self.arms = ['left arm', 'right arm']
        self.legs = ['left leg', 'right leg']
        self.gender = gender
        self.age = age

    def info(self):
        print('Gender: {}\nAge: {}' .format(self.gender, self.age))
        return {'Gender': self.gender, 'Age': self.age}

    def add_leg(self):
        self.legs.append('{} leg' .format(len(self.legs) + 1))
        print('Added a leg. This human now has {} legs' .format(len(self.legs)))
        return self.legs[-1]

    def add_arm(self):
        self.arms.append('{} arm' .format(len(self.arms) + 1))
        print('Added an arm. This human now has {} arms' .format(len(self.arms)))
        return self.arms[-1]

    def get_gender(self):
        return self.gender


human = Human('M', 35)

human.add_leg()
human.add_leg()
human.add_arm()
human.add_arm()

print(human.get_gender())

human.info()

print(human.info()['Gender'])

