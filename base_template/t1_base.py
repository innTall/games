''' Pygame шаблон - скелет для нового проекта Pygame'''
''' 1. Черный экран'''
# 1.	импорт необходимых библиотек
import pygame
import random

# 2. базовые настройки экрана
WIDTH = 360  # ширина игрового окна
HEIGHT = 480 # высота игрового окна
FPS = 30 # частота кадров в секунду
screen = pygame.display.set_mode((WIDTH, HEIGHT)) # screen — окно программы

WHITE = (255, 255, 255)  # Задаем цвета
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# 3. Создание окна и запуск игры
pygame.init() # команда, которая запускает pygame
pygame.mixer.init() # для звука
pygame.display.set_caption("My Game")
clock = pygame.time.Clock() # чтобы игра работала с заданной частотой кадров

# 4. Цикл игры
running = True   # для завершения игры поменять значение running на False
while running:  # цикл while, контролируемый переменной running

  # 4.1 Ввод процесса (события)
  clock.tick(FPS) # Держим цикл на правильной скорости
  for event in pygame.event.get(): # Ввод процесса (события)
    if event.type == pygame.QUIT: # check for closing window
      running = False # завершение игры

  # 4.2 Обновление

  # 4.3 Визуализация (сборка)
  screen.fill(BLACK) # Рендеринг заполнить весь экран.
  pygame.display.flip() # После отрисовки всего, переворачиваем экран
            # обязательно!!! функция flip() должна быть в конце кода
  
# 5. Окончание игры и закрытие окна
pygame.quit()
