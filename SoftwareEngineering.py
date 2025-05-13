# Unit-I Software Engineering: The software crisis, principles of software engineering, programmingin-the-small vs. programming-in-the-large. 

# Software Engineering: Example of Small vs Large Scale Systems

# Part 1: Programming-in-the-Small (Small Software System)
# Simple Example: A function to calculate the area of a circle.

import math

def calculate_area(radius):
    """ Calculate the area of a circle given the radius. """
    return math.pi * radius ** 2

# Testing the small software system
radius = 5
area = calculate_area(radius)
print(f"The area of a circle with radius {radius} is {area:.2f}.")

# Part 2: Principles of Software Engineering Applied (Small System)
# Here, the system is modular (calculate_area is a self-contained function).
# It is simple and does not require extensive planning or multiple components.
# However, it is limited in scope and scalability.

# Part 3: Programming-in-the-Large (Large Software System)
# More complex example: A basic implementation of a Vehicle System with multiple components.
# This will show principles like abstraction, modularity, and encapsulation.

class Engine:
    def __init__(self, engine_type, horsepower):
        self.engine_type = engine_type
        self.horsepower = horsepower

    def start(self):
        print("Engine started!")

    def stop(self):
        print("Engine stopped!")


class Vehicle:
    def __init__(self, make, model, engine):
        self.make = make
        self.model = model
        self.engine = engine

    def start(self):
        print(f"Starting the {self.make} {self.model}...")
        self.engine.start()

    def stop(self):
        print(f"Stopping the {self.make} {self.model}...")
        self.engine.stop()


class Car(Vehicle):
    def __init__(self, make, model, engine, num_doors):
        super().__init__(make, model, engine)
        self.num_doors = num_doors

    def lock_doors(self):
        print("Locking car doors.")

    def unlock_doors(self):
        print("Unlocking car doors.")


class Truck(Vehicle):
    def __init__(self, make, model, engine, payload_capacity):
        super().__init__(make, model, engine)
        self.payload_capacity = payload_capacity

    def load_cargo(self):
        print(f"Loading cargo with a capacity of {self.payload_capacity}kg.")

    def unload_cargo(self):
        print("Unloading cargo.")


# Example of using the complex system (Programming-in-the-Large)
engine = Engine("V8", 450)
car = Car("Ford", "Mustang", engine, 4)
truck = Truck("Tesla", "Cybertruck", engine, 1500)

car.start()
car.lock_doors()

truck.start()
truck.load_cargo()
truck.stop()

# Part 4: Explanation and Comparison

"""
1. Software Crisis and Principles:
   - In the small case, the system is simple, fast to develop, but has limited scalability and maintainability.
   - In the large case, the system follows principles like modularity, abstraction (Engine, Vehicle), and encapsulation (locking/unlocking doors, loading/unloading cargo).

2. Modularity: The Vehicle, Engine, Car, and Truck are separate classes that can be developed, tested, and maintained independently.
3. Abstraction: Details of the engine start/stop functionality are hidden in the Engine class, simplifying Vehicle and its subclasses.
4. Reusability: Components like the Engine class can be reused in different vehicle types (Car, Truck, etc.).
5. Maintainability: The larger system is easier to update or extend with new vehicle types (e.g., adding a Motorcycle class) without impacting other parts of the system.
6. Scalability: The large system is designed to grow with more vehicle types and features.
"""

# Conclusion:
# - Programming-in-the-small is quick, but programming-in-the-large follows software engineering principles to create maintainable, scalable systems.
