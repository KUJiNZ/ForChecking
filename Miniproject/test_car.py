import logging
import pytest
import os
from dotenv import load_dotenv
from Miniproject.car import Car


@pytest.fixture
def car():
    # ENV FILE
    load_dotenv()

    # LOGGER
    logger = logging.getLogger("pytest")
    logger.setLevel("INFO")
    file_handler = logging.FileHandler("test_car_py_log.log")
    formatter = logging.Formatter('%(asctime)s - %(name)s%(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S%p')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # CAR ClASS
    fuel_price = float(os.getenv('FUEL_PRICE'))
    money = float(os.getenv('MONEY'))
    fuel_consumption = float(os.getenv('FUEL_CONSUMPTION'))
    fuel_capacity = float(os.getenv('FUEL_CAPACITY'))
    current_fuel = float(os.getenv('current_fuel'))
    max_gear = int(os.getenv('MAX_GEAR'))
    return Car(fuel_price, money, fuel_consumption, fuel_capacity, current_fuel, max_gear)


def test_get_trip(car):
    """
    Function Name: test_get_trip
    Description: Testing func get_trip from class car
    Input: None
    Output: Log
    :return: None
    """
    try:
        x = car.get_trip(float(os.getenv('NORMAL_TRIP_KM')))
        assert x is True
        logging.getLogger("pytest").info(f"Successful:{test_get_trip.__doc__}")
    except AssertionError as e:
        logging.getLogger("pytest").exception(f"{test_get_trip.__doc__},Error:{e}")


def test_start_engine(car):
    """
    Function Name: test_start_engine
    Description: Testing func start_engine from class car
    Input: None
    Output: Log
    :return: None
    """
    try:
        x = car.start_engine()
        assert x is True
        logging.getLogger("pytest").info(f"Successful:{test_start_engine.__doc__}")
    except AssertionError as e:
        logging.getLogger("pytest").exception(f"{test_start_engine.__doc__} Error:{e}")


def test_shut_engine(car):
    """
    Function Name: test_shut_engine
    Description: Testing func start_engine from class car
    Input: None
    Output: Log
    :return: None
    """
    try:
        with pytest.raises(Exception,match="Engine is shut yet"):
            car.shut_engine()
        logging.getLogger("pytest").info(f"Successful:{test_shut_engine.__doc__}")
    except AssertionError as e:
        logging.getLogger("pytest").exception(f"{test_shut_engine.__doc__} Error:{e}")


def test_insert_gear(car):
    """
    Function Name: test_insert_gear
    Description: Testing func insert_gear from class car
    Input: None
    Output: Log
    :return: None
    """
    try:
        x = car.insert_gear(float(os.getenv('NORMAL_GEAR')))
        assert x is True
        logging.getLogger("pytest").info(f"Successful:{test_insert_gear.__doc__}")
    except AssertionError as e:
        logging.getLogger("pytest").exception(f"{test_insert_gear.__doc__} Error:{e}")


def test_count_speed(car):
    """
    Function Name: test_count_speed
    Description: Testing func count_speed from class car
    Input: None
    Output: Log
    :return: None
    """
    try:
        x = car.count_speed()
        assert x is True
        logging.getLogger("pytest").info(f"Successful:{test_count_speed.__doc__}")
    except AssertionError as e:
        logging.getLogger("pytest").exception(f"{test_count_speed.__doc__} Error:{e}")


def test_get_fuel_left(car):
    """
    Function Name: test_get_fuel_left
    Description: Testing func get_fuel_left from class car
    Input: None
    Output: Log
    :return: None
    """
    try:
        x = car.get_fuel_left()
        assert x is True
        logging.getLogger("pytest").info(f"Successful:{test_get_fuel_left.__doc__}")
    except AssertionError as e:
        logging.getLogger("pytest").exception(f"{test_get_fuel_left.__doc__} Error:{e}")


def test_count_km_left(car):
    """
    Function Name: test_count_km_left
    Description: Testing func count_km_left by fuel from class car
    Input: None
    Output: Log
    :return: None
    """
    try:
        x = car.count_km_left()
        assert x is True
        logging.getLogger("pytest").info(f"Successful:{test_count_km_left.__doc__}")
    except AssertionError as e:
        logging.getLogger("pytest").exception(f"{test_count_km_left.__doc__} Error:{e}")


def test_get_money(car):
    """
    Function Name: test_get_money
    Description: Testing func get_money that printing money from class car
    Input: None
    Output: Log
    :return: None
    """
    try:
        x = car.get_money()
        assert x is True
        logging.getLogger("pytest").info(f"Successful:{test_get_money.__doc__}")
    except AssertionError as e:
        logging.getLogger("pytest").exception(f"{test_get_money.__doc__} Error:{e}")


def test_add_speed(car):
    """
    Function Name: test_add_speed
    Description: Testing func add_speed that adding speed manually (optional method) from class car
    Input: None
    Output: Log
    :return: None
    """
    try:
        car.start_engine()
        x = car.add_speed(float(os.getenv('ADD_NORMAL_SPEED')))
        assert x is True
        logging.getLogger("pytest").info(f"Successful:{test_add_speed.__doc__}")
    except AssertionError as e:
        logging.getLogger("pytest").exception(f"{test_add_speed.__doc__} Error:{e}")


def test_count_gear(car):
    """
    Function Name: test_count_gear
    Description: Testing func count_gear from class car
    Input: None
    Output: Log
    :return: None
    """
    try:
        with pytest.raises(OSError,match="Car not driving"):
            car.count_gear()
        logging.getLogger("pytest").info(f"Successful:{test_add_speed.__doc__}")
    except AssertionError as e:
        logging.getLogger("pytest").exception(f"{test_add_speed.__doc__} Error:{e}")


def test_refuel(car):
    """
    Function Name: test_refuel
    Description: Testing func add_speed that adding speed manually (optional method) from class car
    Input: None
    Output: Log
    :return: None
    """
    try:
        x = car.refuel()
        assert x is True
        logging.getLogger("pytest").info(f"Successful:{test_refuel.__doc__}")
    except AssertionError as e:
        logging.getLogger("pytest").exception(f"{test_refuel.__doc__} Error:{e}")


def test_get_speed(car):
    """
    Function Name: test_get_speed
    Description: Testing func get_speed from class car
    Input: None
    Output: Log
    :return: None
    """
    try:
        x = car.get_speed()
        assert x is True
        logging.getLogger("pytest").info(f"Successful:{test_get_speed.__doc__}")
    except AssertionError as e:
        logging.getLogger("pytest").exception(f"{test_get_speed.__doc__} Error:{e}")


def test_set_speed(car):
    """
    Function Name: test_set_speed
    Description: Testing func get_speed from class car
    Input: None
    Output: Log
    :return: None
    """
    try:
        x = car.set_speed(float(os.getenv('NORMAL_SPEED_TO_SET')))
        assert x is True
        logging.getLogger("pytest").info(f"Successful:{test_set_speed.__doc__}")
    except AssertionError as e:
        logging.getLogger("pytest").exception(f"{test_set_speed.__doc__} Error:{e}")
