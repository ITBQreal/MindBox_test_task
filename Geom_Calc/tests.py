import unittest
from calculator import Circle, Triange

class TestShapeCalculator(unittest.TestCase):
    def test_circle_area(self):
        self.assertAlmostEqual(Circle.area(5), 78.539816, places=5)

    def test_triangle_area(self):
        self.assertAlmostEqual(Triange.area(3, 4, 5), 6.0)

    def test_right_triangle_check(self):
        self.assertTrue(Triange.right_triangle_check(3, 4, 5))
        self.assertFalse(Triange.right_triangle_check(3, 4, 6))

if __name__ == "__main__":
    unittest.main()