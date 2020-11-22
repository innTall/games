''' графика '''
import pygame
import random
from os import path

# определить местоположение папки img
img_dir = path.join(path.dirname(__file__), 'images')

# 2. базовые настройки экрана
WIDTH = 480
HEIGHT = 600
FPS = 60
screen = pygame.display.set_mode((WIDTH, HEIGHT))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Загрузка всей игровой графики
background = pygame.image.load(path.join(img_dir, 'blue.png')).convert()
background_rect = background.get_rect()
player_img = pygame.image.load(path.join(img_dir, "playerShip1_orange.png")).convert()
meteor_img = pygame.image.load(path.join(img_dir, "meteorBrown_med3.png")).convert()
bullet_img = pygame.image.load(path.join(img_dir, "laserRed06.png")).convert()

# Создание спрайта - базовые настройки
class Player(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.image = player_img # заменить зеленый прямоугольник
    self.image = pygame.transform.scale(player_img, (50, 30))
    self.image.set_colorkey(BLACK) # убрать черный прямоугольник вокруг корабля
    self.rect = self.image.get_rect()
    self.rect.centerx = WIDTH / 2
    self.rect.bottom = HEIGHT - 10
    self.speedx = 0

  # создание пули, с местом появления из середины верхней части игрока
  def shoot(self):
    bullet = Bullet(self.rect.centerx, self.rect.top)
    all_sprites.add(bullet)
    bullets.add(bullet)

  # Движение / управление
  def update(self):
    self.speedx = 0
    keystate = pygame.key.get_pressed()
    if keystate[pygame.K_LEFT]:
      self.speedx = -8
    if keystate[pygame.K_RIGHT]:
      self.speedx = 8
    self.rect.x += self.speedx
    if self.rect.right > WIDTH:
      self.rect.right = WIDTH
    if self.rect.left < 0:
      self.rect.left = 0

# определения свойств спрайта врага
class Mob(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.image = meteor_img
    self.image.set_colorkey(BLACK)
    self.rect = self.image.get_rect()
    self.rect.x = random.randrange(WIDTH - self.rect.width)
    self.rect.y = random.randrange(-100, -40)
    self.speedy = random.randrange(1, 8)
    self.speedx = random.randrange(-3, 3)

  # управление спрайтами врагов
  def update(self):
    self.rect.x += self.speedx
    self.rect.y += self.speedy
    if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right \
          > WIDTH + 20:
      self.rect.x = random.randrange(WIDTH - self.rect.width)
      self.rect.y = random.randrange(-100, -40)
      self.speedy = random.randrange(1, 8)

# определения свойств спрайта пули
class Bullet(pygame.sprite.Sprite):
  def __init__(self, x, y):
    pygame.sprite.Sprite.__init__(self)
    self.image = bullet_img
    self.image.set_colorkey(BLACK)
    self.rect = self.image.get_rect()
    self.rect.bottom = y
    self.rect.centerx = x
    self.speedy = -10

  # управление спрайтами пуль
  def update(self):
    self.rect.y += self.speedy
    if self.rect.bottom < 0:
      self.kill()

# 3. Создание окна и запуск игры
pygame.init()
pygame.mixer.init()
pygame.display.set_caption("Shmup!")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
for i in range(8):
  m = Mob()
  all_sprites.add(m)
  mobs.add(m)

# 4. Цикл игры
running = True
while running:
  # 4.1 Ввод процесса (события)
  clock.tick(FPS)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        player.shoot()
  
  # 4.2 Обновление
  all_sprites.update()

  # Проверка, не ударил ли моб игрока
  hits = pygame.sprite.spritecollide(player, mobs, False)
  if hits:
    running = False

  # Проверка, не столкнулись ли пуля и моб
  hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
  for hit in hits:
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)

  # 4.3 Визуализация (сборка)
  screen.fill(BLACK)
  screen.blit(background, background_rect) # прорисовка одного изображения на другом
  all_sprites.draw(screen)
  pygame.display.flip()

# 5. Окончание игры и закрытие окна
pygame.quit()
