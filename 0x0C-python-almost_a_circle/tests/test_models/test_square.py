#!/usr/bin/python3
"""test_square
Tests the class Square from models/square
"""
import unittest

__import__('sys').path.insert(0, "../../")
Square = __import__("models.square").square.Square


class TestSquare(unittest.TestCase):
    """"""
    def test_all_inherited_methods_work_correctly(self):
        """Checks if all methods Square inherited from Rectangle work as
        intended"""
        s = Square(4)
        self.assertEqual(s.width, 4)
        self.assertEqual(s.height, 4)
        self.assertEqual(s.area(), 16)
        s.update(4, 8, 1, 2)
        self.assertEqual("[Square] (4) 1/2 - 8", s.__str__())
        s.__del__()

    def test_invalid_setting_size(self):

        s = Square(1, 2, 3, 4)

        with self.assertRaises(TypeError) as context:
            s.size = "w"
        self.assertTrue("width must be an integer" in str(context.exception))

        with self.assertRaises(ValueError) as context:
            s.size = 0
        self.assertTrue("width must be > 0" in str(context.exception))

        with self.assertRaises(ValueError) as context:
            s.size = -1
        self.assertTrue("width must be > 0" in str(context.exception))

    def test_update(self):
        """Tests the overridden update method"""
        s = Square(8)
        s.update(12)
        self.assertEqual("[Square] (12) 0/0 - 8", s.__str__())
        s.update(7, 18, 2, 4, 5, 6, 7, 8, 9)
        self.assertEqual("[Square] (7) 2/4 - 18", s.__str__())
        s.update(7, 8)
        self.assertEqual("[Square] (7) 2/4 - 8", s.__str__())
        s.update(7, 8, 3)
        self.assertEqual("[Square] (7) 3/4 - 8", s.__str__())

        s.update(id=10)
        self.assertEqual("[Square] (10) 3/4 - 8", s.__str__())
        s.update(x=10)
        self.assertEqual("[Square] (10) 10/4 - 8", s.__str__())
        s.update(y=10)
        self.assertEqual("[Square] (10) 10/10 - 8", s.__str__())
        s.update(mnm=19)
        self.assertEqual("[Square] (10) 10/10 - 8", s.__str__())
        s.update(size_widht=8)
        self.assertEqual("[Square] (10) 10/10 - 8", s.__str__())


if __name__ == '__main__':
    unittest.main()
