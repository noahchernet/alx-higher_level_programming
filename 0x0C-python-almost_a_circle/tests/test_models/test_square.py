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
        s.update(4, 8, 8, 1, 2)
        self.assertEqual("[Square] (4) 1/2 - 8", s.__str__())

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


if __name__ == '__main__':
    unittest.main()
