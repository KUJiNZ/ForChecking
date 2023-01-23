import os
from dotenv import load_dotenv
class Car:
    fuel_price = 0
    money = 0
    gear = 0
    max_gear = 0
    speed = 0
    fuel_consumption = 0 #per 100km
    kmh_increasing = 30
    fuel_capacity = 0
    current_fuel = 0
    engine_start = False
    km_left = 0
    max_speed = 0


    def __init__(self):
        # INSERT OF CAR VIA ENV FILE
        load_dotenv()
        self.fuel_price = float(os.getenv('FUEL_PRICE'))
        self.money = float(os.getenv('MONEY'))
        self.fuel_consumption = float(os.getenv('FUEL_CONSUMPTION'))
        self.fuel_capacity = float(os.getenv('FUEL_CAPACITY'))
        self.current_fuel = float(os.getenv('current_fuel'))
        self.max_gear = int(os.getenv('MAX_GEAR'))
        self.count_km_left()





    def start_engine(self):
        """
        Name: Artiom
        Function Name: start_engine
        Description: Starting engine
        Input: None
        Output: Engine is started
        """
        if self.engine_start is False and self.gear == 0:
            self.engine_start = True
            print("Engine is started")
            return True
        else:
            raise Exception("Engine is started or gear is set!")





    def shut_engine(self):
        """
        Name: Artiom
        Function Name: shut_engine
        Description: Shut down the engine
        Input: None
        Output: Engine is shut down
        """
        if self.engine_start is True:
            self.engine_start = False
            print("Engine is shut down")
            return True
        else:
            raise Exception("Engine is shut yet")




    def insert_gear(self,gear_num):
        """
        Name: Artiom
        Function Name: insert_gear
        Description: Inserting gear
        Input: number of gear
        Output: Current gear
        """
        if self.max_gear > gear_num > 0:
            self.gear = gear_num
            return True
        else:
            raise Exception("Illegal gear insert!")

    def count_speed(self):
        """
        Name: Artiom
        Function Name: count_speed
        Description: Counting current speed
        Input: None
        Output: Current speed
        """
        if self.gear is not None and self.kmh_increasing is not None:
            self.speed = self.gear * self.kmh_increasing
            return True
        else:
            raise Exception("Gear or kmh_increasing is None")


    def get_fuel_left(self):
        """
        Name: Artiom
        Function Name: get_fuel_left
        Description: Get current fuel
        Input: None
        Output: Current fuel
        """
        print(f"Fuel = {self.current_fuel}")
        return True

    def count_km_left(self):
        """
        Name: Artiom
        Function Name: count_km_left
        Description: Counting how much km can drive
        Input: None
        Output: None
        """
        self.km_left = self.current_fuel / self.fuel_consumption
        return True




    def get_money(self):
        """
        Name: Artiom
        Function Name: get_money
        Description: Getting money
        Input: None
        Output: None
        """
        print(self.money)
        return True


    def add_speed(self,num):
        """
        Name: Artiom
        Function Name: add_speed
        Description: Manually adding speed
        Input: None
        Output: Current speed
        """
        if self.engine_start is True and (self.speed == 0 or (self.speed*self.max_gear) > self.speed + num):
            self.speed += num
            self.count_gear()
            self.get_speed()
            return True
        else:
            raise Exception("Illegal speed!")

    def count_gear(self):
        """
        Name: Artiom
        Function Name: count_gear
        Description: Counting number of gear while insert speed manually
        Input: None
        Output: Engine is started
        """
        if self.speed > 0:
            if self.speed > 30:
                self.gear = round(self.speed / 30)
            else:
                self.gear = 1
            print(f"Gear = {self.gear}")
            return True
        else:
            self.gear = 0
            raise OSError("Car not driving")

    def get_speed(self):
        """
        Name: Artiom
        Function Name: get_speed
        Description: Getting speed
        Input: None
        Output: Current_speed
        """
        print(f"Speed = {self.speed}")
        return True

    def set_speed(self,speed):
        """
        Name: Artiom
        Function Name: set_speed
        Description: Manually setting speed
        Input: speed
        """
        if speed <= self.max_gear*self.kmh_increasing:
            self.speed = speed
            return True
        else:
            raise Exception("Illegal speed insert!")


    def refuel(self):
        """
        Name: Artiom
        Function Name: refuel
        Description: Fefuel the car by money
        Input: None
        Output: Engine is started
        """
        if self.money > 0:
            price = self.fuel_price * (self.fuel_capacity - self.current_fuel)
            need = self.fuel_capacity - self.current_fuel
            if price < self.money:
                self.money -= price
                self.current_fuel += need
                print("The car is max filled successfully!")
            else:
                self.current_fuel += self.money/self.fuel_price
                raise Warning("Not enough money to fill full tank,will be fill max as possible")
            return True
        else:
            raise Exception("Not enough money to refuel")

    def get_trip(self,km_to_pass):
        """
        Name: Artiom
        Function Name: get_trip
        Description: Getting trip by km
        Input: km to drive
        Output: Ready
        """
        if self.km_left < km_to_pass:
            self.refuel()
            self.count_km_left()
            print("REFUELED")
        if self.km_left >= km_to_pass:
            self.start_engine()
            self.km_left -= km_to_pass
            self.current_fuel -= km_to_pass * self.fuel_consumption
            print("DRIVING")
            self.set_speed(120)
            self.get_speed()
            self.count_gear()
            return True
        else:
            raise ValueError("Not enough fuel,need to refuel")


