import math


def area(r):
''' Находит площадь окружности
    Параметры:
        r (double): радиус окружности
    Возвращаемые значения:
        circle_area (double): площадь окружности
'''
    return math.pi * r * r


def perimeter(r):
''' Находит периметр окружности
 Параметры:
    r (double): радиус окружности
 Возвращаемые значения:
    circle_perimeter (double): периметр окружности
'''
    return 2 * math.pi * r

