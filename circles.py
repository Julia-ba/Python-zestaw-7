"""
Zadanie 7.5 z zestawu 7
testy do zadania znajduja sie w pliku test_circles.py
"""

from math import pi, sqrt
from points import Point

class Circle:
    """
    Klasa reprezentujaca okregi na plaszczyznie.
    """

    def __init__(self, x, y, radius):
        if radius < 0:
            raise ValueError("Promien nie moze byc ujemny.")
        self.pt = Point(x, y)
        self.radius = radius

    def __repr__(self):
        """
        Zwraca string 'Circle(x, y, radius)'.
        """
        return f"Circle({self.pt.x}, {self.pt.y}, {self.radius})"

    def __eq__(self, other):
        """
        Zwraca True, jesli okregi maja ten sam srodek i promien.
        """
        return self.pt == other.pt and self.radius == other.radius

    def __ne__(self, other):
        """
        Zwraca True, jesli okregi są rozne.
        """
        return not self == other

    def area(self):
        """
        Zwraca pole powierzchni okregu.
        """
        return pi * self.radius ** 2

    def move(self, x, y):
        """
        Zwraca nowy okrag przesuniety o (x, y).
        """
        return Circle(self.pt.x + x, self.pt.y + y, self.radius)

    def cover(self, other):
        """
        Zwraca najmniejszy okrag pokrywajacy oba okregi.
        """
        d = sqrt((self.pt.x - other.pt.x) ** 2 + (self.pt.y - other.pt.y) ** 2)

        if self.radius >= d + other.radius:
            return Circle(self.pt.x, self.pt.y, self.radius)
        if other.radius >= d + self.radius:
            return Circle(other.pt.x, other.pt.y, other.radius)

        new_radius = (d + self.radius + other.radius) / 2

        r = (new_radius - self.radius) / d
        new_x = self.pt.x + r * (other.pt.x - self.pt.x)
        new_y = self.pt.y + r * (other.pt.y - self.pt.y)

        return Circle(new_x, new_y, new_radius)

