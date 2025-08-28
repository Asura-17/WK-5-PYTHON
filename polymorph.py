class Car:
    def move(self):
        print("🚗 Driving on the road")

class Plane:
    def move(self):
        print("✈️ Flying in the sky")

class Boat:
    def move(self):
        print("⛵ Sailing on the sea")



vehicles = [Car(), Plane(), Boat()]

for vehicle in vehicles:
    vehicle.move()  
