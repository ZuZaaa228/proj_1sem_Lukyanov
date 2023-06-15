import random

import pygame

from map import *
from settings import *
pygame.mixer.init()
shoot_sound = pygame.mixer.Sound('sound/shoot.mp3')
shoot_sound.set_volume(0.4)

class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 5
        self.direction = random.choice(['left', 'right', 'up', 'down'])


class Bullet:
    def __init__(self, pos, angle):
        self.x, self.y = pos
        self.angle = angle
        self.speed = 40
        self.rect = pygame.Rect(self.x, self.y, 2, 2)

    def update(self):
        self.x += self.speed * math.cos(self.angle)
        self.y += self.speed * math.sin(self.angle)
        self.rect.center = (self.x, self.y)


class Player:
    def __init__(self, pos, cam):
        self.x, self.y = pos
        self.cam_x, self.cam_y = cam
        self.angle = 0
        self.move_speed = 5
        self.bullets = []
        self.shoot_delay = 600  # задержка между выстрелами в миллисекундах
        self.last_shot_time = 0
        self.is_shooting = False

    @property
    def pos(self):
        return (self.x, self.y)

    def check_collision(self, delta_x, delta_y):
        # Проверяем, не выходим ли мы за границы карты
        new_x, new_y = self.x + delta_x, self.y + delta_y

        if not (0 <= new_x < len(open_map()[0]) * TILE) or not (0 <= new_y < len(open_map()) * TILE):
            return self.x, self.y

        # Проверяем столкновение со стенами карты
        for wall_x, wall_y in render_map(open_map())[0]:
            if new_x >= wall_x and new_x <= wall_x + TILE and new_y >= wall_y and (new_y <= wall_y + TILE):
                return self.x, self.y
        return new_x, new_y

    def movement(self):
        delta_x, delta_y = 0, 0

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            delta_y -= self.move_speed
        if keys[pygame.K_s]:
            delta_y += self.move_speed
            # Меняем позицию игрока по Y
        self.y = self.check_collision(delta_x, delta_y)[1]
        if keys[pygame.K_a]:
            delta_x -= self.move_speed
        if keys[pygame.K_d]:
            delta_x += self.move_speed
        # Меняем позицию игрока по X
        self.x = self.check_collision(delta_x, 0)[0]

        self.cam_x = max(0, min(self.x - WIDTH // 2, len(open_map()[0]) * TILE - WIDTH))
        self.cam_y = max(0, min(self.y - HEIGHT // 2, len(open_map()) * TILE - HEIGHT))

        # Обновляем положение мыши и угол игрока
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
        dx = self.mouse_x - self.x + self.cam_x
        dy = self.mouse_y - self.y + self.cam_y
        self.angle = math.atan2(dy, dx)

    def on_mouse_down(self, event):
        if event.button == 1:  # если нажата левая кнопка мыши
            self.is_shooting = True

    def on_mouse_up(self, event):
        if event.button == 1:  # если отпущена левая кнопка мыши
            self.is_shooting = False

    def shoot(self):
        if not self.is_shooting:
            return
        now = pygame.time.get_ticks()
        if now - self.last_shot_time >= self.shoot_delay:
            # создаем пулю и добавляем в список bullets
            bullet = Bullet((self.x - self.cam_x, self.y - self.cam_y), self.angle)
            self.bullets.append(bullet)
            self.last_shot_time = now
            shoot_sound.play()



    def update_bullets(self):
        # обновляем положение пуль и проверяем столкновение с объектами на карте
        new_bullets = []
        for bullet in self.bullets:
            bullet.update()
            hit_wall = False
            for wall_x, wall_y in render_map(open_map())[0]:
                if bullet.rect.colliderect(pygame.Rect(wall_x - self.cam_x, wall_y - self.cam_y, TILE, TILE)):
                    hit_wall = True
                    break
            if not hit_wall:
                new_bullets.append(bullet)
        self.bullets = new_bullets
