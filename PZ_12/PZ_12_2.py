# 2.Составить генератор (yield), который преобразует все буквенные символы в
# заглавные.
def my_gen(string: str):  # Объявление функции
    for symb in string:
        yield symb.upper()  # Изменения символов


g = my_gen('qwErtTyui')
print(''.join(g))  # Запись в строку
