import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr1(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")

    def test_repr2(self):
        loc = Location("Paris", 48.9, -2.4)
        self.assertEqual(repr(loc),"Location('Paris', 48.9, -2.4)")

    def test_repr3(self):
        loc = Location("London", 150.145, -12.325)
        self.assertEqual(repr(loc),"Location('London', 150.145, -12.325)")

    def test_eq1(self):
        loc1 = Location("SLO", 35.3, -120.7)
        loc2 = Location("SLO", 35.3, -120.7)
        self.assertEqual(loc1 == loc2, True)

    def test_eq2(self):
        loc1 = Location("SLO", 35.3, -120.7)
        loc2 = loc1
        self.assertEqual(loc1 == loc2, True)

    def test_eq3(self):
        loc1 = Location("SLO", 35.3, -120.7)
        loc2 = Location("LA",  41.7, -60.1)
        self.assertEqual(loc1 == loc2, False)

if __name__ == "__main__":
        unittest.main()
