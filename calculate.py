import circle
import square

'''Список доступных фигур'''
figs = ['circle', 'square']
'''Список доступных функций для расчета'''
funcs = ['perimeter', 'area']
'''Словарь для хранения размеров фигур'''
sizes = {}


def calc(fig, func, size):
    ''' Проверка, что фигура и функция находятся в допустимых списках '''
    assert fig in figs
    assert func in funcs

    ''' Выполняем расчет с помощью eval и выводим результат '''
    result = eval(f'{fig}.{func}(*{size})')
    print(f'{func} of {fig} is {result}')


if __name__ == "__main__":
    ''' Инициализация переменных для функции, фигуры и размеров '''
    func = ''
    fig = ''
    size = list()

    ''' Цикл для выбора фигуры, пока не будет введено допустимое значение '''
    while fig not in figs:
        fig = input(f"Enter figure name, available are {figs}:\n")

    ''' Цикл для выбора функции, пока не будет введено допустимое значение '''
    while func not in funcs:
        func = input(f"Enter function name, available are {funcs}:\n")

    ''' Цикл для ввода размеров фигуры, пока не будет введено корректное количество значений '''
    while len(size) != sizes.get(f"{func}-{fig}", 1):
        size = list(map(int, input("Input figure sizes separated by space, 1 for circle and square\n").split(' ')))

    ''' Вызов функции для выполнения расчета '''
    calc(fig, func, size)
