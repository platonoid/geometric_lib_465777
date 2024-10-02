# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle: S = ah/2

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
- Triangle: P = a + b + c

# Как работает мой проект
Проект состоит из 4 файлов [circle.py](/circle.py), [rectangle.py](/rectangle.py), [square.py](/square.py) и [triangle.py](/triangle.py). С помощью параметров, таких как радиус, длины сторон или высоты, считаются периметр и площадь для окружности, прямоугольника, квадрата и треугольника.
# About ***[circle.py](/circle.py)***
``` Python
import math

def area(r):
    return math.pi * r * r
''' 
Функция получает на вход радиус и возвращает площадь окружности.

            Праметры:
                r (int): радиус окружности
            
            Возвращаемое значение:
                area (int): площадь окружности
'''
def perimeter(r):
    return 2 * math.pi * r
'''
Функция получает на вход радиус и возвращает периметр окружности.

            Праметры:
                r (int): радиус окружности
            
            Возвращаемое значение:
                perimeter (int): периметр окружности
'''
```
## Примеры запуска
```
r = 5
area(5) = 78,53981...
perimeter(5) = 31,41592...
```
# About [rectangle.py](/rectangle.py)
``` Python
def area(a, b):
    return a * b
'''
Функция получает на вход стороны прямоугольника и возвращает его площадь.

            Праметры:
                a (int): ширина прямоугольника
                b (int): длина прямоугольника
            
            Возвращаемое значение:
                area (int): площадь прямоугольника
'''

def perimetr(a, b):
    return 2 * (a + b)
'''
Функция получает на вход стороны прямоугольника и возвращает его периметр.

            Праметры:
                a (int): ширина прямоугольника
                b (int): длина прямоугольника
            
            Возвращаемое значение:
                perimetr (int): периметр прямоугольника
'''
```
## Примеры запуска
```
a = 5
b = 10
area(5, 10) = 50
perimeter(5, 10) = 30
```

# About [square.py](/square.py)
``` Python
def area(a):
    return a * a
'''
Функция получает на вход сторону квадрата и возвращает его площадь.

            Праметры:
                a (int): сторона квадрата
            
            Возвращаемое значение:
                area (int): площадь квадрата
'''

def perimeter(a):
    return 4 * a
'''
Функция получает на вход сторону квадрата и возвращает его периметр.

            Праметры:
                a (int): сторона квадрата
            
            Возвращаемое значение:
                perimetr (int): периметр квадрата
'''
```
## Примеры запуска
```
a = 5
area(5) = 25
perimeter(5) = 20
```

# About [triangle.py](/triangle.py)
``` Python
def area(a, h):
    return a * h / 2
'''
Функция получает на вход сторону треугольника и высоту, которая опирается на эту сторону, и возвращает его площадь.

            Праметры:
                a (int): сторона треугольника
                h (int): его высота
            
            Возвращаемое значение:
                area (int): площадь треугольника
'''

def perimetr(a, b, c):
    return a + b + c
'''
Функция получает на вход стороны треугольника и возвращает его периметр.

            Праметры:
                a (int): сторона треугольника
                b (int): сторона треугольника
                c (int): сторона треугольника
            
            Возвращаемое значение:
                perimetr (int): периметр треугольника
'''
```
## Примеры запуска
```
a = 5
b = 6
c = 7
h = 8
area(5, 8) = 20
perimeter(5, 6, 7) = 18
```

# Project History
```
a6a7800 (HEAD -> new_features_467343) исправил ошибку
ade03c6 добавил новый файл
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