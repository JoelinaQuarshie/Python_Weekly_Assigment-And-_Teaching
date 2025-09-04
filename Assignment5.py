#oop 1
class Superhero:
    def __init__(self, name, power, health):
        self.name = name
        self._power = power        # Protected attribute
        self.__health = health     # Private attribute

    def use_power(self):
        print(f"{self.name} uses {self._power}! 💥")

    def get_health(self):
        return self.__health

    def take_damage(self, amount):
        self.__health -= amount
        print(f"{self.name} takes {amount} damage! Current health: {self.__health}")

    def is_alive(self):
        return self.__health > 0


# Inheritance
class FlyingSuperhero(Superhero):
    def __init__(self, name, power, health, flight_speed):
        super().__init__(name, power, health)
        self.flight_speed = flight_speed

    def fly(self):
        print(f"{self.name} is flying at {self.flight_speed} mph! 🕊️")

    def use_power(self):
        print(f"{self.name} unleashes a flying attack with {self._power}! 🌪️")


# Example usage
hero1 = Superhero("Shadow Ninja", "Shadow Strike", 100)
hero2 = FlyingSuperhero("Sky Falcon", "Wind Blast", 120, 500)

hero1.use_power()
hero2.use_power()
hero2.fly()
hero1.take_damage(30)
print(f"{hero1.name} is alive? {hero1.is_alive()}")


#oop 2
#Polymorphism
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")


class Car(Vehicle):
    def move(self):
        print("Driving on the road 🚗")


class Plane(Vehicle):
    def move(self):
        print("Flying in the sky ✈️")


class Boat(Vehicle):
    def move(self):
        print("Sailing on the sea ⛵")


# Using polymorphism
vehicles = [Car(), Plane(), Boat()]

for vehicle in vehicles:
    vehicle.move()