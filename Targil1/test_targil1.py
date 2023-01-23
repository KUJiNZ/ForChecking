import unittest
from dotenv import load_dotenv
from connection import Connection

class TestTargil1(unittest.TestCase):

    def setUp(self):
        self.connection = Connection()  # add assertion here


if __name__ == '__main__':
    load_dotenv()
    unittest.main()

