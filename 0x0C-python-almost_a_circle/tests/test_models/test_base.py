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
        new_base = Base()
        self.assertEqual(1, new_base.id)
        new_base = Base(None)
        self.assertEqual(2, new_base.id)
        new_base = Base()
        self.assertEqual(3, new_base.id)
        new_base = Base(None)
        self.assertEqual(4, new_base.id)
        new_base = Base()
        self.assertEqual(5, new_base.id)

    def test_passed_id(self):
        """Tests if value passed as id is set correctly"""
        new_base = Base(12)
        self.assertEqual(12, new_base.id)
        new_base = Base(0)
        self.assertEqual(0, new_base.id)
        new_base = Base(1000)
        self.assertEqual(1000, new_base.id)
        new_base = Base(9876544)
        self.assertEqual(9876544, new_base.id)
        # Number of objects created should become 4
        self.assertEqual(4, Base.__nb_objects)

    def test_None_and_passed_mix(self):
        """Mixes value and None passed initializations of Base"""
        new_base = Base(12)
        self.assertEqual(12, new_base.id)
        new_base = Base(0)
        self.assertEqual(0, new_base.id)
        new_base = Base()
        self.assertEqual(3, new_base.id)
        new_base = Base(None)
        self.assertEqual(4, new_base.id)
        # Number of objects created should become 4
        self.assertEqual(4, Base.__nb_objects)


if __name__ == '__main__':
    unittest.main()
