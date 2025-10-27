class Vehicle:
    def __init__(self, speed):
        self.speed = speed

    def has_wheels(self):
        return True

class SportItem:
    def __init__(self, weight):
        self.weight = weight

    def can_be_played(self):
        return True

class Bicycle(SportItem, Vehicle):
    def __init__(self, speed, weight):
        Vehicle.__init__(self, speed)
        SportItem.__init__(self, weight)



bike = Bicycle(100, 15)

print(bike.speed)
print(bike.weight)

bike.can_be_played()
bike.has_wheels()
