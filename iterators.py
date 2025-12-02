"""
Zadanie 7.6 z zestawu 7
testy do zadania znajduja sie w pliku test_iterators.py
"""

import random

class ZeroOneIterator:
    """
    Iterator zwracajacy 0, 1, 0, 1, 0, 1, ...
    """

    def __iter__(self):
        self.state = 0
        return self

    def __next__(self):
        value = self.state
        self.state = 1 - self.state
        return value

class RandomDirection:
    """Iterator zwracajacy losowo jedna wartosc z ('N', 'E', 'S', 'W')."""

    def __iter__(self):
            return self

    def __next__(self):
            return random.choice(["N", "E", "S", "W"])

class WeekdayNumbers:
    """Iterator zwracajacy 0,1,2,3,4,5,6,0,1,..."""
    def __iter__(self):
        self.day = 0
        return self

    def __next__(self):
        value = self.day
        self.day = (self.day + 1) % 7
        return value
