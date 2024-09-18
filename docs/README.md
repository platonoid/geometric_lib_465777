# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle: S = ah/2

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2(a + b)
- Square: P = 4a
- Triangle: P = a + b + c

> ***Поскольку ветка с программами rectangle и triangle была удалена, то я восстановил эту ветку (и, соответственно, коммиты в ней) с помощью*** ```git checkout -b <имя удалённой ветки> <хэш удаления>```

# How the program works
The program includes 4 files: [circle.py](/circle.py), [rectangle.py](/rectangle.py), [square.py](/square.py) and [triangle.py](/triangle.py). Each of them, when entering a parameter of the corresponding shape (side length or radius), calculates and outputs the area and perimeter of this shape using mathematical formulas.

> *All further formulas used to calculate the area and perimeter can be found in ***Math formulas***.*

## About ***[circle.py](/circle.py)***
```ruby
import math


def area(r):
    return math.pi * r * r
'''According to the given radius of the circle outputs its area.
        Parameters: 
            r(int or float) - radius of the circle;
            pi - math constant;
        Return value:
            area(r) - area of a circle with this radius. 
'''

def perimeter(r):
    return 2 * math.pi * r
'''According to the given radius of the circle outputs its perimeter.
        Parameters: 
            r(int or float) - radius of the circle;
            pi - math constant;
        Return value:
            perimeter(r) - perimeter of a circle with this radius. 
'''
```
***Launch example:***
```ruby
Radius of the circle: 4
Area: 50.26548245743669 
Perimeter: 25.132741228718345
```
## About ***[rectangle.py](/rectangle.py)***
```ruby
def area(a, b): 
    return a * b 
'''According to the given lengths of the sides of the rectangle outputs its area.
        Parameters: 
            a(int or float) - the length of the one side of the rectangle;
            b(int or float) - the length of the second side of the rectangle;
        Return value: 
            area(a, b) - area of a rectangle with this sides. 
'''

def perimeter(a, b): 
    return (a + b) * 2 
'''According to the given lengths of the sides of the rectangle outputs its perimeter.
        Parameters: 
            a(int or float) - the length of the one side of the rectangle;
            b(int or float) - the length of the second side of the rectangle;
        Return value: 
            perimeter(a, b) - perimeter of a rectangle with this sides. 
'''
```
***Launch example:***
```ruby
First side of the rectangle: 4
Second side of the rectangle: 9
Area: 36
Perimeter: 26
```
## About ***[square.py](/square.py)***
> *Note that a **square** is a special case of a **rectangle**, that is, to calculate the area and perimeter of a **square**, you can use and **rectangle.py** (a and b will be equal)*
```ruby
def area(a):
    return a * a

'''According to the given lengths of the side of the square outputs its area.
        Parameters: 
            a(int or float) - the length of the side of the square;
        Return value: 
            area(a) - area of a square with this side. 
'''
def perimeter(a):
    return 4 * a
'''According to the given lengths of the side of the square outputs its perimeter.
        Parameters: 
            a(int or float) - the length of the side of the square;
        Return value: 
            perimeter(a) - perimeter of a square with this side. 
'''
```
***Launch example:***
```ruby
Side of the square: 7
Area: 49
Perimeter: 28
```
## About ***[triangle.py](/triangle.py)***
```ruby
def area(a, h): 
    return a * h / 2 
'''According to the given lengths of the sides of the triangle outputs its area.
        Parameters: 
            a(int or float) - the length of the one side of the triangle;
            h(int or float) - the length of the height drawn to this side;
        Return value: 
            area(a, h) - area of a triangle with this sides. 
'''
def perimeter(a, b, c): 
    return a + b + c 
'''According to the given lengths of the sides of the triangle outputs its perimeter.
        Parameters: 
            a(int or float) - the length of the one side of the triangle;
            b(int or float) - the length of the second side of the triangle;
            c(int or float) - the length of the third side of the triangle;
        Return value: 
            perimeter(a, b, c) - perimeter of a triangle with this sides. 
'''
```

> *In fact, it is not necessary to know the **height** of the triangle, three of its sides will be enough to calculate the area (according to **[Heron's formula](https://en.wikipedia.org/wiki/Heron%27s_formula)**)*

***Launch example:***
```ruby
First side of the triangle: 4
Second side of the triangle: 5
Third side of the triangle: 6
Height drawn to first side: 4.9607837082461075
Area: 9.921567416492215
Perimeter: 15
```

# Project modification history with commit hashes (except the last commit about this documentary)
```
86edb1c (origin/release) L-05: Update Docs. Add user agreement info
438b89a L-05: Add user agreement
6adb962 L-03: Docs added
3049431 (origin/feature) L-04: Add rectangle.py
b5b0fae (origin/develop) L-04: Update docs for calculate.py
d76db2a L-04: Add calculate.py
51c40eb L-04: Doc updated for triangle
d080c78 L-04: Triangle added
d078c8d (origin/main, origin/HEAD, main) L-03: Docs added
8ba9aeb L-03: Circle and square added
```