import unittest

__import__('sys').path.insert(0, "../../")
Base = __import__("models.base").base.Base

"""
This unittest module tests the class Base in models/base.py
"""


class BaseClassTest(unittest.TestCase):
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
        # nb_objects should be zero since no object was initialized with id
        # as None
        self.assertEqual(0, Base.__nb_objects)

    def test_None_and_passed_mix(self):
        """Mixes value and None passed initializations of Base"""
        b1 = Base(12)
        self.assertEqual(12, b1.id)
        b2 = Base(0)
        self.assertEqual(0, b2.id)
        b3 = Base(-12)
        self.assertEqual(-12, b3.id)
        b4 = Base()
        self.assertEqual(1, b4.id)
        b5 = Base(None)
        self.assertEqual(2, b5.id)
        # nb_objects should be 2 since only 2 objects were initialized with id
        # as None
        self.assertEqual(2, Base.__nb_objects)


if __name__ == '__main__':
    unittest.main()
