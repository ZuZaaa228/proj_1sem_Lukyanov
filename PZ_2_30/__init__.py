# 0 - воскресенье, 1 - понедельник, ... 6 - суббота
K = input("Введите число от 1 до 365: ")

while type(K) != int:  # Проверка корректности ввода числа
    try:
        K = int(K)

    except ValueError:
        K = input("Введите число без лишних знаков: ")

while (0 >= K) or (K > 365):  # Проверка корректности ввода диапазона
    try:
        K = int(input("Введите цифру от 1 до 365!: "))

    except:
        while type(K) != int:
            K = input("Введите число от 1 до 365 без лишних знаков!!: ")

first_day_month = 4
num = K % 7
result = (((first_day_month - 1) + num) % 7)

print(result)