import json
import random

map_height = 33
map_weight = 50


# def generate_map_box(map_height, map_weight) -> list:
#     world = [["_" for _ in range(map_weight)] for _ in range(map_height)]
#
#     world[0] = ["W" for _ in range(map_weight)]
#     world[-1] = ["W" for _ in range(map_weight)]
#
#     for idx, item in enumerate(world):
#         if idx == 0 or idx == (map_weight - 1):
#             pass
#         else:
#             world[idx][0] = "W"
#             world[idx][map_weight - 1] = "W"
#     return world

# def generate_map_box(map_height, map_width) -> list:
#     # создаем пустую карту
#     world = [["_" for _ in range(map_width)] for _ in range(map_height)]
#
#     # добавляем внешние стены
#     world[0] = ["W" for _ in range(map_width)]
#     world[-1] = ["W" for _ in range(map_width)]
#     for idx, item in enumerate(world):
#         if idx == 0 or idx == (map_height - 1):
#             pass
#         else:
#             world[idx][0] = "W"
#             world[idx][map_width - 1] = "W"
#
#     # добавляем случайные стены
#     num_walls = int((map_height * map_width) * 0.2)  # количество стен (10% от общей площади)
#     for i in range(num_walls):
#         # выбираем случайные координаты внутри карты
#         x = random.randint(1, map_width - 2)
#         y = random.randint(1, map_height - 2)
#
#         # если выбранная ячейка пуста и не перекрывает проход игроку - добавляем стену
#         if world[y][x] == "_" and not (x == 1 and y == map_height // 2):
#             world[y][x] = "W"
#
#     return world

def generate_map_box(map_height, map_width) -> list:
    # создаем пустую карту
    world = [["_" for _ in range(map_width)] for _ in range(map_height)]

    # добавляем внешние стены
    world[0] = ["W" for _ in range(map_width)]
    world[-1] = ["W" for _ in range(map_width)]
    for idx, item in enumerate(world):
        if idx == 0 or idx == (map_height - 1):
            pass
        else:
            world[idx][0] = "W"
            world[idx][map_width - 1] = "W"

    # добавляем случайные стены
    num_walls = int((map_height * map_width) * 0.2)  # количество стен (10% от общей площади)
    for i in range(num_walls):
        # выбираем случайные координаты внутри карты
        x = random.randint(1, map_width - 2)
        y = random.randint(1, map_height - 2)

        # если выбранная ячейка пуста и не перекрывает проход игроку - добавляем стену
        if world[y][x] == "_" and not (x == 1 and y == map_height // 2):
            world[y][x] = "W"

    # добавляем случайных врагов
    num_enemies = int((map_height * map_width) * 0.03)  # количество врагов (5% от общей площади)
    for i in range(num_enemies):
        # выбираем случайные координаты внутри карты
        x = random.randint(1, map_width - 2)
        y = random.randint(1, map_height - 2)

        # если выбранная ячейка пуста и не перекрывает проход игроку - добавляем врага
        if world[y][x] == "_" and not (x == 1 and y == map_height // 2):
            world[y][x] = "E"

    return world



def save_map():
    world = {
        "maps": (generate_map_box(map_height, map_weight))
    }
    with open('maps/map.json', 'w') as map:
        json.dump(world, map)
    return world