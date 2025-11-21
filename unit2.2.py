class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some generic animal sound"

    def move(self):
        return "The animal moves around"
class Dog(Animal):
    def speak(self):
        return f"{self.name} says: Woof! Woof!"

    def move(self):
        return f"{self.name} runs happily."
class Cat(Animal):
    def speak(self):
        return f"{self.name} says: Meow!"

    def move(self):
        return f"{self.name} walks gracefully."
class Bird(Animal):
    def speak(self):
        return f"{self.name} says: Tweet! Tweet!"

 def move(self):
        return f"{self.name} flies in the sky."


# --- Taking input from user ---
dog_name = input("Enter Dog's namekk: ")
cat_name = input("Enter Cat's name: ")
bird_name = input("Enter Bird's name: ")

dog = Dog(dog_name)
cat = Cat(cat_name)
bird = Bird(bird_name)

animals = [dog, cat, bird]

print("\n--- Animal Actions ---")
for animal in animals:
    print(animal.speak())
    print(animal.move())