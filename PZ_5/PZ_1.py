# Составить функцию, которая выполнит сумирование числового ряда
def funcion_sum(numerical_series: list) -> int:
    return sum(numerical_series)  # Сложение всех чисел из списка с числовым рядом


numerical_series = input("Введите числовой ряд.\nПример: 12 747 6236 \n").split()  # Создание списка с числовым рядом

index = 0  # id элемента в списке
while index < len(numerical_series):  # Обработчик исключений
    while type(numerical_series[index]) != int:
        try:
            numerical_series[index] = int(numerical_series[index])
        except ValueError:
            numerical_series[index] = input("Введите целое число без лишних символов: ")
    index += 1

print(funcion_sum(numerical_series))  # Результат вызова функции
