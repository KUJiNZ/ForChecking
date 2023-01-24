import os
from dotenv import load_dotenv
from car import Car
from log import Log

if __name__ == '__main__':
    # ENV FILE
    load_dotenv()

    # LOGGER
    LOG = Log("__main__", "car_log_main.log")
    logger = LOG.logger

    # CLASS CAR
    car = Car()

    try:
        car.get_trip(float(os.getenv('NORMAL_TRIP_KM')))
        logger.info(f"Successful:{car.get_trip.__doc__}")
    except Exception as e:
        logger.exception(f"{car.get_trip.__doc__} {e}")
