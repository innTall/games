''' Столкновения и стрельба '''
import pygame
import random

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

# Создание спрайта - базовые настройки
class Player(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.Surface((50, 40))
    self.image.fill(GREEN)
    self.rect = self.image.get_rect()
    self.rect.centerx = WIDTH / 2
    self.rect.bottom = HEIGHT - 10
    self.speedx = 0

  # создание пули, с местом появления из середины верхней части игрока
  def shoot(self):
    bullet = Bullet(self.rect.centerx, self.rect.top)
    all_sprites.add(bullet) # для отрисовки и обновлений
    bullets.add(bullet) # для столкновений

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
    self.image = pygame.Surface((30, 40))
    self.image.fill(RED)
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
    self.image = pygame.Surface((10, 20))
    self.image.fill(YELLOW)
    self.rect = self.image.get_rect()
    self.rect.bottom = y # указание спрайту где появляться
    self.rect.centerx = x
    self.speedy = -10 # минус - потому что двигаются вверх

  # управление спрайтами пуль
  def update(self):
    self.rect.y += self.speedy
    if self.rect.bottom < 0: # убить, если он заходит за верхнюю часть экрана
      self.kill()

# 3. Создание окна и запуск игры
pygame.init()
pygame.mixer.init()
pygame.display.set_caption("Shmup!")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group() # показать спрайт
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group() # добавить группу для пуль
player = Player()
all_sprites.add(player)
for i in range(8): # вызвать определенное количество мобов
  m = Mob()
  all_sprites.add(m) # добавить мобов в группы
  mobs.add(m)

# 4. Цикл игры
running = True
while running:
  # 4.1 Ввод процесса (события)
  clock.tick(FPS)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.KEYDOWN: # проверка состояния кнопки
      if event.key == pygame.K_SPACE: # нажатие на пробел = выстрел
        player.shoot()

  # 4.2 Обновление
  all_sprites.update()
  
  # Проверка, не ударил ли моб игрока
  hits = pygame.sprite.spritecollide(player, mobs, False)
  if hits: # если hits > 0, то if = True
    running = False # игра закончится

  # Проверка, не столкнулись ли пуля и моб
  hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
  for hit in hits:
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)

  # 4.3 Визуализация (сборка)
  screen.fill(BLACK)
  all_sprites.draw(screen)
  pygame.display.flip()

# 5. Окончание игры и закрытие окна
pygame.quit()
