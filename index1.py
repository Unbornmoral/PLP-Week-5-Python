# Parent Class
class Entity:
    def move(self):
        #Generic move method (to be overridden)
        pass

# Dinosaur Class
class Dinosaur(Entity):
    def move(self):
        return "Stomping through the land 🦖"

# Vehicle Classes
class Car(Entity):
    def move(self):
        return "Driving 🚗"

class Boat(Entity):
    def move(self):
        return "Sailing ⛵"

class Plane(Entity):
    def move(self):
        return "Flying ✈️"

# Function to demonstrate polymorphism
def show_movement(entity):
    print(entity.move())

# Creating objects
entities = [Dinosaur(), Car(), Boat(), Plane()]

# Looping through each entity and calling move()
for entity in entities:
    show_movement(entity)
