''' Спрайты врагов, непрерывный поток опускающихся мобов '''
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
    self.rect.x = random.randrange(WIDTH - self.rect.width) # x между двух сторон
    self.rect.y = random.randrange(-100, -40) # объект сверху за экраном (y < 0)
    self.speedy = random.randrange(1, 8)
    self.speedx = random.randrange(-3, 3) # добавить движения по оси х

  # управление спрайтами врагов
  def update(self):
    self.rect.x += self.speedx # определенная скорость движения право-лево
    self.rect.y += self.speedy # определенная скорость движения вниз
    if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right \
        > WIDTH + 20: # удаление спрайтов двигающихся по диагонали
      self.rect.x = random.randrange(WIDTH - self.rect.width)
      self.rect.y = random.randrange(-100, -40)
      self.speedy = random.randrange(1, 8)

# 3. Создание окна и запуск игры
pygame.init()
pygame.mixer.init()
pygame.display.set_caption("Shmup!")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group() # показать спрайт
mobs = pygame.sprite.Group()
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
  # 4.2 Обновление
  all_sprites.update()
  # 4.3 Визуализация (сборка)
  screen.fill(BLACK)
  all_sprites.draw(screen)
  pygame.display.flip()

# 5. Окончание игры и закрытие окна
pygame.quit()
