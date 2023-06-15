
import sys

import pygame
from drawing import Drawing

from player import *
from settings import *


pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

font2 = pygame.font.Font(FONT_PATH2, FONT_SIZE2)
game_started = False
while not game_started:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
            game_started = True
            break
    sc.fill(BLACK)
    text1 = font2.render("""Управление:""", True, RED)
    sc.blit(text1, (WIDTH // 2 - text1.get_width() // 2, (HEIGHT // 2 - text1.get_height() // 2)*0.4))
    text2 = font2.render("""W,A,S,D - движение (верх, влево, вниз, вправо)""", True, RED)
    sc.blit(text2, ((WIDTH // 2 - text2.get_width() // 2), (HEIGHT // 2 - text2.get_height() // 2)*0.6))
    text3 = font2.render("""ЛКМ - выстрел""", True, RED)
    sc.blit(text3, ((WIDTH // 2 - text3.get_width() // 2), (HEIGHT // 2 - text3.get_height() // 2)*0.8))
    text4 = font2.render("""U - генерация нового уровня""", True, RED)
    sc.blit(text4, ((WIDTH // 2 - text4.get_width() // 2), (HEIGHT // 2 - text4.get_height() // 2)*1))
    text5 = font2.render("""R - перезапуск уровня""", True, RED)
    sc.blit(text5, ((WIDTH // 2 - text5.get_width() // 2), (HEIGHT // 2 - text5.get_height() // 2) * 1.2))
    text6 = font2.render("""V - Изменить главный саундтрек""", True, RED)
    sc.blit(text6, ((WIDTH // 2 - text6.get_width() // 2), (HEIGHT // 2 - text6.get_height() // 2) * 1.4))
    text7 = font2.render("""Нажмите любую клавишу для продолжения""", True, WHITE)
    sc.blit(text7, ((WIDTH // 2 - text7.get_width() // 2), (HEIGHT // 2 - text7.get_height() // 2) * 1.8))


    pygame.display.update()
    clock.tick(FPS)

count_track = 1
pygame.mixer.Sound(f'sound/main_{count_track}.mp3').play().set_volume(0.2)

font = pygame.font.Font(FONT_PATH, FONT_SIZE)
cam_x, cam_y = 0, 0
player = Player(player_pos, (cam_x, cam_y))
bullet_texture = pygame.image.load('textures/bullet.png')
hitmarker_sound = pygame.mixer.Sound('sound/hitmarker.mp3')

world_map, enemy_map = render_map(open_map())

# enemy_walls = [(enemy[0], enemy[1]) for enemy in enemy_map]
enemy_walls = [Enemy(enemy[0], enemy[1]) for enemy in enemy_map]

killed_enemies = 0
alive_enemies = len(enemy_walls)

world_walls = list(world_map)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            player.on_mouse_down(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            player.on_mouse_up(event)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_u:
                cam_x, cam_y = 0, 0
                player = Player(player_pos, (cam_x, cam_y))
                world_map, enemy_map = render_map(save_map().get('maps'))
                world_walls = list(world_map)
                enemy_walls = [Enemy(enemy[0], enemy[1]) for enemy in enemy_map]
                killed_enemies = 0
                alive_enemies = len(enemy_walls)

            if event.key == pygame.K_r:
                cam_x, cam_y = 0, 0
                player = Player(player_pos, (cam_x, cam_y))
                enemy_walls = [Enemy(enemy[0], enemy[1]) for enemy in enemy_map]
                killed_enemies = 0
                alive_enemies = len(enemy_walls)
            if event.key == pygame.K_v:
                count_track += 1
                pygame.mixer.stop()
                pygame.mixer.Sound(f'sound/main_{count_track}.mp3').play()
                if count_track == 11:
                    count_track = 1
    player.movement()
    player.shoot()
    # обновляем положение пуль и проверяем столкновение с объектами на карте
    player.update_bullets()

    sc.fill(BLACK)

    Drawing.draw_enemy_map(sc, [(enemy.x, enemy.y) for enemy in enemy_walls], player.cam_x, player.cam_y)

    Drawing.draw_world_map(sc, world_walls, player.cam_x, player.cam_y)

    Drawing.draw_player(sc, player.x, player.y, player.cam_x, player.cam_y, player.angle)


    for bullet in player.bullets:
        sc.blit(pygame.transform.rotate(bullet_texture, -math.degrees(bullet.angle) - 90), bullet.rect)
        for idx, obj in enumerate(enemy_walls):
            enemy_rect = pygame.Rect(obj.x - player.cam_x, obj.y - player.cam_y, TILE, TILE)
            if enemy_rect.colliderect(bullet.rect):
                enemy_walls.remove(obj)
                killed_enemies += 1
                alive_enemies -= 1
                hitmarker_sound.play()
                break

    # отрисовка счета
    killed_text = font.render("Killed: " + str(killed_enemies), True, RED)
    alive_text = font.render("Alive: " + str(alive_enemies), True, RED)
    sc.blit(killed_text, (10, 10))
    sc.blit(alive_text, (10, 40))
    pygame.display.update()
    clock.tick(FPS)
