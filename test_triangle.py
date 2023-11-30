import unittest
from triangle import *

class TriangleTestCase(unittest.TestCase):
    
    def test_zero_area(self):
        
        res = area(0, 0)
        self.assertEqual(res, 0)

    def test_negative_area(self):
        
        self.assertRaises(ValueError, area, -10, -20)

    def test_float_area(self):
        
        res = area(228.228, 1337.1919)
        self.assertAlmostEqual(res, 152592.3164766, delta=0.1)

    def test_zero_perim(self):
        
        res = perimeter(0, 0, 0)
        self.assertEqual(res, 0)

    def test_negative_perimeter(self):
        
        self.assertRaises(ValueError, perimeter, -10, -20, -30)

    def test_float_perim(self):
        
        res = perimeter(228.228, 1919.1919, 777.1337)
        self.assertAlmostEqual(res, 2924.5536, delta=0.1)
