class Animal:
    def make_sound(self):
        print("Some generic animal sound.")

class Dog(Animal):
    def make_sound(self):
        print("Woof! Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

class Bird(Animal):
    def make_sound(self):
        print("Tweet! Tweet!")


animal_type = input("Enter animal type (dog/cat/bird): ").lower()

if animal_type == "dog":
    animal = Dog()
elif animal_type == "cat":
    animal = Cat()
elif animal_type == "bird":
    animal = Bird()
else:
    animal = Animal()

animal.make_sound()