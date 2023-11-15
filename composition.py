class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(f"{self.name} says {self.sound}")


class Legs:
    def __init__(self, num_legs):
        self.num_legs = num_legs

    def describe(self):
        print(f"This animal has {self.num_legs} legs")


class Scales:
    def __init__(self, scale_type):
        self.scale_type = scale_type

    def describe(self):
        print(f"This animal has {self.scale_type} scales")

class Mammal:
    def __init__(self, name, sound, legs):
        self.animal = Animal(name, sound)
        self.legs = Legs(legs)

    def describe(self):
        self.animal.make_sound()
        self.legs.describe()

class Reptile:
    def __init__(self, name, sound, scales) -> None:
        self.animal = Animal(name, sound)
        self.scales = Scales(scales)

    def describe(self):
        self.animal.make_sound()
        self.scales.describe()


# Using Composition
    
lion = Mammal('Lion', 'roar', 4)
snake = Reptile('Snake', 'hiss', 'smooth')

lion.describe()
snake.describe()