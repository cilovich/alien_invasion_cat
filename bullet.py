"""Функциональность стрельбы.
Выпускание снарядов при нажатии клавиши 'пробел'. Снаряды летят
вертикально, пока не исчезнут у верхнего края экрана."""

import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Класс управления снарядами, выпущенными звездолётом."""
    def __init__(self, aic_game):
        """Создание объект снарядов текущей позиции корабля."""
        super().__init__()
        self.screen = aic_game.screen
        self.settings = aic_game.settings
        self.color = self.settings.bullet_color

        # Создание снарядов позиции (0, 0) и назначение правильной позиции.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_heigth)
        self.rect.midtop = aic_game.spaceship.rect.midtop

        # Позиция снаряда хранится в вещественном формате.
        self.y = float(self.rect.y)

    def update(self):
        """"Перемещает снаряд вверх по экрану."""
        self.y -= self.settings.bullet_speed
        # Обновление позиции прямоугольника.
        self.rect.y = self.y

    def draw_bullet(self):
        """Вывод снаряда на экран."""
        pygame.draw.rect(self.screen, self.color, self.rect)
