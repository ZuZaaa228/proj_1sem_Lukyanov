import random


def sequence(N) -> str:
    line_sequence = []
    while N != 0:
        line_sequence.append(str(random.randint(-100, 100)))
        N -= 1
    line_sequence = " ".join(line_sequence)
    return line_sequence


# Создание и запись в файл 1
file1 = open('file1.txt', 'w+', encoding="UTF-8")
all_elements = sequence(random.randint(1, 10))
min_index = str(all_elements.split().index(str(min([int(x) for x in all_elements.split()]))))
file1.write(all_elements)
file1.close()

# Создание и запись в файл 2
file2 = open('file2.txt', 'w+', encoding="UTF-8")

file2_elements = sequence(random.randint(1, 10))
max_index = str(file2_elements.split().index(str(max([int(x) for x in file2_elements.split()]))))
all_elements += " " + file2_elements
count_elements = len(all_elements.split())
elements_are_multiples_of_4 = " ".join([str(x) for x in all_elements.split()
                                        if int(x) % 4 == 0])
file2.write(file2_elements)
file2.close()


# Создание и запись в файл 3, используя даннные из 1 и 2 файла
file3 = open('file3.txt', 'w', encoding="UTF-8")

file3.writelines([f'Элементы первого и второго файлов: {all_elements}\n',
                  f'Количество элементов первого и второго файлов: {count_elements}\n',
                  f'Индекс первого минимального элемента первого файла: {min_index}\n',
                  f'Индекс последнего максимального элемента второго файла: {max_index}\n',
                  f'Элементы кратные 4 первого и второго файлов: {elements_are_multiples_of_4}\n',])

file3.close()
