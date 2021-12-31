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


if __name__ == '__main__':
    unittest.main()
