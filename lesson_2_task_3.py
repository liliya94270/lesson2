from math import ceil

def square(a):
    return ceil(a ** 2)

a = float(input("Длина стороны квадрата: "))
print(f'Округленная в большую сторону площадь - {square(a)}')
