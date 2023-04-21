import sqlite3 as sq

goods = [
    ('Молоко', 'Описание молока', 'литр'),
    ('Кефир', 'Описание кефира', 'литр'),
    ('Вода', 'Описание воды', 'литр'),
    ('Газировка', 'Описание газировки', 'литр'),
    ('Колбаса', 'Описание колбасы', 'грамм'),
    ('Сыр', 'Описание сыра', 'грамм'),
    ('Чипсы', 'Описание чипсов', 'грамм'),
    ('Сухарики', 'Описание сухариков', 'грамм'),
    ('Суп', 'Описание супа', 'литр'),
    ('Мята', 'Описание мяты', 'грамм'),
    ('Помидоры', 'Описание помидоров', 'шт'),
    ('Огурцы', 'Описание огурцов', 'шт'),
    ('Зелень', 'Описание зелени', 'грамм'),
    ('Рыба', 'Описание рыбы', 'грамм'),
    ('Мясо Курицы', 'Описание мяса', 'грамм'),
]

sostav = [
    (1, 1, 200),
    (1, 5, 100),
    (1, 6, 50),
    (2, 2, 50),
    (2, 7, 20),
    (2, 8, 100),
    (3, 3, 200),
    (3, 4, 50),
    (3, 9, 50),
    (4, 2, 150),
    (4, 10, 150)
]

count_sklad = [
    (1, 1000),
    (2, 200),
    (3, 500),
    (11, 100),
    (5, 300),
    (6, 0),
    (7, 50),
    (8, 400),
    (9, 100),
    (10, 300)
]

ac = [
    (1, '2021-08-01'),
    (2, '2021-08-03'),
    (3, '2021-08-05'),
    (4, '2021-08-07')
]

shops = [
    ('Алмазный', 'ул. Ленина, 10', '+7 (495) 123-45-67'),
    ('Мир продуктов', 'ул. Пушкина, 5', '+7 (495) 234-56-78'),
    ('Океан', 'пр-т Мира, 20', '+7 (495) 345-67-89'),
    ('Пятёрочка', 'ул. Садовая, 2', '+7 (495) 456-78-90')
]

with sq.connect('baze.db') as con:
    con.execute("PRAGMA foreign_keys = ON")
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS Товары(
        id_tov integer PRIMARY KEY AUTOINCREMENT,
        Название varchar,
        Описание varchar,
        Единица_измерения varchar


    )""")
    cur.execute("""CREATE TABLE IF NOT EXISTS Магазины (
        id_маг integer PRIMARY KEY AUTOINCREMENT,
        Название varchar,
        Адрес varchar,
        Телефон varchar
)   """)

    cur.execute("""CREATE TABLE IF NOT EXISTS "Заявки_магазинов" (
        id_заяв integer PRIMARY KEY AUTOINCREMENT,
        Дата_заявки date,
        id_маг integer,
        FOREIGN KEY (id_маг) REFERENCES Магазины(id_маг) ON DELETE CASCADE ON UPDATE CASCADE
    )""")

    cur.execute("""CREATE TABLE IF NOT EXISTS "Количество_товаров_на_складе" (
        id_кол integer PRIMARY KEY AUTOINCREMENT,
        Количество integer,
        id_tov integer,
        FOREIGN KEY (id_tov) REFERENCES Товары(id_tov) ON DELETE CASCADE ON UPDATE CASCADE
    )""")

    cur.execute("""CREATE TABLE IF NOT EXISTS Состав (
        id_сост integer PRIMARY KEY AUTOINCREMENT,
        Количество integer,
        id_заяв integer,
        id_tov integer,
        FOREIGN KEY (id_tov) REFERENCES Товары(id_tov) ON DELETE CASCADE ON UPDATE CASCADE
        FOREIGN KEY (id_заяв) REFERENCES Заявки_магазинов(id_заяв) ON DELETE CASCADE ON UPDATE CASCADE
    )""")

    # cur.executemany("INSERT INTO Товары (Название, Описание, Единица_измерения) VALUES (?, ?, ?)", goods)
    # cur.executemany("""INSERT INTO Магазины (Название, Адрес, Телефон) VALUES (?, ?, ?)""", shops)
    # cur.executemany("""INSERT INTO Заявки_магазинов (id_маг, Дата_заявки) VALUES (?, ?)""", ac)
    # cur.executemany("""INSERT INTO Количество_товаров_на_складе (id_tov, Количество) VALUES (?, ?)""", count_sklad)
    # cur.executemany("""INSERT INTO Состав (id_заяв, id_tov, Количество) VALUES (?,?,?)""", sostav)

    # print(cur.execute("""SELECT Название, Описание FROM Товары""").fetchall())
    # print(cur.execute("""SELECT Название, Адрес FROM Магазины""").fetchall())
    # print(cur.execute("""SELECT id_маг, Дата_заявки FROM 'Заявки_магазинов'""").fetchall())
    # print(cur.execute("""SELECT id_tov, Количество FROM 'Количество_товаров_на_складе'""").fetchall())
    # print(cur.execute("""SELECT id_tov, Количество FROM 'Количество_товаров_на_складе' ORDER BY Количество DESC""").fetchall())
    # print(cur.execute("""SELECT "Заявки_магазинов".id_заяв, id_tov FROM "Заявки_магазинов" JOIN "Состав" ON "Заявки_магазинов".id_заяв = "Состав".id_заяв""").fetchall())
    # print(cur.execute("""SELECT Название FROM Товары JOIN "Количество_товаров_на_складе" ON Товары.id_tov = "Количество_товаров_на_складе".id_tov WHERE Количество < 101""").fetchall())
    # print(cur.execute("""SELECT * FROM "Заявки_магазинов" WHERE Дата_заявки BETWEEN '2021-08-03' AND '2021-08-06'""").fetchall())
    # print(cur.execute("""SELECT Магазины.id_маг, SUM("Количество_товаров_на_складе".Количество) as total FROM Магазины JOIN "Заявки_магазинов" ON Магазины.id_маг = "Заявки_магазинов".id_маг JOIN "Состав" ON "Заявки_магазинов".id_заяв = "Состав".id_заяв JOIN "Количество_товаров_на_складе" ON "Состав".id_tov = "Количество_товаров_на_складе".id_tov GROUP BY Магазины.id_маг HAVING total < 1000""").fetchall())
    #

    #
    # cur.execute("""UPDATE "Количество_товаров_на_складе" SET Количество = 555 WHERE id_tov=10""")
    # cur.execute("""UPDATE "Товары" SET Название = 'сыыр' WHERE id_tov = 6""")
    # cur.execute("""UPDATE "Состав" SET Количество = 201 WHERE id_заяв = 1 AND id_tov = 1""")
    # cur.execute("""UPDATE "Магазины" SET Адрес = 'ул. Ленина 278' WHERE id_маг = (SELECT id_маг FROM 'Заявки_магазинов' WHERE id_маг = 1)""")
    # cur.execute("""UPDATE "Заявки_магазинов" SET Дата_заявки = '2021-08-04' WHERE id_маг = 2""")
    # cur.execute("""UPDATE "Количество_товаров_на_складе" SET Количество = 528 WHERE id_tov IN (1, 2, 5)""")
    #

    #
    # cur.execute("""DELETE FROM "Заявки_магазинов" WHERE id_заяв = 1""")
    # cur.execute("""DELETE FROM "Количество_товаров_на_складе" WHERE id_tov NOT IN (SELECT id_tov FROM "Состав")""")
    # cur.execute("""DELETE FROM "Магазины" WHERE Адрес LIKE 'ул. Ленина%'""")
    # cur.execute("""DELETE FROM "Состав" WHERE id_tov IN (SELECT id_tov FROM "Количество_товаров_на_складе" WHERE Количество = 0)""")
    # cur.execute("""DELETE FROM "Магазины" WHERE id_маг NOT IN (SELECT id_маг FROM "Заявки_магазинов" WHERE Дата_заявки >= date('now','-1 month'))""")
    # cur.execute("""DELETE FROM "Товары" WHERE id_tov NOT IN (SELECT id_tov FROM "Состав")""")
    # cur.execute("""DELETE FROM "Количество_товаров_на_складе" WHERE id_tov NOT IN (SELECT id_tov FROM "Состав")""")
    # cur.execute("""DELETE FROM "Состав" WHERE id_заяв IN (SELECT id_заяв FROM "Заявки_магазинов" WHERE Дата_заявки < date('now','-1 month'))""")
