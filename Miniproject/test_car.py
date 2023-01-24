import pytest
import os
from dotenv import load_dotenv
from Miniproject.car import Car
from Miniproject.log import Log

# LOGGER
LOG = Log("__pytest__ ", "test_car_py_log.log")
logger = LOG.logger


@pytest.fixture
def car():
    # ENV FILE
    load_dotenv()

    # CAR ClASS
    return Car()


@pytest.mark.trip
def test_get_trip(car):
    """
    Name: Artiom
    Function Name: test_get_trip
    Description: Testing func get_trip from class car
    Input: None
    Output: Log
    :return: None
    """
    try:
        x=car.get_trip(float(os.getenv('TRIP_KM_NUM')))
        assert x is True
        logger.info(f"{test_get_trip.__doc__}")
    except Exception as e:
        logger.error(f"{test_get_trip.__doc__}Error:{e}")
        raise

@pytest.mark.start_engine
def test_start_engine(car):
    """
    Name: Artiom
    Function Name: test_start_engine
    Description: Testing func start_engine from class car
    Input: None
    Output: Log
    :return: None
    """
    try:
        x = car.start_engine()
        assert x is True
        logger.info(f"{test_start_engine.__doc__}")
    except Exception as e:
        logger.exception(f"{test_start_engine.__doc__} Error:{e}")
        raise


@pytest.mark.shut_engine
def test_shut_engine(car):
    """
    Name: Artiom
    Function Name: test_shut_engine
    Description: Testing func start_engine from class car
    Input: None
    Output: Log
    :return: None
    """
    try:
        car.start_engine()
        x = car.shut_engine()
        assert x is True
        logger.info(f"{test_shut_engine.__doc__}")
    except Exception as e:
        logger.exception(f"{test_shut_engine.__doc__} Error:{e}")
        raise

@pytest.mark.insert_gear
def test_insert_gear(car):
    """
    Name: Artiom
    Function Name: test_insert_gear
    Description: Testing func insert_gear from class car
    Input: None
    Output: Log
    :return: None
    """
    try:
        x = car.insert_gear(float(os.getenv('GEAR_NUM')))
        assert x is True
        logger.info(f"{test_insert_gear.__doc__}")
    except AssertionError as e:
        logger.exception(f"{test_insert_gear.__doc__} Error:{e}")
        raise


@pytest.mark.count_speed
def test_count_speed(car):
    """
    Name: Artiom
    Function Name: test_count_speed
    Description: Testing func count_speed from class car
    Input: None
    Output: Log
    :return: None
    """
    try:
        x = car.count_speed()
        assert x is True
        logger.info(f"{test_count_speed.__doc__}")
    except Exception as e:
        logger.exception(f"{test_count_speed.__doc__} Error:{e}")


@pytest.mark.fuel_left
def test_get_fuel_left(car):
    """
    Name: Artiom
    Function Name: test_get_fuel_left
    Description: Testing func get_fuel_left from class car
    Input: None
    Output: Log
    :return: None
    """
    try:
        x = car.get_fuel_left()
        assert x is True
        logger.info(f"{test_get_fuel_left.__doc__}")
    except AssertionError as e:
        logger.exception(f"{test_get_fuel_left.__doc__} Error:{e}")
        raise


@pytest.mark.km_left
def test_count_km_left(car):
    """
    Name: Artiom
    Function Name: test_count_km_left
    Description: Testing func count_km_left by fuel from class car
    Input: None
    Output: Log
    :return: None
    """
    try:
        x = car.count_km_left()
        assert x is True
        logger.info(f"{test_count_km_left.__doc__}")
    except Exception as e:
        logger.exception(f"{test_count_km_left.__doc__} Error:{e}")
        raise


@pytest.mark.get_money
def test_get_money(car):
    """
    Name: Artiom
    Function Name: test_get_money
    Description: Testing func get_money that printing money from class car
    Input: None
    Output: Log
    :return: None
    """
    try:
        x = car.get_money()
        assert x is True
        logger.info(f"{test_get_money.__doc__}")
    except Exception as e:
        logger.exception(f"{test_get_money.__doc__} Error:{e}")
        raise


@pytest.mark.add_speed
def test_add_speed(car):
    """
    Name: Artiom
    Function Name: test_add_speed
    Description: Testing func add_speed that adding speed manually (optional method) from class car
    Input: None
    Output: Log
    :return: None
    """
    try:
        car.start_engine()
        x = car.add_speed(float(os.getenv('ADD_SPEED_NUM')))
        assert x is True
        logger.info(f"{test_add_speed.__doc__}")
    except Exception as e:
        logger.exception(f"{test_add_speed.__doc__} Error:{e}")
        raise


@pytest.mark.count_gear
def test_count_gear(car):
    """
    Name: Artiom
    Function Name: test_count_gear
    Description: Testing func count_gear from class car
    Input: None
    Output: Log
    :return: None
    """
    try:
        car.set_speed(float(os.getenv('SPEED_TO_SET_NUM')))
        x = car.count_gear()
        assert x is True
        logger.info(f"{test_count_gear.__doc__}")
    except Exception as e:
        logger.exception(f"{test_count_gear.__doc__} Error:{e}")
        raise


@pytest.mark.trip
def test_refuel(car):
    """
    Name: Artiom
    Function Name: test_refuel
    Description: Testing func add_speed that adding speed manually (optional method) from class car
    Input: None
    Output: Log
    :return: None
    """
    try:
        x = car.refuel()
        assert x is True
        logger.info(f"Successful:{test_refuel.__doc__}")
    except AssertionError as e:
        logger.exception(f"{test_refuel.__doc__} Error:{e}")


@pytest.mark.get_speed
def test_get_speed(car):
    """
    Name: Artiom
    Function Name: test_get_speed
    Description: Testing func get_speed from class car
    Input: None
    Output: Log
    :return: None
    """
    try:
        x = car.get_speed()
        assert x is True
        logger.info(f"{test_get_speed.__doc__}")
    except Exception as e:
        logger.exception(f"{test_get_speed.__doc__} Error:{e}")
        raise


@pytest.mark.set_speed
def test_set_speed(car):
    """
    Name: Artiom
    Function Name: test_set_speed
    Description: Testing func get_speed from class car
    Input: None
    Output: Log
    :return: None
    """
    try:
        x = car.set_speed(float(os.getenv('SPEED_TO_SET_NUM')))
        assert x is True
        logger.info(f"{test_set_speed.__doc__}")
    except Exception as e:
        logger.exception(f"{test_set_speed.__doc__} Error:{e}")
        raise
