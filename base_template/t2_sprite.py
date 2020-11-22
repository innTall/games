''' Pygame шаблон - скелет для нового проекта Pygame'''
''' 2. Непрерывное движение зеленого квадрата слева направо на черном экране'''
import pygame
import random

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

# Создание спрайта - базовые настройки
class Player(pygame.sprite.Sprite): # новый объект, основан на заранее
        # определенном в Pygame классе Sprite
  def __init__(self): # код, который будет запущен при создании нового объекта
        # этого типа
    pygame.sprite.Sprite.__init__(self) # запускает инициализатор встроенных
        # классов Sprite
    self.image = pygame.Surface((50, 50)) # обязательное свойство размеры image
    self.image.fill(GREEN) # цвет image
    self.rect = self.image.get_rect() # обязательное свойство rect, get_rect()
        # оценивает изображение image и высчитывает
        # прямоугольник, способный окружить его.
    self.rect.center = (WIDTH / 2, HEIGHT / 2) # создания спрайта по центру

  # Движение спрайта
  def update(self): # определить правила обновления спрайта
    self.rect.x += 5 # при каждом игровом цикле x-координата спрайта будет
        # увеличиваться на 5 пикселей
    if self.rect.left > WIDTH: # если левая сторона rect пропадает с экрана
      self.rect.right = 0 # значение правого края равное 0

# 3. Создание окна и запуск игры
pygame.init()
pygame.mixer.init()
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group() # создать группу спрайтов в игре
player = Player() # определения спрайта игрока Player
all_sprites.add(player) # добавить спрайт в группу all_sprites

# 4. Цикл игры
running = True
while running:

  # 4.1 Ввод процесса (события)
  clock.tick(FPS)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  # 4.2 Обновление
  all_sprites.update() # добавить и обновлять группу спрайтов целиком в цикл

  # 4.3 Визуализация (сборка)
  screen.fill(BLACK)
  all_sprites.draw(screen) # отрисовывать спрайты
  pygame.display.flip()
  
# 5. Окончание игры и закрытие окна
pygame.quit()
