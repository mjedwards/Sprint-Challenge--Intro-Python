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

# # base Class
# class Vehicle:
#     def __init__(self, vehicle):
#         self.vehicle = vehicle

# # base Class for Airplane
# class FlightVehicle(Vehicle):
#     def __init__(self, flight_vehicle):
#         self.flight_vehicle = flight_vehicle

# class Airplane(FlightVehicle):
#     def __init__(self, plane, flight_vehicle):
#         self.plane = plane 
#         super(Airplane, self).__init__(flight_vehicle)
    


# class Starship:
#     def __init__(self, starship):
#         self.starship = starship


# class GroundVehicle(Vehicle):
#     def __init__(self, ground_vehicle, vehicle):
#         self.ground_vehicle = ground_vehicle
#         super(GroundVehicle, self).__init__(vehicle)


# class Motorcycle(GroundVehicle):
#     def __init__(self, motorcycle, ground_vehicle, vehicle):
#         self.motorcycle = motorcycle 
#         super(Motorcycle, self).__init__(ground_vehicle, vehicle)

# class Car(GroundVehicle):
#     def __init__(self, car, ground_vehicle, vehicle):
#         self.car = car 
#         super(Car, self).__init__(ground_vehicle, vehicle)
    



# base Class
class Vehicle:
    pass

# base Class for Airplane
class FlightVehicle(Vehicle):
    pass

class Airplane(FlightVehicle):
    pass
    


class Starship(FlightVehicle):
    pass


class GroundVehicle(Vehicle):
    pass


class Motorcycle(GroundVehicle):
    pass

class Car(GroundVehicle):
   pass
    

