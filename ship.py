import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """Класс для управления кораблем."""
    def __init__(self, ai_game):
        """Инициализирует корабль и задает его начальную позицию."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        # получить прямоугольник экрана
        self.screen_rect = ai_game.screen.get_rect()

        # загрузить изображение
        self.image = pygame.image.load('images/ship.bmp')
        # получает прямоугольник из изображения
        self.rect = self.image.get_rect()

        # установить середину нижнего края экрана
        self.rect.midbottom = self.screen_rect.midbottom

        # Сохранение вещественной координаты центра корабля
        self.x = float(self.rect.x)

        self.moving_right = False   # флаг непрерывного движения вправо
        self.moving_left = False    # флаг непрерывного движения влево

    def update(self):
        """Обновляет позицию корабля с учетом флага."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed  # перемещает корабль вправо
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed  # перемещает корабль влево

        self.rect.x = self.x

    def blitme(self):
        """Рисует корабль в текущей позиции."""
        self.screen.blit(self.image, self.rect) # отобразить изображение на экране

    def center_ship(self):
        """Размещает корабль в центре нижней стороны."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)