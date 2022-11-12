# Дан список размера N и целое число размера K (1 < K < N) осуществить сдвиг элементов списка вправо на K
# позиций (при этом A1 перейдет в Ак+1, A2 - в Ак+2, …An-k - в An, а исходное значение К последних элементов
# будет потеряно). Первые К элементов полученного списка положить равными 0.
def list_append(n: int, list_gen: list) -> list:  # Функция генерации списка
    for _ in range(n):
        list_gen.append(input(f"Введите {(_ + 1)}-е число: "))
        while type(list_gen[_]) != int:  # Обработчик исключений элементов списка
            try:
                list_gen[_] = int(list_gen[_])
            except ValueError:
                list_gen[_] = input(f"Введите целое число {_ + 1} без лишних символов: ")
    return list_gen


def offset_elements(n: int, k: int, lst: list) -> list:  # Функция смещающая элементы в право на К позиций
    for i in range(n - 1, k - 1, -1):
        lst[i] = lst[i - k]
    for i in range(0, k):  # Первые К элементов будет потеряны и на их место встанет '0'
        lst[i] = 0
    return lst


N, K = input("Введите размер списка: "), input(
    "Введите число K, которое меньше длины списка, но больше 1: ")

while type(N) != int or type(K) != int:  # Обработчик исключений
    try:
        N, K = int(N), int(K)
        if K >= N or 1 >= K:
            raise AttributeError  # Если число К не входит в диапазон, то будет вызвано исключение
        break
    except ValueError:
        if type(N) != int:
            N = input("Введите целое число длины списка без лишних символов: ")
        if type(K) != int:
            K = input("Введите число K без лишнних символов, которое меньше длины списка, но больше 1: ")
    except AttributeError:
        K = input("Введите целое число К без лишних символов в диапазоне от 1 до Длины списка (1 < K < N): ")

gen_list = list_append(N, [])  # Создание листа с нужным размером

print(f"Результат: {offset_elements(N, K, gen_list)}")  # Вывод списка
