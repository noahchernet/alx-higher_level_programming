#!/usr/bin/python3
"""
This unittest module test_rectangle tests the class Rectangle in
models/rectangle
"""
import unittest

__import__('sys').path.insert(0, "../../")
Rectangle = __import__("models.rectangle").rectangle.Rectangle


class RectangleTest(unittest.TestCase):
    """This class has a battery of functions that test every functionality of
    the class Rectangle in module models/rectangle"""

    def test_1_import_works_correctly(self):
        """Checks if id is set correctly when many objects are instantiated
        from Rectangle (which inherits from Base)"""
        r1 = Rectangle(10, 12)
        self.assertEqual(1, r1.id)
        r2 = Rectangle(8, 9, 2, 3)
        self.assertEqual(2, r2.id)
        r3 = Rectangle(1, 7, 4, 9)
        self.assertEqual(3, r3.id)
        r4 = Rectangle(1, 7, 4, 9, 12)
        self.assertEqual(12, r4.id)
        r5 = Rectangle(1, 7, 4, 9, 897)
        self.assertEqual(897, r5.id)
        r6 = Rectangle(1, 7, 4, 9)
        self.assertEqual(4, r6.id)

    def test_2_getters_setters(self):
        """Checks if getters and setters work as intended"""
        r1 = Rectangle(1, 2, 3, 4)
        self.assertEqual(1, r1.width)
        self.assertEqual(2, r1.height)
        self.assertEqual(3, r1.x)
        self.assertEqual(4, r1.y)

        r1.width = 20
        self.assertEqual(20, r1.width)
        r1.height = 60
        self.assertEqual(60, r1.height)
        r1.x = 7
        self.assertEqual(7, r1.x)
        r1.y = 8
        self.assertEqual(8, r1.y)

    def test_3_invalid_initialization_and_setting_values(self):
        """Tests if every exception is correctly raised for each attribute
        in Rectangle
        """

        #  Checks for object initialization

        with self.assertRaises(TypeError) as context:
            Rectangle("w", 1, 2, 3)
        self.assertTrue("width must be an integer" in str(context.exception))

        with self.assertRaises(TypeError) as context:
            Rectangle("1", "1", 2, 3)
        self.assertTrue("width must be an integer" in str(context.exception))

        with self.assertRaises(TypeError) as context:
            Rectangle("1", "1", 2, 3)
        self.assertTrue("width must be an integer" in str(context.exception))

        with self.assertRaises(ValueError) as context:
            Rectangle(-2, "1", 2, 3)
        self.assertTrue("width must be > 0" in str(context.exception))

        with self.assertRaises(ValueError) as context:
            Rectangle(0, 0, 2, 3)
        self.assertTrue("width must be > 0" in str(context.exception))

        with self.assertRaises(TypeError) as context:
            Rectangle(2, "1", 2, 3)
        self.assertTrue("height must be an integer" in str(context.exception))

        with self.assertRaises(TypeError) as context:
            Rectangle(2, "1", "2", 3)
        self.assertTrue("height must be an integer" in str(context.exception))

        with self.assertRaises(TypeError) as context:
            Rectangle(2, "1", 2, 3)
        self.assertTrue("height must be an integer" in str(context.exception))

        with self.assertRaises(ValueError) as context:
            Rectangle(2, -1, 2, 3)
        self.assertTrue("height must be > 0" in str(context.exception))

        with self.assertRaises(ValueError) as context:
            Rectangle(1, 0, 2, 3)
        self.assertTrue("height must be > 0" in str(context.exception))

        with self.assertRaises(ValueError) as context:
            Rectangle(2, 0, 2, 3)
        self.assertTrue("height must be > 0" in str(context.exception))

        with self.assertRaises(TypeError) as context:
            Rectangle(2, 1, "2", 3)
        self.assertTrue("x must be an integer" in str(context.exception))

        with self.assertRaises(ValueError) as context:
            Rectangle(1, 1, -1, 3)
        self.assertTrue("x must be >= 0" in str(context.exception))

        with self.assertRaises(TypeError) as context:
            Rectangle(2, 1, 2, "3")
        self.assertTrue("y must be an integer" in str(context.exception))

        with self.assertRaises(ValueError) as context:
            Rectangle(1, 1, 1, -3)
        self.assertTrue("y must be >= 0" in str(context.exception))

        #  Checks for using object's setters
        r = Rectangle(1, 2, 3, 4)

        with self.assertRaises(TypeError) as context:
            r.width = "w"
        self.assertTrue("width must be an integer" in str(context.exception))

        with self.assertRaises(ValueError) as context:
            r.width = 0
        self.assertTrue("width must be > 0" in str(context.exception))

        with self.assertRaises(ValueError) as context:
            r.width = -1
        self.assertTrue("width must be > 0" in str(context.exception))

        with self.assertRaises(TypeError) as context:
            r.height = "w"
        self.assertTrue("height must be an integer" in str(context.exception))

        with self.assertRaises(ValueError) as context:
            r.height = 0
        self.assertTrue("height must be > 0" in str(context.exception))

        with self.assertRaises(ValueError) as context:
            r.height = -6
        self.assertTrue("height must be > 0" in str(context.exception))

        with self.assertRaises(TypeError) as context:
            r.x = "w"
        self.assertTrue("x must be an integer" in str(context.exception))

        with self.assertRaises(ValueError) as context:
            r.x = -6
        self.assertTrue("x must be >= 0" in str(context.exception))

        with self.assertRaises(TypeError) as context:
            r.y = "w"
        self.assertTrue("y must be an integer" in str(context.exception))

        with self.assertRaises(ValueError) as context:
            r.y = -6
        self.assertTrue("y must be >= 0" in str(context.exception))


if __name__ == '__main__':
    unittest.main()
