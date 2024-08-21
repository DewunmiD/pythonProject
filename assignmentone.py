class Animal:
    def __init__(self, breed, age):
        self.breed = breed
        self.age = age

    def speak(self):
        return None


class Dog(Animal):
    def __init__(self, breed, age):
        super().__init__(breed, age)


    def speak(self):
        print("Bark!")


class Cat(Animal):
    def __init__(self, breed, age):
        super().__init__(breed, age)

    def speak(self):
        print("Meow!")


dog = Dog("Pitbull", 2)
cat = Cat("Black and White", 4)


dog.speak()
cat.speak()
