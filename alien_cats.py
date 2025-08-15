import pygame
from pygame.sprite import Sprite


class Alien_Cats(Sprite):
    """Класс, представляющий одного кота-пришельца."""

    def __init__(self, aic_game):
        """Инициализирует кота и задаёт его начальную позицию."""
        super().__init__()
        self.screen = aic_game.screen

        # Загрузка изображения пришельца и назначение атрибута rect.
        self.image = pygame.image.load('images\alien_cats_1.bmp')
        self.rect = self.image.get_rect()

        # Каждый новый пришелец появляется в верхнем левом углу экрана.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Сохранение точной горизонтальной позиции пришельца.
        self.x = float(self.rect.x)