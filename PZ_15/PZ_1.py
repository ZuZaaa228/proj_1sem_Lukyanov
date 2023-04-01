import sqlite3 as sq


goods = [
    (0, 'Молоко', 'Описание молока', 'литр'),
    (0, 'Кефир', 'Описание кефира', 'литр'),
    (0, 'Вода', 'Описание воды', 'литр'),
    (0, 'Газировка', 'Описание газировки', 'литр'),
    (0, 'Колбаса', 'Описание колбасы', 'грамм'),
    (0, 'Сыр', 'Описание сыра', 'грамм'),
    (0, 'Чипсы', 'Описание чипсов', 'грамм'),
    (0, 'Сухарики', 'Описание сухариков', 'грамм'),
    (0, 'Суп', 'Описание супа', 'литр'),
    (0, 'Мята', 'Описание мяты', 'грамм'),
    (0, 'Помидоры', 'Описание помидоров', 'шт'),
    (0, 'Огурцы', 'Описание огурцов', 'шт'),
    (0, 'Зелень', 'Описание зелени', 'грамм'),
    (0, 'Рыба', 'Описание рыбы', 'грамм'),
    (0, 'Мясо Курицы', 'Описание мяса', 'грамм'),
]


with sq.connect('baze.db') as con:
    con.execute("PRAGMA foreign_keys = ON")
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS Товары(
        id_tov integer PRIMARY KEY AUTOINCREMENT,
        Название varchar,
        Описание varchar,
        Единица измерения varchar
    )""")
    cur.execute("""CREATE TABLE IF NOT EXISTS Магазины (
        id_маг integer PRIMARY KEY AUTOINCREMENT,
        Название varchar,
        Адрес varchar,
        Телефон varchar
)   """)
    cur.execute("""CREATE TABLE IF NOT EXISTS "Заявки магазинов" (
        id_заяв integer PRIMARY KEY AUTOINCREMENT,
        Дата заявки date,
        id_маг integer
    )""")
    cur.execute("""CREATE TABLE IF NOT EXISTS "Количество товаров на складе" (
        id_кол integer PRIMARY KEY AUTOINCREMENT,
        Количество integer,
        id_тов integer
    )""")
    cur.execute("""CREATE TABLE IF NOT EXISTS Состав (
        id_сост integer PRIMARY KEY AUTOINCREMENT,
        Количество integer,
        id_заяв integer,
        id_тов integer
    )""")

    cur.executemany('INSERT INTO Товары VALUES (?, ?, ?, ?)', goods)