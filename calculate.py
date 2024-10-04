import circle
import square

# Список доступных фигур
figs = ['circle', 'square']
# Список доступных функций для расчета
funcs = ['perimeter', 'area']
# Словарь для хранения размеров фигур
sizes = {}

def calc(fig, func, size):
    """
    Вычисляет и выводит результат для заданной фигуры и функции.

    Параметры:
    fig (str): название фигуры (например, 'circle' или 'square').
    func (str): название функции для расчета (например, 'perimeter' или 'area').
    size (list): список параметров фигуры (например, радиус для круга).

    Возвращаемое значение:
    None

    Пример вызова:
    calc('circle', 'area', [5])
    """
    assert fig in figs, "Некорректная фигура"
    assert func in funcs, "Некорректная функция"

    # Вычисление с использованием eval для вызова функции на основе имени фигуры и операции
    result = eval(f'{fig}.{func}(*{size})')
    print(f'{func} of {fig} is {result}')

if __name__ == "__main__":
    func = ''
    fig = ''
    size = list()
    
    # Запрос имени фигуры у пользователя
    while fig not in figs:
        fig = input(f"Enter figure name, available are {figs}:\n")
    
    # Запрос имени функции у пользователя
    while func not in funcs:
        func = input(f"Enter function name, available are {funcs}:\n")
    
    # Запрос параметров фигуры у пользователя
    while len(size) != sizes.get(f"{func}-{fig}", 1):
        size = list(map(int, input("Input figure sizes separated by space, 1 for circle and square\n").split(' ')))
    
    # Вызов функции для расчета и вывода результата
    calc(fig, func, size)
