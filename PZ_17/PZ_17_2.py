# Создайте базовый класс "Фигура" со свойствами "ширина" и "высота".
# От этого класса унаследуйте классы "Прямоугольник" и "Квадрат".
# Для класса "Квадрат" переопределите методы, связанные с вычислением площади и периметра.

class Figure:  # Создаем класс Figure
    def __init__(self, height, width):
        self.height = height
        self.width = width


class Rectangle(Figure):  # Создаем класс Rectangle, наследуя от Figure
    ...


class Square(Figure):  # Создаем класс Square, наследуя от Figure
    def area_search(self):  # метод класса для поиска
        return self.width ** 2

    def perimeter_search(self):  # метод класса для поиска периметра
        return self.width * 4


print(Figure(12, 43).__dict__)  # Проверка на то что класс можно создать
print(Rectangle(20, 10).__dict__)  # Проверка на то что наследуемый класс можно создать
sq = Square(10, 12)  # Инициализация класс в переменную
print(sq.area_search())  # Поиск площади для квадрата
print(sq.perimeter_search())  # Поиск периметра для квадрата
