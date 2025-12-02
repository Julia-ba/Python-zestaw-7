import unittest
from math import pi, sqrt
from circles import Circle
from points import Point

class TestCircles(unittest.TestCase):

    def setUp(self):
        self.c1 = Circle(1, 2, 4)
        self.c2 = Circle(3, 0, 3)

    def test_repr_and_equality(self):
        self.assertEqual(repr(self.c1), "Circle(1, 2, 4)")
        self.assertTrue(self.c1 == Circle(1, 2, 4))
        self.assertFalse(self.c1 == self.c2)

    def test_area(self):
        self.assertAlmostEqual(self.c1.area(), pi * 16)
        self.assertAlmostEqual(Circle(0, 0, 0).area(), 0)

    def test_move(self ):
        moved = self.c1.move(1, 5)
        self.assertEqual(moved.pt, Point(2, 7))
        self.assertEqual(moved.radius, 4)

    def test_cover_non_overlapping(self):
        result = self.c1.cover(self.c2)
        d = sqrt((self.c1.pt.x - self.c2.pt.x) ** 2 + (self.c1.pt.y - self.c2.pt.y) ** 2)
        exp_radius = (d + self.c1.radius + self.c2.radius) / 2
        self.assertAlmostEqual(result.radius, exp_radius, places=6)

    def test_cover_contained(self):
        c_big = Circle(0, 0, 5)
        c_small = Circle(1, 1, 1)
        result = c_big.cover(c_small)
        self.assertEqual(result, c_big)

    def test_invalid_radius(self):
        with self.assertRaises(ValueError):
            Circle(0, 0, -3)


if __name__ == "__main__":
    unittest.main()