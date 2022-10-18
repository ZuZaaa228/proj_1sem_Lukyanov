hello_string = "Введите целое число без лишних символов и пробелов"
a, b, c = input(f"{hello_string} №1"), input(f"{hello_string} №2"), input(f"{hello_string} №3")

while type(a) != int:
    try:
        a = int(a)
    except ValueError:
        a = input("Введите первое верное целое значение без лишних символов")

while type(b) != int:
    try:
        b = int(b)
    except ValueError:
        b = input("Введите второе верное целое значение без лишних символов")

while type(c) != int:
    try:
        c = int(c)
    except ValueError:
        c = input("Введите третье верное целое значение без лишних символов")

if a == b == c:
    print("Высказывание истинно!")
else:
    print("Высказывание не истинно!")
