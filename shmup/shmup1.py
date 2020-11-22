''' Спрайт и простое движение по оси х с ограничением по краям '''
import pygame
import random
# import os

# 2. базовые настройки экрана
WIDTH = 480
HEIGHT = 600
FPS = 60 # высокое значение = плавные движения
screen = pygame.display.set_mode((WIDTH, HEIGHT))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# настройка папки ассетов
# game_folder = os.path.dirname(__file__)
# img_folder = os.path.join(game_folder, 'images')
# player_img = pygame.image.load(os.path.join(img_folder, '1.png')).convert()

# Создание спрайта - базовые настройки
class Player(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.Surface((50, 40)) # сначала прямоугольники
    self.image.fill(GREEN) # цвет спрайта
    self.rect = self.image.get_rect()
    self.rect.centerx = WIDTH / 2 # по центру
    self.rect.bottom = HEIGHT - 10 # в нижней части экрана
    self.speedx = 0 # скорость игрока по оси x

  # Движение / управление
  def update(self):
    self.speedx = 0
    keystate = pygame.key.get_pressed() # возвращает словарь со всеми клавишами
    if keystate[pygame.K_LEFT]:
      self.speedx = -8
    if keystate[pygame.K_RIGHT]:
      self.speedx = 8
    self.rect.x += self.speedx   # Движение спрайта с конкретной скоростью
    if self.rect.right > WIDTH: # установить границу справа для спрайта
      self.rect.right = WIDTH
    if self.rect.left < 0: # установить границу слева для спрайта
      self.rect.left = 0

# 3. Создание окна и запуск игры
pygame.init()
pygame.mixer.init()
pygame.display.set_caption("Shmup!")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group() # показать спрайт
player = Player()
all_sprites.add(player)

# 4. Цикл игры
running = True
while running:
  # 4.1 Ввод процесса (события)
  clock.tick(FPS) # Держим цикл на правильной скорости
  for event in pygame.event.get(): # Ввод процесса (события)
    if event.type == pygame.QUIT: # проверка для закрытия окна
      running = False
  # 4.2 Обновление
  all_sprites.update()
  # 4.3 Визуализация (сборка)
  screen.fill(BLACK)
  all_sprites.draw(screen)
  pygame.display.flip() # После отрисовки всего, переворачиваем экран

# 5. Окончание игры и закрытие окна
pygame.quit()
