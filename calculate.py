import circle
import square


figs = ['circle', 'square']
funcs = ['perimeter', 'area']
sizes = {}

def calc(fig, func, size):
'''
		Заданная функция вычисляет значение для указанной фигуры, исходя из размера фигуры.

			Параметры:
				figs (str) - название фигуры должны быть 'circle' or 'square'
				funcs (str) - название функции должно быть 'perimeter' or 'area'
				size (list) - список размеров фигуры. Для круга - 1 значение (радиус). Для квадрата - 1 значение (сторона).
			Возвращаемое значение:
				(float) - Результат вычисления функции для указанной фигуры.
			
			  
'''
	assert fig in figs
	assert func in funcs

	result = eval(f'{fig}.{func}(*{size})')
	print(f'{func} of {fig} is {result}')

if __name__ == "__main__":
	func = ''
	fig = ''
	size = list()
    
	while fig not in figs:
		fig = input(f"Enter figure name, avaliable are {figs}:\n")
	
	while func not in funcs:
		func = input(f"Enter function name, avaliable are {funcs}:\n")
	
	while len(size) != sizes.get(f"{func}-{fig}", 1):
		size = list(map(int, input("Input figure sizes separated by space, 1 for circle and square\n").split(' ')))
	
	calc(fig, func, size)



