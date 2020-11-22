''' Pygame шаблон - скелет для нового проекта Pygame'''
''' 3. Непрерывное движение sprite слева направо на зеленом экране'''
import pygame
import random
import os # Чтобы игра работала на любом устройстве

# 2. базовые настройки экрана
WIDTH = 360
HEIGHT = 480
FPS = 30
screen = pygame.display.set_mode((WIDTH, HEIGHT))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# настройка папки ассетов
game_folder = os.path.dirname(__file__) # указать, где находится игра
img_folder = os.path.join(game_folder, 'images') # местоположение папки 'img'
player_img = pygame.image.load(os.path.join(img_folder, '1.png')).convert()

# Создание спрайта - базовые настройки
class Player(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.image = player_img # Замена зеленого квадрата на изображение персонажа
    self.image.set_colorkey(BLACK) # игнорирование ненужных пикселей
    self.rect = self.image.get_rect() # теперь прямоугольник будет окружать любое
        # изображение self.image
    self.rect.center = (WIDTH / 2, HEIGHT / 2)

  # Движение спрайта
  def update(self):
    self.rect.x += 5
    if self.rect.left > WIDTH:
      self.rect.right = 0

# 3. Создание окна и запуск игры
pygame.init()
pygame.mixer.init()
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

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
  screen.fill(GREEN)
  all_sprites.draw(screen) # отрисовывать спрайты
  pygame.display.flip()

# 5. Окончание игры и закрытие окна
pygame.quit()
