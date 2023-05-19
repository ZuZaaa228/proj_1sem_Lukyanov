# Создайте класс «Банк», который имеет атрибуты суммы денег и процентной ставки.
# Добавьте методы для вычисления процентных начислений и снятия денег.

class Bank:  # Создаем класс Bank
    def __init__(self, money_count, percent):  # Переопределяем функцию инициализации класса
        self.money_count = money_count
        self.percent = percent

    def interest_charges(self):  # функция проверки начисления годовых
        return round((self.money_count * (self.percent / 100)) / 365 * 30, 2)

    def cash_withdrawal(self, count):  # функция для снятия денег
        if self.money_count > count:
            self.money_count -= count
            return True  # Возращает True, так как операция произошла успешно
        else:
            return 'У вас недостаточно средств!'  # Выводит сообщение об ошибке операции


bank_start = Bank(100000, 8)  # Инициализируем класс в переменную
print(bank_start.interest_charges())  # Проверяем кол-во годовых
print(bank_start.cash_withdrawal(700000))  # Попытка сняти денег > суммы на балансе
print(bank_start.money_count)  # Проверка баланса
print(bank_start.cash_withdrawal(70000))  # Попытка сняти денег < суммы на балансе
print(bank_start.money_count)  # Проверка баланса
