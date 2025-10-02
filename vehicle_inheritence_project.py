class Vehicle:
    def __init__(self,brand,model,year,rate_per_day):
        self.brand=brand
        self.model=model
        self.year=year
        self.rate_per_day=rate_per_day
    def rent_price(self, days):
        price = days * self.rate_per_day
        print(f"Vehicle rent price for {days} days is {price}")
        return price
    def display_info(self):
        print(f"vehicle brand is {self.brand},vehicle model is {self.model},vehicle innovation year is {self.year}")
class Car(Vehicle):
    def __init__(self,brand,model,year,rate_per_day,fuel_requried):
        super().__init__(brand, model, year, rate_per_day)
        self.fuel_required=fuel_requried
    def display_info(self):
        super().display_info()
        print(f"fuel_required for car is:{self.fuel_required} litres")  
class Electric_Bus(Vehicle):
    def __init__(self,brand,model,year,rate_per_day,charge_required):
        super().__init__(brand,model,year,rate_per_day)
        self.charge_required=charge_required
    def display_info(self):
        super().display_info()
        print(f"charge required for bus is {self.charge_required} Watt")
class Truck(Vehicle):
    def __init__(self,brand,model,year,rate_per_day,load):
        super().__init__(brand,model,year,rate_per_day)
        self.load=load
    def display_info(self):
        super().display_info()
        print(f"Truck carries the load is  {self.load}Kg")   
Vehicle_1=Vehicle("TATA","COROLLA",2020,5)
Vehicle_2=Vehicle("KIA","KIAS",2033,4)
Vehicle_1.display_info()
Vehicle_1.rent_price(5)   
Vehicle_2.display_info()
Vehicle_2.rent_price(4)
Car_1=Car("suzuki","Corolla",2023,5,50)
Car_1.display_info()
Bus_1=Electric_Bus("vola","luxury",2045,5,80)
Bus_1.display_info()
Truck_1=Truck("ashokleland","super",2023,5,500)
Truck_1.display_info()