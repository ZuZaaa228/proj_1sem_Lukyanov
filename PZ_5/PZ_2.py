# Описать функцию minmax(X, Y) записывающую в переменную X минимальное, а в переменную Y максимальное из значений
# Используя четыре вызова функции найти минимальное и максимальное из данных чисел A, B, C, D
def minmax(x: float, y: float):
    if x > y:
        x, y = y, x  # x и y меняются местами
        return x, y
    return x, y


A, B, C, D = input("Введите первое число: "), input("Введите второе число: "), input("Введите третье число: "), input(
    "Введите четвертое число: ")

while type(A) != float or type(B) != float or type(C) != float or type(D) != float:  # Обработчик исключений
    if type(A) != float:
        try:
            A = float(A)
        except ValueError:
            A = input("Введите целое число A без лишних символов: ")
    if type(B) != float:
        try:
            B = float(B)
        except ValueError:
            B = input("Введите целое число B без лишних символов: ")
    if type(C) != float:
        try:
            C = float(C)
        except ValueError:
            C = input("Введите целое число C без лишних символов: ")
    if type(D) != float:
        try:
            D = float(D)
        except ValueError:
            D = input("Введите целое число D без лишних символов: ")

A, B = minmax(A, B)  # Первый вызов функции
C, D = minmax(C, D)  # Второй вызов функции
A, C = minmax(A, C)  # Третий вызов функции
B, D = minmax(B, D)  # Четвертый вызов функции

print(f"Min: {A}\nMax: {D}")
