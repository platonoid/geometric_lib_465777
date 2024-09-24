#Общее описание решения: 

Проект geometric_lib - это библиотека на языке Python, предназначенная для работы с геометрическими фигурами. Она предоставляет функциональность для вычисления периметра и площади различных фигур, таких как круг и квадрат.

Библиотека состоит из нескольких модулей, каждый из которых отвечает за определенную фигуру. Например, модуль circle содержит функции для вычисления периметра и площади круга, а модуль square - для квадрата. Каждый модуль экспортирует соответствующие функции, которые могут быть использованы другими частями программы.

# How to use calculator:

1. Run `python calculate.py`
2. Enter the figure name. Available are Circle, Square.
3. Enter the function: Area or Perimeter.
4. Enter figure sizes. Radius for circle, one side for square.
5. Get the answer!

# Math formulas

## Area


- Circle: `S = πR²`
- Rectangle: `S = ab`
- Square: `S = a²`
- Triangle: `S = sqrt(p * (p-a) * (p-b) * (p-c))` where p is semiperimeter

## Perimeter

- Circle: `P = 2πR`
- Rectangle: `P = 2a + 2b`
- Square: `P = 4a`
- Triangle: `P = a + b + c`

#Описание функций

##Circle:

**area:** возвращает площадь круга с заданным радиусом
входные данные: r=4
вывод: 50.26548245743669

**perimeter:** возвращает длину окружности с заданным радиусом
входные данные: 4
вывод: 25.132741228718345


##Square:

**area:** возвращает площадь квадрата с заданной стороной
входные данные: 4
вывод: 16

**perimeter:** возвращает периметр квадрата с заданной стороной
входные данные: 4
вывод: 16


##Triangle

**area** возвращает полупериметр треугольника с заданными сторонами
входные данные: 3, 4, 5
вывод: 6.0

**perimeter** возвращает периметр треугольника с заданными сторонами
входные данные: 3, 4, 5
вывод: 12


##Calculate

Ничего не выводит

 

#История изменения проекта с хешами коммитов

- _86edb1c3dd57fa9abc7ba2ec7052507938084727_  Add user agreement info
- _438b89a1dfc58d90e9036fe431771427965cd1ff_ Add user agreement
- _6adb96248a4d00d3bea13bd95d78ef52352cd1b_ Docs added
- _30494317cde4419be779c14306561e0eaa78b88b_ Add rectangle.py
- _b5b0fae727ca72c317c383b39c0af73d6adcd81c_ Update docs for calculate.py
- _d76db2ac7f69cc920ae2e6f669fb0671a7fa7d71_ Add calculate.py
- _51c40ebfd0e0b65f52fe5e54740cbb038e492db3_ Doc updated for triangle
- _d080c7888b81955bad2ed78d58ad910526b5132a_ Triangle added
- _d078c8d9ee6155f3cb0e577d28d337b791de28e2_  Docs added
- _8ba9aeb3cea847b63a91ac378a2a6db758682460_ Circle and square added

