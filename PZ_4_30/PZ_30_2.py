N = input("Введите число")

while type(N) != int:  # Обработка исключений
    try:
        N = int(N)
    except ValueError:
        N = input("Введите число еще раз!: ")

if N % 10 == 2:  # Проверка
    print(True)  #Вывод True
else:
    print(False)  #Вывод False