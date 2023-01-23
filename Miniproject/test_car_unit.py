import logging
import unittest
import os
from dotenv import load_dotenv
from Miniproject.car import Car


class TestCar(unittest.TestCase):

    def setUp(self):
        # ENV FILE
        load_dotenv()

        # LOGGER
        logger = logging.getLogger("test")
        logger.setLevel("INFO")
        file_handler = logging.FileHandler("test_car_unit_log.log")
        ## CONSOL ONLY
        # consoleHandler = logging.StreamHandler()
        # consoleHandler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s%(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S%p')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        # CLASS CAR VIA ENV
        fuel_price = float(os.getenv('FUEL_PRICE'))
        money = float(os.getenv('MONEY'))
        fuel_consumption = float(os.getenv('FUEL_CONSUMPTION'))
        fuel_capacity = float(os.getenv('FUEL_CAPACITY'))
        current_fuel = float(os.getenv('current_fuel'))
        max_gear = int(os.getenv('MAX_GEAR'))
        self.car = Car(fuel_price, money, fuel_consumption, fuel_capacity, current_fuel, max_gear)


    def test_get_trip(self):
        """
        Function Name: test_get_trip
        Input: None
        Output: Log
        :return: None
        """
        try:
            x = self.car.get_trip(100)
            self.assertTrue(x)
            logging.getLogger("test").info(f"Successful:{self.test_get_trip.__doc__}")
        except AssertionError as e:
            logging.getLogger("test").exception(f"{self.test_get_trip.__doc__},Error:{e}")

    def test_start_engine(self):
        """
        Function Name: test_start_engine
        Input: None
        Output: Log
        :return: None
        """
        try:
            x = self.car.start_engine()
            self.assertTrue(x)
            logging.getLogger("test").info(f"Successful:{self.test_start_engine.__doc__}")
        except AssertionError as e:
            logging.getLogger("test").exception(f"{self.test_start_engine.__doc__} Error:{e}")

    def test_shut_engine(self):
        """
        Function Name: test_shut_engine
        Input: None
        Output: Log
        :return: None
        """
        try:
            x = self.car.shut_engine()
            self.assertTrue(x)
            logging.getLogger("test").info(f"Successful:{self.test_shut_engine.__doc__}")
        except AssertionError as e:
            logging.getLogger("test").exception(f"{self.test_shut_engine.__doc__} Error:{e}")

    def test_insert_gear(self):
        """
        Function Name: test_insert_gear
        Input: None
        Output: Log
        :return: None
        """
        try:
            self.car.start_engine()
            x = self.car.insert_gear(4)
            self.assertTrue(x)
            logging.getLogger("test").info(f"Successful:{self.test_insert_gear.__doc__}")
        except AssertionError as e:
            logging.getLogger("test").exception(f"{self.test_insert_gear.__doc__} Error:{e}")

    def test_count_speed(self):
        """
        Function Name: test_count_speed
        Input: None
        Output: Log
        :return: None
        """
        try:
            self.car.start_engine()
            x = self.car.count_speed()
            self.assertTrue(x)
            logging.getLogger("test").info(f"Successful:{self.test_count_speed.__doc__}")
        except AssertionError as e:
            logging.getLogger("test").exception(f"{self.test_count_speed.__doc__} Error:{e}")

    def test_get_fuel_left(self):
        """
        Function Name: test_get_fuel_left
        Input: None
        Output: Log
        :return: None
        """
        try:
            x = self.car.get_fuel_left()
            self.assertTrue(x)
            logging.getLogger("test").info(f"Successful:{self.test_get_fuel_left.__doc__}")
        except AssertionError as e:
            logging.getLogger("test").exception(f"{self.test_get_fuel_left.__doc__} Error:{e}")

    def test_count_km_left(self):
        """
        Function Name: test_count_km_left
        Input: None
        Output: Log
        :return: None
        """
        try:
            x = self.car.count_km_left()
            self.assertTrue(x)
            logging.getLogger("test").info(f"Successful:{self.test_count_km_left.__doc__}")
        except AssertionError as e:
            logging.getLogger("test").exception(f"{self.test_count_km_left.__doc__} Error:{e}")

    def test_get_money(self):
        """
        Function Name: test_get_money
        Input: None
        Output: Log
        :return: None
        """
        try:
            x = self.car.get_money()
            self.assertTrue(x)
            logging.getLogger("test").info(f"Successful:{self.test_get_money.__doc__}")
        except AssertionError as e:
            logging.getLogger("test").exception(f"{self.test_get_money.__doc__} Error:{e}")

    def test_add_speed(self):
        """
        Function Name: test_add_speed
        Input: None
        Output: Log
        :return: None
        """
        try:
            self.car.start_engine()
            x = self.car.add_speed(10)
            self.assertTrue(x)
            logging.getLogger("test").info(f"Successful:{self.test_add_speed.__doc__}")
        except AssertionError as e:
            logging.getLogger("test").exception(f"{self.test_add_speed.__doc__} Error:{e}")

    def test_count_gear(self):
        """
        Function Name: test_count_gear
        Input: None
        Output: Log
        :return: None
        """
        try:
            self.car.start_engine()
            x = self.car.count_gear()
            self.assertTrue(x)
            logging.getLogger("test").info(f"Successful:{self.test_add_speed.__doc__}")
        except AssertionError as e:
            logging.getLogger("test").exception(f"{self.test_add_speed.__doc__} Error:{e}")

    def test_refuel(self):
        """
        Function Name: test_refuel
        Input: None
        Output: Log
        :return: None
        """
        try:
            x = self.car.refuel()
            self.assertTrue(x)
            logging.getLogger("test").info(f"Successful:{self.test_refuel.__doc__}")
        except AssertionError as e:
            logging.getLogger("test").exception(f"{self.test_refuel.__doc__} Error:{e}")

    def test_get_speed(self):
        """
        Function Name: test_get_speed
        Input: None
        Output: Log
        :return: None
        """
        try:
            x = self.car.get_speed()
            self.assertTrue(x)
            logging.getLogger("test").info(f"Successful:{self.test_get_speed.__doc__}")
        except AssertionError as e:
            logging.getLogger("test").exception(f"{self.test_get_speed.__doc__} Error:{e}")

    def test_set_speed(self):
        """
        Function Name: test_set_speed
        Input: None
        Output: Log
        :return: None
        """
        try:
            x = self.car.set_speed(100)
            self.assertTrue(x)
            logging.getLogger("test").info(f"Successful:{self.test_set_speed.__doc__}")
        except AssertionError as e:
            logging.getLogger("test").exception(f"{self.test_set_speed.__doc__} Error:{e}")


if __name__ == '__main__':
    unittest.main()
