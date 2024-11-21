import unittest
from rectangle import rectangle_area
from rectangle import rectangle_perimeter
from square import square_area
from square import square_perimeter
from triangle import triangle_area
from triangle import triangle_perimeter

class MathTest(unittest.TestCase):
    def test_rectangle_area1(self):
        first = 10
        second = 2
        result = rectangle_area(first, second)
        self.assertEqual(result, 20) 

    def test_rectangle_area2(self):
        first = 3
        second = 1
        result = rectangle_area(first, second)
        self.assertEqual(result, 3) 

    def test_rectangle_area3(self):
        first = 0
        second = 0
        with self.assertRaises(ValueError):
            rectangle_area(first, second)
    
    def test_rectangle_area4(self):
        first = 1
        second = 1
        result = rectangle_area(first, second)
        self.assertEqual(result, 1) 

    def test_rectangle_perimetr1(self):
        first = 10
        second = 2
        result = rectangle_perimeter(first, second)
        self.assertEqual(result, 24) 

    def test_rectangle_perimetr2(self):
        first = 3
        second = 1
        result = rectangle_perimeter(first, second)
        self.assertEqual(result, 8) 

    def test_rectangle_perimetr3(self):
        first = 0
        second = 0
        with self.assertRaises(ValueError):
            rectangle_perimeter(first, second)
    
    def test_rectangle_perimetr4(self):
        first = 1
        second = 1
        result = rectangle_perimeter(first, second)
        self.assertEqual(result, 4) 

    def test_square_area1(self):
        a = 10
        result = square_area(a)
        self.assertEqual(result, 100) 

    def test_square_area2(self):
        a = 13
        result = square_area(a)
        self.assertEqual(result, 169) 

    def test_square_area3(self):
        a = 0
        with self.assertRaises(ValueError):
            square_area(a)
    
    def test_square_area4(self):
        a = 1
        result = square_area(a)
        self.assertEqual(result, 1) 

    def test_square_perimetr1(self):
        a = 10
        result = square_perimeter(a)
        self.assertEqual(result, 40) 

    def test_square_perimetr2(self):
        a = 1
        result = square_perimeter(a)
        self.assertEqual(result, 4) 

    def test_square_perimetr3(self):
        a = 0
        with self.assertRaises(ValueError):
            square_perimeter(a)
    
    def test_square_perimetr4(self):
        a = 4
        result = square_perimeter(a)
        self.assertEqual(result, 16) 

    def test_triangle_area1(self):
        a = 10
        h = 1
        result = triangle_area(a, h)
        self.assertEqual(result, 5) 

    def test_triangle_area2(self):
        a = 13
        h = 2
        result = triangle_area(a, h)
        self.assertEqual(result, 13) 

    def test_triangle_area3(self):
        a = 0
        h = 0
        with self.assertRaises(ValueError):
            triangle_area(a, h)
    
    def test_triangle_area4(self):
        a = 1
        h = 4
        result = triangle_area(a, h)
        self.assertEqual(result, 2) 

    def test_triangle_perimetr1(self):
        a = 10
        b = 10
        c = 10
        result = triangle_perimeter(a, b, c)
        self.assertEqual(result, 30) 

    def test_triangle_perimetr2(self):
        a = 1
        b = 2
        c = 3
        result = triangle_perimeter(a, b, c)
        self.assertEqual(result, 6)

    def test_triangle_perimetr3(self):
        a = 0
        b = 0
        c = 0
        with self.assertRaises(ValueError):
            triangle_perimeter(a, b, c)
    
    def test_triangle_perimetr4(self):
        a = 1
        b = 1
        c = 1
        result = triangle_perimeter(a, b, c) 
        self.assertEqual(result, 3)