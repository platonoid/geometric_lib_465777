# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle: S = (a*h)/2

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
- Triangle: P = a + b + c

## Общее описание
- Содержит два файла circle.py и rectangle.py с функциями вычисления площади и периметра соответствующих геометрических фигур.

## Функции
# circle.py
- area() принимает число r - радиус окружности, возвращает квадрат этого числа, умноженный на pi.
'''
r = 6
print(area(r)) // 6 * 6 * pi
>> 113,09733552923255
'''
- perimeter() принимает число r - радиус окружности, возвращает это число, умноженное на 2 и на pi.
'''
r = 7
print(perimeter(r)) // 7 * 2 * pi
>> 43,98229715025710
'''
# square.py
- area() принимает число a - сторону квадрата, возвращает квадрат этого числа - площадь фигуры.
'''
a = 8
print(area(a)) // 8 * 8 
>> 64
'''
- perimeter() принимает число a - сторону квадрата, возвращает это число, умноженное на 4 - периметр фигуры.
'''
a = 8
print(perimeter(a)) // 8 * 4 
>> 32
'''
# rectangle.py
- area() принимает два числа a и b - две перпендикулярных стороны прямоугольника, возвращает их произведение - площадь фигуры.
'''
a = 3
b = 4
print(area(a, b)) // 3 * 4
>> 12
'''
- perimeter() принимает два числа a и b - две перпендикулярных стороны прямоугольника, возвращает их сумму, умноженную на 2 - периметр фигуры.
'''
a = 2
b = 4
print(perimeter(a, b)) // (2 + 4) * 2
>> 12
'''
# triangle.py
- area() принимает два числа a и h - основание и высота треугольника, возвращает их произведение, деленное на 2 - площадь фигуры.
'''
a = 6
h = 4
print(area(a, h)) // (6 * 4)/2
>> 12
'''
- perimeter() принимает три числа a, b и c - три стороны, возвращает их сумму - периметр фигуры.
'''
a = 6
b = 5
c = 5
print(perimeter(a, b, c)) // 6 + 5 + 5
>> 16
'''

## История изменения
[Fixed triangle.py](https://github.com/RadAnfisa/geometric_lib/commit/edec1093d29ecfaea750a78e980f2e93ea249d43)
[Added rectangle.py](https://github.com/RadAnfisa/geometric_lib/commit/00de5801f0b52bad9e462c824798063fe044ea40)
[L-03: Docs added](https://github.com/RadAnfisa/geometric_lib/commit/d078c8d9ee6155f3cb0e577d28d337b791de28e2)
[L-03: Circle and square added](https://github.com/RadAnfisa/geometric_lib/commit/8ba9aeb3cea847b63a91ac378a2a6db758682460)
