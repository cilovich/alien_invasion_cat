""" Вторжение инопланетных котов (ALIEN INVASION CATS).
Суть игры - космос, уничтожение пришельцев-котов, один игрок - один корабль.
Игрок помещает корабль в разные стороны клавишами управления курсора; клавиша
'пробел' - стрельба. Уничтожение одного врага осуществляется выстрелами,
уничтожение - появление более быстрых пришельцев. Если кот-пришелец
сталкивается с кораблём или доходит до нижнего края экрана - потеря корабля.
потеря всех трёх кораблей - GAMEOVER!
Да прибудет с Вами сила!
"""


import sys
import pygame

from settings import Settings
from spaceship import Spaceship
from bullet import Bullet


class AlienInvasionCats():
    """Класс для управления ресурсами игры."""

    def __init__(self):
        """Инициализирует игру и создёт игровые ресурсы."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_heigth))
        pygame.display.set_caption("Alien Invasion Cats")

        # Назначение цвета фона.
        self.bg_color = (230, 100, 230)

        # Назначение звездолёта.
        self.spaceship = Spaceship(self)
        self.bullets = pygame.sprite.Group()

    def _chek_events(self):
        """Реагирует на нажатие клавиш и события мыши."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._chek_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._chek_keyup_events(event)

    def _chek_keydown_events(self, event):
        """Реагирует на нажатие клавиш."""
        if event.key == pygame.K_RIGHT:
            # Переместить корабль вправо.
            self.spaceship.moving_right = True
        elif event.key == pygame.K_LEFT:
            # Переместить корабль влево.
            self.spaceship.moving_left = True
        elif event.key == pygame.K_ESCAPE:
            sys.exit()

    def _chek_keyup_events(self, event):
        """"Реагирует на отпускание клавиш."""
        if event.key == pygame.K_RIGHT:
            self.spaceship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.spaceship.moving_left = False
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _fire_bullet(self):
        """"Создание нового снаряда и включение в группу bullets."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_screen(self):
        """Обновляет и отображает новый экран."""
        self.screen.fill(self.settings.bg_color)
        # Обновление позиции звездолёта в его текущем положении.
        self.spaceship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # Отображение последнего прорисованного экрана.
        pygame.display.flip()

    def run_game(self):
        """Запуск основного цикла игры."""
        while True:
            self._chek_events()
            self.spaceship.update()
            self.bullets.update()
            self._update_screen()

            # Удаление снарядов, вышедших за край экрана.
            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)


if __name__ == '__main__':
    # Создание экземпляра игры и запуска её процесса.
    aic = AlienInvasionCats()
    aic.run_game()
