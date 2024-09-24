# Общее описание проекта geometric_lib

Проект geometric_lib представляет собой библиотеку, предназначенную для выполнения математических расчетов, связанных с геометрическими фигурами, такими как круги и квадраты. Библиотека включает в себя функции для вычисления площади и периметра данных фигур, используя стандартные математические формулы. Также есть встроенный калькулятор.

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

# Описание функций

## Функция `calc`

Функция вычисляет значение указанной функции(площадь, периметр...) для заданной фигуры(круг, квадрат...).

### Пример использования:

------------------------------

## Функция `area`

Функция считает площадь круга.

### Пример использования:

>>> area(5)
78.539816

## Функция `perimeter`

Функция считает периметр круга.

### Пример использования:

>>> perimeter(5)
31.41592653589793

## Функция `area`

Функция считает площадь квадрата(возвращает квадрат числа).

### Пример использования:

>>> area(2)
4

## Функция `perimeter`

Вычисляет периметр квадрата.

### Пример использования:

>>> area(5)
20

## Функция `area`

Функция считает полупериметр треугольника.

### Пример использования:

>>> area(3, 4, 5)
6.0

## Функция `perimeter`

Функция считает периметр треугольника.

### Пример использования:

>>> area(3, 4, 5)
12

# История изменений

- b5b0fae727ca72c317c383b39c0af73d6adcd81c: Update docs for calculate.py
- d76db2ac7f69cc920ae2e6f669fb0671a7fa7d71: Add calculate.py
- 51c40ebfd0e0b65f52fe5e54740cbb038e492db3: Doc updated for triangle
- d080c7888b81955bad2ed78d58ad910526b5132a: Triangle added
- d078c8d9ee6155f3cb0e577d28d337b791de28e2: Docs added
- 8ba9aeb3cea847b63a91ac378a2a6db758682460: Circle and square added
