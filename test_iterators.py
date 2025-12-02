import unittest
from iterators import ZeroOneIterator, RandomDirection, WeekdayNumbers

class TestIterators(unittest.TestCase):

    def test_zero_one_iterator(self):
        it = iter(ZeroOneIterator())
        result = [next(it) for _ in range(6)]
        self.assertEqual(result, [0, 1, 0, 1, 0, 1])

    def test_random_direction(self):
        it = iter(RandomDirection())
        for _ in range(12):
            value = next(it)
            self.assertIn(value, ["N", "E", "S", "W"])

    def test_weekday_numbers(self):
        it = iter(WeekdayNumbers())
        result = [next(it) for _ in range(12)]
        self.assertEqual(result, [0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4])

if __name__ == "__main__":
    unittest.main()