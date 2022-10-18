N = input("Введите положительное натуральное число: ")
while type(N) != int:
    try:
        N = int(N)
    except ValueError:
        N = input("Ошибка ввода! \n Введите целое положительное число без лишних символов \n Пример: 10 ")

S = 0.0
i = 1

while N:
    x = round((1 + i * 0.1) * (-1) ** (i + 1), 1)
    S = round((S + x), 1)
    i += 1
    N -= 1
N = S

print(N)
