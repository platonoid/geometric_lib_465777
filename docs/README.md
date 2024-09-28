
# How to use calculator:
1. Run `python calculate.py`
2. Enter the figure name. Available are Circle, Square.
3. Enter the function: Area or Perimeter.
4. Enter figure sizes. Radius for circle, one side for square.
5. Get the answer!

# Math formulas
## Area
- Circle: `S = πR²`
	def area(r):
	"""Вычисляет площадь окружности по числу пи и квадарту радиуса
	
	Параметры:
	r(int, float): радиус окружности

	Возвращает: 
	float: площадь окружности
	
	Пример использования:
	>>> area(4)
	50.24
	"""
	return math.pi * r * r
- Rectangle: `S = ab`
	def area(a, b):
	"""Вычисляет площадь прямоугольника по двум сторонам

	Параметры:
	a(int, float): первое десятичное число
	b(int, float): второе десятичное число

	Возвращает:
	int, float: Площадь прямоугольника

	Пример использования:
	>>> area(3, 4):
	12
	"""
- Square: `S = a²`
- Triangle: `S = sqrt(p * (p-a) * (p-b) * (p-c))` where p is semiperimeter

## Perimeter
- Circle: `P = 2πR`
- Rectangle: `P = 2a + 2b`
- Square: `P = 4a`
- Triangle: `P = a + b + c`

