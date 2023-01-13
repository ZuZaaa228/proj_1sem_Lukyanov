punctuation_marks = ['.', '?', '!', '...', ',', ';', ':', '-']


file1 = open('text18-30.txt', 'r', encoding="UTF-8")
file_text = file1.read()
count_marks = 0
for i in file_text:
    if i in punctuation_marks:
        count_marks += 1
print(f"Содержимое файла: \n{file_text}\nКоличество знаков препинания: {count_marks}")
file1.close()

file2 = open('text18-30.txt', 'a')

# file2.write("f")

file2.close()