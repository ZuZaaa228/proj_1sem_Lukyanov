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
    (2, 7, 10),
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
    (4, 100),
    (5, 300),
    (6, 100),
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
    cur.execute("""UPDATE "Количество_товаров_на_складе" SET Количество = 555 WHERE id_tov=10""")
    # cur.execute("""UPDATE "Заявки_магазинов" SET Название = <новое название> WHERE id = <идентификатор заявки>"""))
    # cur.execute(""""""))
    # cur.execute(""""""))
    # cur.execute(""""""))
    # cur.execute(""""""))
    # cur.execute(""""""))
    # cur.execute(""""""))
    # print(cur.execute(""""""))
    # print(cur.execute(""""""))
    # print(cur.execute(""""""))
    # print(cur.execute(""""""))
    # print(cur.execute(""""""))
    #
    # 2. UPDATE "Заявки магазинов" SET название_товара = <новое название> WHERE id = <идентификатор заявки>
    # 3. UPDATE "Состав" SET Количество = <новое Количество> WHERE id_заявки = <идентификатор заявки> AND id_товара = <идентификатор товара>
    # 4. UPDATE "Заявки магазинов" SET адрес_магазина = <новый адрес> WHERE id_магазина = <идентификатор магазина>
    # 5. UPDATE "Заявки магазинов" SET дата_заявки = <новая дата> WHERE id_магазина = <идентификатор магазина>
    # 6. UPDATE "Количество_товаров_на_складе" SET Количество = <новое Количество> WHERE id_товара IN (<идентификатор товара 1>, <идентификатор товара 2>, ...)
    # 7. UPDATE "Товары" SET описание = <новое описание>, Количество = <новое Количество> WHERE id = <идентификатор товара>
    # 8. UPDATE "Количество_товаров_на_складе" SET Количество = Количество - <Количество выполненной заявки> WHERE id_товара IN (SELECT id_товара FROM "Состав" WHERE id_заявки = <идентификатор заявки>)
    # 9. UPDATE "Количество_товаров_на_складе" SET Количество = Количество - <Количество выполненной заявки> WHERE id_товара = <идентификатор товара> AND id IN (SELECT id FROM "Состав" WHERE id_заявки = <идентификатор заявки>)
    # 10. UPDATE "Заявки магазинов" SET название_магазина = <новое название>, адрес_магазина = <новый адрес> WHERE id = <идентификатор заявки>
    # 11. UPDATE "Заявки магазинов" SET название_магазина = <новое название> WHERE id_магазина = <идентификатор магазина>
    # 12. UPDATE "Состав" SET Количество = <новое Количество>, адрес_магазина = <новый адрес> WHERE id_заявки = <идентификатор заявки> AND id_товара = <идентификатор товара>
    # 13. UPDATE "Товары" SET описание = <новое описание>, Количество = <новое Количество> WHERE id IN (<идентификатор товара 1>, <идентификатор товара 2>, ...)
    #
    # print(cur.execute(""""""))
    # print(cur.execute(""""""))
    # print(cur.execute(""""""))
    # print(cur.execute(""""""))
    # print(cur.execute(""""""))
    # print(cur.execute(""""""))
    # print(cur.execute(""""""))
    # print(cur.execute(""""""))
    # print(cur.execute(""""""))

    # 2. DELETE FROM "Заявки магазинов" WHERE id = {id_заявки};
    #    DELETE FROM "Состав" WHERE id_заявки = {id_заявки};
    # 3. DELETE FROM "Количество_товаров_на_складе" WHERE id_товара NOT IN (SELECT id_товара FROM "Состав");
    # 4. DELETE FROM "Заявки магазинов" WHERE адрес LIKE "ул. Ленина%";
    # 5. DELETE FROM "Состав" WHERE id_товара NOT IN (SELECT id_товара FROM "Количество_товаров_на_складе" WHERE Количество > 0);
    # 6. DELETE FROM "Магазины" WHERE id NOT IN (SELECT id_магазина FROM "Заявки магазинов" WHERE дата_заявки >= date('now','-1 month'));
    # 7. DELETE FROM "Товары" WHERE id NOT IN (SELECT id_товара FROM "Состав");
    # 8. DELETE FROM "Количество_товаров_на_складе" WHERE id_товара NOT IN (SELECT id_товара FROM "Состав");
    # 9. DELETE FROM "Состав" WHERE id_заявки IN (SELECT id FROM "Заявки магазинов" WHERE дата_заявки < date('now','-1 month'));
