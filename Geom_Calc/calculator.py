import abc
import math
from abc import ABC


# Я создал абстракный класс чтобы можно было с лёгкостью добавить новую фигуры не нарушая OCP
class Shape(ABC):
    @staticmethod
    @abc.abstractmethod
    def area(*sides):
        pass


class Circle(Shape):
    @staticmethod
    def area(radius):
        if radius <= 0:
            raise ValueError("Радиус должен быть положительным числом")
        return math.pi * radius ** 2


class Triange(Shape):
    @staticmethod
    def right_triangle_check(side1, side2, side3):
        sides = [side1, side2, side3]
        hypotenuse = max(sides)
        sides.remove(hypotenuse)
        return hypotenuse ** 2 == sides[0] ** 2 + sides[1] ** 2

    @staticmethod
    def area(side1, side2, side3):
        if any(side <= 0 for side in [side1, side2, side3]):
            raise ValueError("Длины сторон должны быть положительными числами")
        s = (side1 + side2 + side3) / 2
        return math.sqrt(s * (s - side1) * (s - side2) * (s - side3))


# Немного не понял задания "Вычисление площади фигуры без знания типа фигуры в compile-time"
# Если неизвестная фигура это одна из тех которые мы реализовали, то данный код будет верен.
def calculate_unknown_figure_type(*sides):
    if len(sides)==3:
        return Triange.area(sides[0], sides[1], sides[2])
    if len(sides) == 1:
        return Circle.area()