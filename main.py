import pygame, sys
from pygame.math import Vector2

pygame.init()

GREEN = (173, 204, 96)
DARK_GREEN = (43, 51, 24)

cell_size = 30 # высота игровой сетки
number_of_cells = 25 # ширина игровой сетки

class Food:
    def __init__(self):
        self.position = Vector2(5, 6) # стартовая позиция еды


    def draw(self):
        food_rect = pygame.Rect(self.position.x * cell_size, self.position.y * cell_size, cell_size, cell_size)
        pygame.draw.rect(screen, DARK_GREEN, food_rect) # создание поля для еды (квадрата)

screen = pygame.display.set_mode((cell_size * number_of_cells, cell_size * number_of_cells)) # создание экрана с игровой сеткой

pygame.display.set_caption("Snake")

clock = pygame.time.Clock()

food = Food() # создание объекта с изображением еды
food_surface = pygame.image.load("apple.webp")

while True:
    for event in pygame.event.get(): # получаем все события с момента последнего запуска и помещаем в список
        if event .type == pygame.QUIT: # если нажали крестик - конец игры
            pygame.quit()
            sys.exit()

    # Рисование
    screen.fill(GREEN) # заполнение заднего фона зеленым цветом
    food.draw() # нарисовали квадрат еды

    pygame.display.update() # очищает экран
    clock.tick(60) # цикл while и весь код внутри будут выполняться 60 раз в секунду (частота кадров)


