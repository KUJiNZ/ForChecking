import os
from dotenv import load_dotenv
from car import Car
import logging

if __name__ == '__main__':
    # ENV FILE
    load_dotenv()

    #BASIC LOGGER
    logging.basicConfig(level=logging.INFO, filename="car_log_main.log", filemode="a", format="%(asctime)s %("
                                                                                              "levelname)s %(message)s")

    #INSTANCE OF CAR VIA ENV FILE
    fuel_price = float(os.getenv('FUEL_PRICE'))
    money = float(os.getenv('MONEY'))
    fuel_consumption = float(os.getenv('FUEL_CONSUMPTION'))
    fuel_capacity = float(os.getenv('FUEL_CAPACITY'))
    current_fuel = float(os.getenv('current_fuel'))
    max_gear = int(os.getenv('MAX_GEAR'))

    car = Car(fuel_price, money, fuel_consumption, fuel_capacity, current_fuel, max_gear)


    try:
        car.get_trip(10)
        logging.info(f"Successful:{car.get_trip.__doc__}")
    except Exception as e:
        logging.exception(f"{car.get_trip.__doc__} {e}")


