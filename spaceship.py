import pygame

class Spaceship():
    """"Класс для управления звездолётом."""

    def __init__(self, aic_game):
        """"Инициализирует звездолёт и задаёт его начальную позицию."""
        self.screen = aic_game.screen
        self.screen_rect = aic_game.screen.get_rect()
        self.settings = aic_game.settings 

        # Загружает изображение корабля и получает прямоугольник.
        self.image = pygame.image.load('images/spaceship.bmp')
        self.rect = self.image.get_rect()

        # Каждый новый корабль появляется у нижнего края экрана.
        self.rect.midbottom = self.screen_rect.midbottom

        # Сохранение вещественной координаты.
        self.x = float(self.rect.x)

        # Флаги перемещения.
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """"Обновляет позицию корабля с учётом флага."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.spaceship_speed
        elif self.moving_left and self.rect.left > 0:
            self.x -= self.settings.spaceship_speed
        
        # Обновление атрибута rect на основании self.x
        self.rect.x = self.x
            
    def blitme(self):
        """"Рисует звездолёт в текущей позиции. """
        self.screen.blit(self.image, self.rect)
