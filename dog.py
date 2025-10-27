class Dog:
    created = 0

    def __init__(self, name, age, sound="Woof woof"):
        self.age = age
        self.name = name
        self.legs = 4
        self.barked_times = 0
        self.sound = sound
        Dog.created = Dog.created + 1

    def bark(self):
        print(f"{self.name} is now barking: {self.sound}")
        self.barked_times = self.barked_times + 1

    def bark_times(self, times):
        for i in range(times):
            self.bark()

dog1 = Dog("Musti", 1)
dog1.bark_times(3)
print(dog1.barked_times)

dog2 = Dog( "name", 100, "yip yap")
dog2.legs = 3

dog2.bark()
print("Dog2 has barked " + str(dog2.barked_times) + " times")

print("First dog")
print(dog1.age)
print(dog1.name)
print(dog1.legs)

print("Second dog")
print(dog2.age)
print(dog2.name)
print(dog2.legs)


print(f"{Dog.created} dogs created in the main program")