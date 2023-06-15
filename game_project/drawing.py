import pygame
from settings import *

wall_texture = pygame.image.load('textures/wall1.png')
bullet_texture = pygame.image.load('textures/bullet.png')
player_texture = pygame.image.load('textures/player1.png')
enemy_texture1 = pygame.image.load('textures/enemy1.png')

hitbox_width = -30
hitbox_height = -30

class Drawing:
    @staticmethod
    def draw_world_map(sc, world_map, player_cam_x, player_cam_y):
        for x, y in world_map:
            wall_rect = wall_texture.get_rect()
            sc.blit(wall_texture, (x - player_cam_x, y - player_cam_y, TILE, TILE), wall_rect)
            # pygame.draw.rect(sc, DARKGRAY, (x - player_cam_x, y - player_cam_y, TILE, TILE), 2)

    @staticmethod
    def draw_enemy_map(sc, enemy_map, player_cam_x, player_cam_y):
        for x, y in enemy_map:
            # sc.blit(enemy_texture1, (x - player_cam_x, y - player_cam_y))
            texture_x = x - hitbox_width / 2 - player_cam_x
            texture_y = y - hitbox_height / 2 - player_cam_y
            sc.blit(enemy_texture1, (texture_x, texture_y))

    @staticmethod
    def draw_player(sc, player_x, player_y, player_cam_x, player_cam_y, player_angle):
        # pygame.draw.line(sc, GREEN, (player_x - player_cam_x, player_y - player_cam_y),
        #                  (player_x - player_cam_x + WIDTH * math.cos(player_angle),
        #                   player_y - player_cam_y + WIDTH * math.sin(player_angle)), 2)
        # pygame.draw.circle(sc, GREEN, (int(player_x - player_cam_x), int(player_y - player_cam_y)), 12)
        player_rect = player_texture.get_rect(center=(int(player_x - player_cam_x), int(player_y - player_cam_y)))
        rotated_texture = pygame.transform.rotate(player_texture, -math.degrees(player_angle)-90)  # повернуть изображение в соответствии с углом поворота персонажа
        sc.blit(rotated_texture, player_rect)