# Даны 4 числа, одно из которых отлично от других, определить порядковый номер числа отличного от других
one = input("Введите первое число: ")
two = input("Введите второе число: ")
three = input("Введите третье число: ")
four = input("Введите четвёртое число: ")

# Проверка числа на правильность ввода
while type(one) != int:
    try:
        one = int(one)
    except ValueError:
        one = input("Введите целое число №1 без лишних символов! \n Пример: 12 ")

# Проверка числа на правильность ввода
while type(two) != int:
    try:
        two = int(two)
    except ValueError:
        two = input("Введите целое число №2 без лишних символов! \n Пример: 12 ")

# Проверка числа на правильность ввода
while type(three) != int:
    try:
        three = int(three)
    except ValueError:
        three = input("Введите целое число №3 без лишних символов! \n Пример: 12 ")

# Проверка числа на правильность ввода
while type(four) != int:
    try:
        four = int(four)
    except ValueError:
        four = input("Введите целое число №4 без лишних символов! \n Пример: 12 ")

# Поиск чила отличного от дургих
if one != two == three == four:
    print(1)
elif two != one == three == four:
    print(2)
elif three != one == two == four:
    print(3)
elif four != one == two == three:
    print(4)
else:
    print("Ошибка! Введенные числа не соответсвую условию. Выход из программы. ")
