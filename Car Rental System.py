

'''

Car Rental System (Inheritance + Composition)
Create a base class Vehicle with attributes like model, year, and rental_price_per_day. Then, create two subclasses:

Car (with additional attributes like seating_capacity).
Truck (with additional attributes like cargo_capacity). Create a Rental Company class that manages a list of vehicles and allows customers to rent a vehicle for a specified number of days.

'''

class Vehicle:

    def __init__(self,name,model,year,rental_price_per_day):
        self.name = name
        self.model = model
        self.year = year
        self.rental_price_per_day  = rental_price_per_day

    def get_rental_price(self,days):
        return self.rental_price_per_day* days


class Bus(Vehicle):

    def __init__(self,name,model,year,rental_price_per_day,seating_capacity):
        super().__init__(name,model,year,rental_price_per_day)
        self.seating_capacity = seating_capacity


class Truck(Vehicle):

    def __init__(self,name,model,year,rental_price_per_day,cargo_capacity):
        super().__init__(name,model,year,rental_price_per_day)
        self.cargo_capacity = cargo_capacity

class Cycle(Vehicle):
    def __init__(self,name,model,year,rental_price_per_day,man_capacity):
        super().__init__(name,model,year,rental_price_per_day)
        self.man_capacity = man_capacity


class RentalCompany:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def rent_vehicle(self, model, days):
        for vehicle in self.vehicles:
            if vehicle.model == model:
                cost = vehicle.get_rental_price(days)
                return f"{model} rented for {days} days. Total cost: ${cost}"
        return "Vehicle not available."

if __name__ =="__main__":

    my_company = RentalCompany()
