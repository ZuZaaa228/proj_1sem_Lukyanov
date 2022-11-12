# Дан целочисленный список размера N. Увеличит все четные числа содержащиеся в списке, на исходное значение
# первого четного числа. Если четные числа в списке отсутвуют, то оставить список без изменений
def list_append(n: int, list_gen: list) -> list:  # Функция генерации списка
    for _ in range(n):
        list_gen.append(input(f"Введите {(_ + 1)}-е число: "))
        while type(list_gen[_]) != int:  # Обработчик исключений элементов списка
            try:
                list_gen[_] = int(list_gen[_])
            except ValueError:
                list_gen[_] = input(f"Введите целое число {_ + 1} без лишних символов: ")
    return list_gen


def first_even_element(default_list: list) -> int:  # Функция находящая первый четный элемент
    for _ in default_list:
        if _ % 2 == 0:
            first = _
            return first


def count_addiction(default_list: list, first_even_el: int or None) -> list:
    # Функция которая увеличивает четные числа на первое четное число из списка
    if first_even_el is None:
        return default_list
    for i in range(len(default_list)):
        if default_list[i] % 2 == 0:
            default_list[i] += first_even
    return default_list


N, lst = input("Введите длину списка: "), []

while type(N) != int:  # Обработчик исключений
    try:
        N = int(N)
    except ValueError:
        N = input("Введите целое число: ")

lst = list_append(N, lst)  # Создание списка
first_even = first_even_element(lst)  # Присваивание функции
print(count_addiction(lst, first_even))  # Вывод результата