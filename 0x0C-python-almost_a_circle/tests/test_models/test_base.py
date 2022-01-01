#!/usr/bin/python3
"""
This unittest module tests the class Base in models/base.py
"""

import unittest
from models.base import Base
from models.rectangle import Rectangle


class BaseTest(unittest.TestCase):
    """This class has a battery of functions that test every functionality of
    the class Base in module models/base"""

    def test_None_id(self):
        """Tests if id is set correctly to the number of objects
        instantiated when id is None"""
        b1 = Base()
        self.assertEqual(1, b1.id)
        b2 = Base(None)
        self.assertEqual(2, b2.id)
        b3 = Base()
        self.assertEqual(3, b3.id)
        b4 = Base(None)
        self.assertEqual(4, b4.id)
        b5 = Base()
        self.assertEqual(5, b5.id)
        b1.__del__()
        b2.__del__()
        b3.__del__()
        b4.__del__()
        b5.__del__()

    def test_passed_id(self):
        """Tests if value passed as id is set correctly"""
        b1 = Base(12)
        self.assertEqual(12, b1.id)
        b2 = Base(0)
        self.assertEqual(0, b2.id)
        b3 = Base(1000)
        self.assertEqual(1000, b3.id)
        b4 = Base(9876544)
        self.assertEqual(9876544, b4.id)
        b1.__del__()
        b2.__del__()
        b3.__del__()
        b4.__del__()

    def test_None_and_passed_mix(self):
        """Mixes value and None passed initializations of Base"""
        b1 = Base(12)
        self.assertEqual(12, b1.id)
        b2 = Base(0)
        self.assertEqual(0, b2.id)
        b3 = Base(-12)
        self.assertEqual(-12, b3.id)
        b4 = Base()
        # Since 6 objects will have been made by the previous functions
        self.assertEqual(1, b4.id)
        b5 = Base(None)
        self.assertEqual(2, b5.id)
        b1.__del__()
        b2.__del__()
        b3.__del__()
        b4.__del__()
        b5.__del__()

    def test_to_json_string(self):
        """Tests the to_json_string method from Base"""
        r = Rectangle(2, 8)
        self.assertEqual(r.to_json_string([r.to_dictionary()]),
                         "[{\"id\": 1, \"width\": 2, \"height\": 8, \"x\": "
                         "0, \"y\": 0}]")
        r.update(x=10, y=90)
        self.assertEqual(r.to_json_string([r.to_dictionary()]),
                         "[{\"id\": 1, \"width\": 2, \"height\": 8, \"x\": "
                         "10, \"y\": 90}]")
        self.assertEqual(r.to_json_string([]), "[]")
        self.assertEqual(r.to_json_string(None), "[]")


if __name__ == '__main__':
    unittest.main()
