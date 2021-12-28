import unittest

__import__('sys').path.insert(0, "../../")
Rectangle = __import__("models.rectangle").rectangle.Rectangle

"""
This unittest module test_rectangle tests the class Rectangle in 
models/rectangle
"""


class RectangleTest(unittest.TestCase):

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
        r1 = Rectangle(1, 2, 3, 4)
        self.assertEqual(1, r1.width)
        self.assertEqual(2, r1.height)
        self.assertEqual(3, r1.x)
        self.assertEqual(4, r1.y)


if __name__ == '__main__':
    unittest.main()
