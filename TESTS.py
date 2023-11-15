import unittest
import math
import circle
import rectangle
import square
import triangle

class CIRCLETEST(unittest.TestCase):
    def test_int(self):
        n = int(input("введите число для вычисления круга(целое и неотрицательное):"))
        if(n >= 0 and n < 10**9):
            x = True
        else:
            x = False
        self.assertTrue(x)
    def test_c_area_const(self):
        result = circle.area(5)
        self.assertEqual(result, 78.53981633974483)

    def test_c_perimeter_const(self):
        result2 = circle.perimeter(5)
        self.assertEqual(result2, 31.41592653589793)

class RECTANGLETEST(unittest.TestCase):
    def test_int1(self):
        n = int(input("введите число для вычисления прямоугольника(целое и неотрицательное):"))
        n1 = int(input("введите число для вычисления прямоугольника(целое и неотрицательное):"))
        if ((n1 >= 0 and n1 < 10 ** 9) and (n >= 0 and n < 10 ** 9)):
            x = True
        else:
            x = False
        self.assertTrue(x)
    def test_r_area_const(self):
        result = rectangle.area(10, 2)
        self.assertEqual(result, 20)

    def test_r_perimeter_const(self):
        result = rectangle.perimeter(10, 2)
        self.assertEqual(result, 24)


class SQUARETEST(unittest.TestCase):
    def test_int(self):
        n = int(input("введите число для вычисления квадрата(целое и неотрицательное):"))
        if (n >= 0 and n < 10 ** 9):
            x = True
        else:
            x = False
        self.assertTrue(x)

    def test_s_area(self):
        result = square.area(4)
        self.assertEqual(result, 16)

    def test_s_perimeter(self):
        result = square.area(4)
        self.assertEqual(result, 16)

class TRIANGLETEST(unittest.TestCase):
    def test_int2(self):
        n = int(input("введите число для вычисления треугольника(целое и неотрицательное):"))
        n1 = int(input("введите число для вычисления треугольника(целое и неотрицательное):"))
        n2 = int(input("введите число для вычисления треугольника(целое и неотрицательное):"))
        if ((n1 >= 0 and n1 < 10 ** 9) and (n >= 0 and n < 10 ** 9) and ((n2 >= 0 and n2 < 10 ** 9))):
            x = True
        else:
            x = False
        self.assertTrue(x)
    def test_t_area(self):
        result = triangle.area(2, 3)
        self.assertEqual(result, 3)

    def test_t_peremiter(self):
        result = triangle.perimeter(10, 10, 10)
        self.assertEqual(result, 30)


if __name__ == '__main__':
    unittest.main()
