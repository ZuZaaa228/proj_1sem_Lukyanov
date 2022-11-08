# Дан список А размера N. Сформировать новый список B того же размера по следующему првилу:
# элемент Bк равен сумме элементов списка А с номерами от 1 до К.
def newlistfunc(first_list: list, second_list: list) -> list:  # Функция формирования списка по условию
    for K in range(len(first_list)):
        if K >= 1:  # Элемент списка с 0 индексом не будет включаться в сумму элементов
            second_list.append(sum(first_list[1:K + 1]))
        else:
            second_list.append(first_list[K])
    return second_list  # Возвращает уже наполненный список и сформированный список


def list_append(n: int, list_gen: list) -> list:  # Функция генерации списка
    for _ in range(n):
        list_gen.append(input(f"Введите {(_ + 1)}-е число: "))
        while type(list_gen[_]) != int:  # Обработчик исключений элементов списка
            try:
                list_gen[_] = int(list_gen[_])
            except ValueError:
                list_gen[_] = input(f"Введите целое число {_ + 1} без лишних символов: ")
    return list_gen


N, A, B = input("Введите длину списка: "), [], []

while type(N) != int:  # Обработчик исключений
    try:
        N = int(N)
    except ValueError:
        N = input("Введите целое число: ")

A = list_append(N, A)
print(newlistfunc(A, B))
