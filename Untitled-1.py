from math import sqrt
import itertools

message = ('Добро пожаловать в самую лучшую программу для вычисления '
           'квадратного корня из заданного числа')
print(message)


def calculate_square_root(number):
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(number):
    """Проверяем что-то."""
    if number <= 0:
        return


square = calculate_square_root(25.5)
calc(25.5)
print(f'Мы вычислили квадратный корень из введённого вами числа.'
      f'Это будет: {square}')
