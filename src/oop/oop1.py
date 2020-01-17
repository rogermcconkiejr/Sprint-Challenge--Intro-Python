# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

class Vehicle:
    # This class is the base class
        pass

class GroundVehicle(Vehicle):
    # Subclass of Vehicle class
        pass


class Car(GroundVehicle):
    # Subclass of Ground Vehicle class
        pass

class Motorcycle(GroundVehicle):
    # Subclass of Ground Vehicle class
        pass

class FlightVehicle(Vehicle):
    # Subclass of Vehicle class
        pass

class Airplane(FlightVehicle):
    # Subclass of FlightVehicle class
        pass

class Starship(FlightVehicle):
    # Subclass of FlightVehicle class
        pass