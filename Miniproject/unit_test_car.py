import unittest
import os
from dotenv import load_dotenv
from Miniproject.car import Car
from Miniproject.log import Log

# LOGGER
LOG = Log("__unittest__ ", "car_unit_test_log.log")
logger = LOG.logger


class TestCar(unittest.TestCase):

    def setUp(self):
        # ENV FILE
        load_dotenv()

        # CLASS CAR IN UNIT TEST
        self.car = Car()

    def test_get_trip(self):
        """
        Name: Artiom
        Function Name: test_get_trip
        Description: Testing func get_trip from class car
        Input: Must get km
        Output: Log
        :return: None
        """
        try:
            x = self.car.get_trip(float(os.getenv('TRIP_KM_NUM')))
            self.assertTrue(x)
            logger.info(f"{self.test_get_trip.__doc__}")
        except Exception as e:
            logger.exception(f"{self.test_get_trip.__doc__} Error:{e}")
            raise Exception

    def test_start_engine(self):
        """
        Name: Artiom
        Function Name: test_start_engine
        Description: Testing func start_engine from class car
        Input: None
        Output: Log
        :return: None
        """
        try:
            x = self.car.start_engine()
            self.assertTrue(x)
            logger.info(f"{self.test_start_engine.__doc__}")
        except AssertionError as e:
            logger.exception(f"{self.test_start_engine.__doc__}Error:{e}")
            raise ValueError

    def test_shut_engine(self):
        """
        Name: Artiom
        Function Name: test_shut_engine
        Description: Testing func shut_engine from class car
        Input: None
        Output: Log
        :return: None
        """
        try:
            with self.assertRaises(Exception):
                self.car.shut_engine()
            logger.info(f"{self.test_shut_engine.__doc__}")
        except Exception as e:
            logger.exception(f"{self.test_shut_engine.__doc__} Error:{e}")
            raise Exception

    def test_insert_gear(self):
        """
        Name: Artiom
        Function Name: test_insert_gear
        Description: Testing func insert_gear from class car
        Input: None
        Output: Log
        :return: None
        """
        try:
            x = self.car.insert_gear(float(os.getenv('GEAR_NUM')))
            self.assertTrue(x)
            logger.info(f"{self.test_insert_gear.__doc__}")
        except Exception as e:
            logger.exception(f"{self.test_insert_gear.__doc__} Error:{e}")
            raise Exception

    def test_count_speed(self):
        """
        Name: Artiom
        Function Name: test_count_speed
        Description: Testing func count_speed from class car
        Input: None
        Output: Log
        :return: None
        """
        try:
            x = self.car.count_speed()
            self.assertTrue(x)
            logger.info(f"{self.test_count_speed.__doc__}")
        except Exception as e:
            logger.exception(f"{self.test_count_speed.__doc__} Error:{e}")
            raise Exception

    def test_get_fuel_left(self):
        """
        Name: Artiom
        Function Name: test_get_fuel_left
        Description: Testing func get_fuel_left from class car
        Input: None
        Output: Log
        :return: None
        """
        try:
            x = self.car.get_fuel_left()
            self.assertTrue(x)
            logger.info(f"Successful:{self.test_get_fuel_left.__doc__}")
        except Exception as e:
            logger.exception(f"{self.test_get_fuel_left.__doc__} Error:{e}")
            raise Exception

    def test_count_km_left(self):
        """
        Name: Artiom
        Function Name: test_count_km_left
        Description: Testing func count_km_left by fuel from class car
        Input: None
        Output: Log
        :return: None
        """
        try:
            x = self.car.count_km_left()
            self.assertTrue(x)
            logger.info(f"{self.test_count_km_left.__doc__}")
        except Exception as e:
            logger.exception(f"{self.test_count_km_left.__doc__} Error:{e}")
            raise Exception

    def test_get_money(self):
        """
        Name: Artiom
        Function Name: test_get_money
        Description: Testing func get_money that printing money from class car
        Input: None
        Output: Log
        :return: None
        """
        try:
            x = self.car.get_money()
            self.assertTrue(x)
            logger.info(f"{self.test_get_money.__doc__}")
        except Exception as e:
            logger.exception(f"{self.test_get_money.__doc__} Error:{e}")
            raise Exception

    def test_add_speed(self):
        """
        Name: Artiom
        Function Name: test_add_speed
        Description: Testing func add_speed that adding speed manually (optional method) from class car
        Input: None
        Output: Log
        :return: None
        """
        try:
            with self.assertRaises(Exception):
                self.car.add_speed(float(os.getenv('ADD_SPEED_NUM')))
            logger.info(f"{self.test_add_speed.__doc__}")
        except Exception as e:
            logger.exception(f"{self.test_add_speed.__doc__} Error:{e}")
            raise Exception

    def test_count_gear(self):
        """
        Name: Artiom
        Function Name: test_count_gear
        Description: Testing func count_gear from class car
        Input: None
        Output: Log
        :return: None
        """
        try:
            with self.assertRaises(OSError):
                self.car.count_gear()
            logger.info(f"{self.test_count_gear.__doc__}")
        except Exception as e:
            logger.exception(f"{self.test_count_gear.__doc__} Error:{e}")
            raise Exception

    def test_refuel(self):
        """
        Name: Artiom
        Function Name: test_refuel
        Description: Testing func add_speed that adding speed manually (optional method) from class car
        Input: None
        Output: Log
        :return: None
        """
        try:
            x = self.car.refuel()
            self.assertTrue(x)
            logger.info(f"Successful:{self.test_refuel.__doc__}")
        except Exception as e:
            logger.exception(f"{self.test_refuel.__doc__} Error:{e}")
            raise Exception

    def test_get_speed(self):
        """
        Name: Artiom
        Function Name: test_get_speed
        Description: Testing func get_speed from class car
        Input: None
        Output: Log
        :return: None
        """
        try:
            x = self.car.get_speed()
            self.assertTrue(x)
            logger.info(f"{self.test_get_speed.__doc__}")
        except Exception as e:
            logger.exception(f"{self.test_get_speed.__doc__} Error:{e}")
            raise Exception

    def test_set_speed(self):
        """
        Name: Artiom
        Function Name: test_set_speed
        Description: Testing func get_speed from class car
        Input: None
        Output: Log
        :return: None
        """
        try:
            x = self.car.set_speed(float(os.getenv('SPEED_TO_SET_NUM')))
            self.assertTrue(x)
            logger.info(f"{self.test_set_speed.__doc__}")
        except Exception as e:
            logger.exception(f"{self.test_set_speed.__doc__} Error:{e}")
            raise Exception


if __name__ == '__main__':
    unittest.main()
