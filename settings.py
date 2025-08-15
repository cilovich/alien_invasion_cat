class Settings():
    """Класс для хранения всех настроек игры Alien Invasion Cats"""

    def __init__(self):
        """Инициализация настрокйи игры."""
        self.screen_width = 1100
        self.screen_heigth = 950
        self.bg_color = (100, 130, 230)
        self.spaceship_speed = 1.5
        # Поведение снарядов.
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_heigth = 15
        self.bullet_color = (60, 60, 100)
        self.bullets_allowed = 3
