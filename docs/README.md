# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a

# Функций возвращающие значения,Math formulas

## Общее описание
- Данные функции вычисляют площадь и периметр для представленых выше фигур
- Для каждой фигуры свой файл,где содержатся функции вычисляющие
их площадь и периметр

### circle.py
``` python 
import math

   #вызывает библиотеку math

def area(r):
   '''принимает int(r) ,предполагаемый радиус окружности'''
  
    return math.pi * r * r
    '''возвращает значение площади int()'''
  
   
def perimeter(r):
    '''принимает int(r) ,предполагаемый радиус окружности'''
    return 2 * math.pi * r 
    '''возвращает значение периметра int()'''
```
### rectangle.py
``` python
   def area(a, b):
      '''принимает int(a) и int(b) = стороны прямоугольника'''
       return a * b
       '''возвращает значение площади int()'''
   def perimeter(a, b):
      '''принимает int(a) и int(b) = стороны прямоугольника'''
       return 2*(a + b)
       '''возвращает значение периметра int()'''
```
### square.py
``` python
   def area(a):
   '''принимает int(a)  =  сторона квадрата'''
      return a * a
      '''возвращает значение площади int()'''

   def perimeter(a):
   '''принимает int(a)  =  сторона квадрата'''
      return 4 * a
      '''возвращает значение периметра int()'''
```
### triangle.py
``` python
   def area(a, h):
   '''принимает int(a) и int(h) = сторона и высота треугольника'''
      return a * h / 2
      '''возвращает значение площади int()'''
      
   def perimeter(a, b, c):
   '''принимает int(a) и int(b) и int(c) = стороны треугольника'''
      return a + b + c
      '''возвращает значение периметра int()'''
```