# Импортируем модуль для работы с кругами
import circle
# Импортируем модуль для работы с квадратами
import square

# Список доступных фигур
figs = ['circle', 'square']
# Список доступных функций
funcs = ['perimeter', 'area']
# Словарь для хранения размеров
sizes = {}


#Эта функция вычисляет значение заданной функции для замкнутой фигуры.
#Аргументы:
    #fig (str): Название фигуры ('circle' или 'square').
    #func (str): Название функции ('perimeter' или 'area').
    #size (list): Список размеров фигуры.
#Возвращает:
    #None: Результат выводится на экран.

  #Пример:
   #>>> calc('circle', 'area', [5])
   #area of circle is 78.53975 # (площадь круга с радиусом 5)
def calc(fig, func, size):
# Проверяем, что фигура доступна в списке
	assert fig in figs
 # Проверяем, что функция доступна в списке
    assert func in funcs

# Вызываем функцию на выбранной фигуре с указанными размерами
	result = eval(f'{fig}.{func}(*{size})')
 # Выводим результат
	print(f'{func} of {fig} is {result}')

# Проверяем, что программа выполняется напрямую
if __name__ == "__main__":
	func = ''
	fig = ''
	size = list()
# Цикл для выбора доступной фигуры
	while fig not in figs:
		fig = input(f"Enter figure name, avaliable are {figs}:\n")
# Цикл для выбора доступной функции
	while func not in funcs:
		func = input(f"Enter function name, avaliable are {funcs}:\n")

# Проверка правильного количества размеров
	while len(size) != sizes.get(f"{func}-{fig}", 1):
		size = list(map(int, input("Input figure sizes separated by space, 1 for circle and square\n").split(' ')))

# Вызываем функцию для вычислений
	calc(fig, func, size)



