import pygame
import os
import random

#  настройка папки асситов
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')
player_img = pygame.image.load(os.path.join(img_folder, 'p1_jump.png'))

pygame.init()
pygame.mixer.init()

WIDTH = 360
HEIGHT = 480
FPS = 30


class Player(pygame.sprite.Sprite):
    """Определяем новый спрайт"""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)  # размещаем спрайт по середине

    def update(self):
        """Дейстиве плеера при обновлении"""
        self.rect.x += 5
        if self.rect.left > WIDTH:
            self.rect.right = 0


# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Создаем игру и окно
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()  # группировка спрайтов
player = Player()
all_sprites.add(player)

# Цикл игры
running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Обновление
    all_sprites.update()

    # Рендеринг
    screen.fill(BLUE)
    all_sprites.draw(screen)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()

