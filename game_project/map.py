from maps.create_map import *
from settings import *


def open_map():
    with open('maps/map.json', 'r') as maps:
        text_map = json.loads(maps.read())['maps']
    return text_map


def reload_map():
    save_map()
    return open_map()


def render_map(text_map):
    world_map = set()
    enemy_map = set()

    for j, row in enumerate(text_map):
        for i, char in enumerate(row):
            if char == 'W':
                world_map.add((i * TILE, j * TILE))
            elif char == 'E':
                enemy_map.add((i * TILE, j * TILE))
    return world_map, enemy_map
