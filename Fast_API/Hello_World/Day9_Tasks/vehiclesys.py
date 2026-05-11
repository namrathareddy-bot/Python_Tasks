class Vehicle:
    def __init__(self,brand,speed):
        self.brand=brand
        self.speed=speed
class Bike(Vehicle):
    def display(self):
        print("Bike brand:",self.brand)
        print("Speed:",self.speed)

class Bike(Vehicle):
    def display(self):
        print("Bike brand:",self.brand)
        print("Bike speed:",self.speed)
c=Car("Honda",130)
b=Bike("BMW",170)
c.display()
b.display()
