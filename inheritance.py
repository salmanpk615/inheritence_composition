class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(f"{self.name} says {self.sound}")


class Mammal(Animal):
    def __init__(self, name, sound, legs):
        super().__init__(name, sound)
        self.legs = legs

    def describe(self):
        print(f"{self.name} is a mammal with {self.legs} legs")


class Reptile(Animal):
    def __init__(self, name, sound, scales):
        super().__init__(name, sound)
        self.scales = scales

    def describe(self):
        print(f"{self.name} is a reptile with {self.scales} scales")


# using Inheritance

dog = Mammal('Lion', 'roar', 4)
snake = Reptile('Snake', 'hiss', 'smooth')

dog.make_sound()
dog.describe()

snake.make_sound()
snake.describe()
