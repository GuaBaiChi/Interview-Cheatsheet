# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        pass


# Child class inheriting from Animal
class Dog(Animal):
    def sound(self):
        return "Woof!"


# Child class inheriting from Animal
class Cat(Animal):
    def sound(self):
        return "Meow!"


# Creating instances of the child classes
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Accessing the inherited methods
print(dog.name)  # Output: Buddy
print(dog.sound())  # Output: Woof!
print(cat.name)  # Output: Whiskers
print(cat.sound())  # Output: Meow!
