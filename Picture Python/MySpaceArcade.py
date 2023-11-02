# music by SketchyLogic
import pygame
from os import path
import random

#  инициируем пайгейм
pygame.init()
pygame.mixer.init()

WIDTH = 640
HEIGHT = 480
FPS = 60

font_name = pygame.font.match_font('arial')


def draw_text(surf, text, size, x, y):
    """Отрисовка текст"""
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


def newmob():
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)


def draw_shield_bar(surf, x, y, pct):
    if pct < 0:
        pct = 0
    bar_length = 100
    bar_height = 10
    fill = (pct / 100) * bar_length
    outline_rect = pygame.Rect(x, y, bar_length, bar_height)
    fill_rect = pygame.Rect(x, y, fill, bar_height)
    pygame.draw.rect(surf, GREEN, fill_rect)
    pygame.draw.rect(surf, WHITE, outline_rect, 2)


def draw_lives(surf, x, y, lives, _img):
    for live in range(lives):
        img_rect = img.get_rect()
        img_rect.x = x + 30 * live  # на растоянии 30 пикселей друг от друга
        img_rect.y = y
        surf.blit(_img, img_rect)


def show_go_screen():
    screen.blit(background, background_rect)
    draw_text(screen, "Аркада в космосе", 64, WIDTH / 2, HEIGHT / 4)
    draw_text(screen, "Управление на стрелочках, огонь на пробел", 22, WIDTH / 2, HEIGHT / 2)
    draw_text(screen, "Нажми кнопку, что-бы начать приключение", 18, WIDTH / 2, HEIGHT * 0.15)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for eve in pygame.event.get():
            if eve.type == pygame.QUIT:
                pygame.quit()
            if eve.type == pygame.KEYUP:
                waiting = False


class Player(pygame.sprite.Sprite):
    """мой игрок"""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)  # запускает инициализатор встроенных классов
        self.image = pygame.transform.scale(player_img, (50, 40))  # картинка игрока
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()  # оценивает изображение image и высчитывает прямоугольник, способный окружить
        self.radius = 20
        # pygame.draw.circle(self.image, RED, self.rect.center, self.radius)  # использовать при подгонке
        self.rect.centerx = WIDTH / 2    # первоночальное положение игрока
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0                  # скорость
        self.shield = 100  # щит
        self.shoot_delay = 250  # задержка перед выстрелами
        self.last_shot = pygame.time.get_ticks()
        self.lives = 3
        self.hidden = False
        self.hide_timer = pygame.time.get_ticks()
        self.power = 1
        self.power_time = pygame.time.get_ticks()
        self.POWERUP_TIME = 5000

    def update(self):
        """Дейстиве плеера при обновлении"""
        self.speedx = 0
        keystate = pygame.key.get_pressed()  # вовзращает True или False при проверки на нажатия кнопки
        if keystate[pygame.K_LEFT]:
            self.speedx -= 8
        if keystate[pygame.K_RIGHT]:
            self.speedx += 8
        if keystate[pygame.K_SPACE]:
            self.shoot()
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:         # ограничение чтобы игрок не ушел за пределы экрана
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.hidden and pygame.time.get_ticks() - self.hide_timer > 2000:
            self.hidden = False
            self.rect.centerx = WIDTH/2
            self.rect.bottom = HEIGHT - 10
        if self.power >= 2 and pygame.time.get_ticks() - self.power_time > self.POWERUP_TIME:
            self.power -= 1
            self.power_time = pygame.time.get_ticks()

    def shoot(self):
        """Стреьба на пробел"""
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay and not self.hidden:
            self.last_shot = now
            if self.power == 1:
                bullet = Bullet(self.rect.centerx, self.rect.top)
                all_sprites.add(bullet)
                bullets.add(bullet)
                shoot_sound.play()
            if self.power >= 2:
                bullet1 = Bullet(self.rect.left, self.rect.centery)
                bullet2 = Bullet(self.rect.right, self.rect.centery)
                all_sprites.add(bullet1)
                all_sprites.add(bullet2)
                bullets.add(bullet1)
                bullets.add(bullet2)
                shoot_sound.play()

    def hide(self):
        """Показать, если скрыто спустя 1 секунуд"""
        self.hidden = True
        self.hide_timer = pygame.time.get_ticks()
        self.rect.center = (WIDTH / 2, HEIGHT + 200)

    def powerup(self):
        self.power += 1
        self.power_time = pygame.time.get_ticks()


class Bullet(pygame.sprite.Sprite):
    """Снаряды"""
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(bullet_img, (10, 30))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = 15
        # pygame.draw.circle(self.image, RED, self.rect.center, self.radius)  # использовать при подгонке
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        # убираем спрайт если на границе
        if self.rect.bottom < 0:
            self.kill()


class Pow(pygame.sprite.Sprite):
    """Улучшения"""
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        self.type = random.choice(['shield', 'gun'])
        self.image = powerup_images[self.type]
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speedy = 2

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT:
            self.kill()


class Mob(pygame.sprite.Sprite):
    """Вражеские объекты"""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_orig = random.choice(meteor_images)
        self.image_orig.set_colorkey(BLACK)
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * .85 / 2)
        # pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-150, -100)
        self.speedy = random.randrange(1, 8)
        self.speedx = random.randrange(-3, 3)
        self.rot = 0  # штучки для поворотов спрайтов
        self.rot_speed = random.randrange(-8, 8)
        self.last_update = pygame.time.get_ticks()

    # вращение спрайта
    def rotate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 50:
            self.last_update = now
            self.rot = (self.rot + self.rot_speed) % 360
            new_image = pygame.transform.rotate(self.image_orig, self.rot)
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()  # при вращении картинки, делаем пересчет границ
            self.rect.center = old_center

    def update(self):
        self.rotate()
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random. randrange(-100, -40)
            self.speedy = random.randrange(1, 8)


class Explosion(pygame.sprite.Sprite):
    """взрывы"""
    def __init__(self, center, size):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.image = explosion_anim[self.size][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(explosion_anim[self.size]):
                self.kill()
            else:
                center = self.rect.center
                self.image = explosion_anim[self.size][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center


# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Создаем игру и окно
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")

#  настройка папки асситов и картинок
game_folder = path.dirname(__file__)
img_folder = path.join(game_folder, 'img')
snd_folder = path.join(game_folder, 'snd')
# Загрузка мелодий игры
shoot_sound = pygame.mixer.Sound(path.join(snd_folder, 'pew.wav'))
shield_sound = pygame.mixer.Sound(path.join(snd_folder, 'shield.wav'))
gun_sound = pygame.mixer.Sound(path.join(snd_folder, 'amo.wav'))
expl_sounds = []
for snd in ['expl3.wav', 'expl6.wav']:
    expl_sounds.append(pygame.mixer.Sound(path.join(snd_folder, snd)))
pygame.mixer.music.load(path.join(snd_folder, 'Venus.wav'))
pygame.mixer.music.set_volume(0.4)
cont_snd = pygame.mixer.Sound(path.join(snd_folder, "cont.wav"))

background = pygame.image.load(path.join(img_folder, 'background.png')).convert()
background_rect = background.get_rect()
player_img = pygame.image.load(path.join(img_folder, "ship.png")).convert()
player_mimi_img = pygame.transform.scale(player_img, (25, 19))
player_mimi_img.set_colorkey(BLACK)
bullet_img = pygame.image.load(path.join(img_folder, "shoot.png")).convert()
meteor_images = []
meteor_list = ['meteor.png', 'meteor (1).png', 'meteor (2).png',
               'meteor (3).png', 'meteor (4).png', 'meteor (5).png']
for img in meteor_list:
    meteor_images.append(pygame.image.load(path.join(img_folder, img)).convert())

explosion_anim = {}  # список картинок для аниации
explosion_anim['lg'] = []
explosion_anim['sm'] = []
explosion_anim['player'] = []
for i in range(9):
    filename = 'regularExplosion0{}.png'.format(i)
    img = pygame.image.load(path.join(img_folder, filename)).convert()
    img.set_colorkey(BLACK)
    img_lg = pygame.transform.scale(img, (75, 75))
    explosion_anim['lg'].append(img_lg)
    img_sm = pygame.transform.scale(img, (32, 32))
    explosion_anim['sm'].append(img_sm)
    filename = 'sonicExplosion0{}.png'.format(i)
    img = pygame.image.load(path.join(img_folder, filename)).convert()
    img.set_colorkey(BLACK)
    explosion_anim['player'].append(img)

powerup_images = {}
powerup_images['shield'] = pygame.image.load(path.join(img_folder, 'shield_gold.png')).convert()
powerup_images['gun'] = pygame.image.load(path.join(img_folder, 'bolt_gold.png')).convert()

clock = pygame.time.Clock()




pygame.mixer.music.play(loops=-1)  # запускаем музыку
# Цикл игры
game_over = True
running = True
while running:
    if game_over:
        show_go_screen()
        game_over = False
        all_sprites = pygame.sprite.Group()  # группировка спрайтов
        mobs = pygame.sprite.Group()
        bullets = pygame.sprite.Group()
        powerups = pygame.sprite.Group()
        player = Player()
        all_sprites.add(player)
        for i in range(10):  # добавляем 10 врагов в группу
            newmob()
        score = 0  # счет
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Обновление
    all_sprites.update()
    # Проверка, не ударил ли моб игрока
    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
    for hit in hits:
        score += 50 - hit.radius  # от размера зависит кол-во очков
        random.choice(expl_sounds).play()  # случайный взрыв
        expl = Explosion(hit.rect.center, 'lg')
        all_sprites.add(expl)
        if random.random() > 0.9:
            pow = Pow(hit.rect.center)
            all_sprites.add(pow)
            powerups.add(pow)
        newmob()

    # Провкерка на прикосновение
    hits = pygame.sprite.spritecollide(player, mobs, True, pygame.sprite.collide_circle)
    for hit in hits:
        player.shield -= hit.radius * 2
        cont_snd.play()
        expl = Explosion(hit.rect.center, 'sm')
        all_sprites.add(expl)
        newmob()
        if player.shield <= 0:
            death_explosion = Explosion(player.rect.center, 'player')
            all_sprites.add(death_explosion)
            player.hide()
            player.lives -= 1
            player.shield = 100
        if player.lives == 0:
            game_over = True
    hits = pygame.sprite.spritecollide(player, powerups, True)
    for hit in hits:
        if hit.type == 'shield':
            player.shield += random.randrange(10, 30)
            if player.shield >= 100:
                player.shield = 100
                shield_sound.play()
        if hit.type == 'gun':
            player.powerup()
            gun_sound.play()
    # Рендеринг
    screen.fill(BLACK)
    screen.blit(background, background_rect)
    all_sprites.draw(screen)
    draw_text(screen, str(score), 18, WIDTH / 2, 10)  # счетчик
    # После отрисовки всего, переворачиваем экран
    draw_text(screen, str(score), 18, WIDTH / 2, 10)  # здоровье
    draw_shield_bar(screen, 5, 5, player.shield)
    draw_lives(screen, WIDTH - 100, 5, player.lives, player_mimi_img)
    pygame.display.flip()
pygame.quit()
