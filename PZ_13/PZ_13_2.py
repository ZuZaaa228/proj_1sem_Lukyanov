# В квадратной матрице все элементы, не лежащие на главной диагонали увеличить в
# 2 раза.
import random

count = random.randint(2, 6)  # Генерируем размер матрицы
matr = [[random.randint(0, 50) for x in range(count)]
        for i in range(count)]  # Создаем матрицу
print(f"Сгенерированая матрица: \n{matr}")

for x, y in enumerate(matr):  # Проходимся по строкам матрицы
    for i, o in enumerate(y):  # проходимся по каждому элементу матрицы
        if i != x:
            matr[x][i] = o*2
print(f"новая матрица: \n{matr}")
