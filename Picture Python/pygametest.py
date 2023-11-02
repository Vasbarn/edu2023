import pygame
from pygame.draw import *  # this will allow to use : "rect(..)" instead "pygame.draw.rect(...)"

# after import pygame. it needed initial
pygame.init()
# and create window
sreen = pygame.display.set_mode((400, 400))

# here draw figures

# after draw ,need show it on sreen - update
pygame.display.update()
# this command need repeat after everyone changes

# here place for main cycle
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

# Также хорошей практикой является добавление небольшой задержки в главный цикл программы,
# чтобы не заставлять ее работать "вхолостую", постоянно считывая события, которых, скорее всего, нет.
# Для этого в pygame есть специальный модуль time. До начала главного цикла создаем объект Clock:
clock = pygame.time.Clock()
# После этого в главном цикле добавляем строку:
clock.tick(30)
#З десь 30 - это максимальный FPS, быстрее которого программа работать не будет. Естественно, можно указать и
# любое другое значение (которое, кстати, есть смысл записать в отдельную переменную для легкого доступа).
