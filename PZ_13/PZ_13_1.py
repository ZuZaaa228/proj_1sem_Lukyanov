import numpy as np  # Импортируем нампай
import random  # Импортируем ранндом

matr = np.array([[  # Генерируем нампай массив(матрицу)
    random.randint(0, 30) for i in range(4)
] for x in range(random.randint(2, 4))]
)
print(
    f"Сгенерированная матрица: \n{matr}"  # Выводим матрицу
)
for x in np.nditer(matr, op_flags=['readwrite']):  # Итерируем массив и меняем в нем значения по усл
    if x[...] > 10:
        x[...] = 0

print(f"Матрица, где числа > 10 изменились на 0:\n{matr}")  # Выводим сгенерированную матрицу
