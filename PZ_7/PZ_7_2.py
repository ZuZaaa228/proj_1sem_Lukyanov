# Дана строка, состоящая из русских слов, набранных заглавными буквами и разделенных пробелами (Одним или несколькими)
# Найти количество слов, которые начинаются и заканчиваются одной и той же буквой.
String = input("Введите строку, состаящую из русских слов заглавными буквами: ").upper()
if "  " in String:
    while "  " in String:
        String = String.replace("  ", " ")

String = String.split(" ")
count = 0  # Счетчик слов начинающихся с одной и той же буквы
for i in String:  # Цикл проходит по списку и смотрит на первый и последних символ
    if i[0] == i[-1]:
        count += 1
print(f"Количество слов, которые начинаются с одной и той же буквы: {count}")
