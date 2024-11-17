import pygame as pg

from lesson_22.board import Board

pg.init()

# Высота и ширина окна
hight = 600
width = 600

FPS = 30
clock = pg.time.Clock()

# Различные переменные
BLACK = [0] * 3
GRAY = [100] * 3
WHITE = [255] * 3
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
LIGHTGREEN = (0, 200, 200)

# Основное окно
window = pg.display.set_mode((width, hight))

board = Board(width, hight, 200)

# Запускаем главный цикл
while True:
    """ Начало игровой логики  """
    # Обрабатываем события (мышки, клавиатуры...)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        if event.type == pg.MOUSEBUTTONDOWN:
            board.click(event.pos)

    # Закрашиваем фон
    window.fill('white')
    board.render(window)
    pg.display.update()

    # Различные игровые события
    keys = pg.key.get_pressed()
    if keys[pg.K_SPACE] or board.chek_end():
        pg.quit()
        exit()
    """ Конец игровой логики  """
