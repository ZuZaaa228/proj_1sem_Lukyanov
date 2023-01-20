punctuation_marks = ['.', '?', '!', '...', ',', ';', ':', '-', '—']


file1 = open('text18-30.txt', 'r', encoding="UTF-8")
file_text = file1.read()
count_marks = 0
for i in file_text:
    if i in punctuation_marks:
        count_marks += 1
print(f"Содержимое файла: \n{file_text}\nКоличество знаков препинания: {count_marks}")
file1.close()

file2 = open('text18-30-2.txt', 'w', encoding="UTF-8")

author = 'М. Ю. Лермонтов'
title = 'Бородино'

file2.write(file_text+f'\n\nАвтор: {author}\nНазвание произведения: {title}')

file2.close()
