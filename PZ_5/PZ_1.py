def f(lst: list) -> int:
    return sum(lst)  # Сложение всех чисел из списка с числовым рядом


lst = input("Введите числовой ряд.\nПример: 12 747 6236 \n").split()  # Создание списка с числовым рядом

for index in range(len(lst)):
    lst[index] = int(lst[index])  # форматирование каждлого элемента списка

print(f(lst)) # Результат вызова функции
