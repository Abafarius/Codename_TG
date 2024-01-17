import pygame as pg
import sys

pg.init()

# Определение цветов
WHITE = (255, 255, 255)

# Инициализация окна
width, height = 1024, 768
screen = pg.display.set_mode((width, height))
pg.display.set_caption("Magic Mastery Boss")
icon = pg.image.load('resources/icons/robe.png')
pg.display.set_icon(icon)
# bg1 = pg.image.load("resources/background/dunge.png")
# bg1 = pg.transform.scale(bg1, (bg1.get_width()*4, bg1.get_height()*4))
# x, y, bg_width, bg_height = 0, 0, 340, 376
# bg1 = bg1.subsurface((x, y, bg_width, bg_height))
# bg2 = pg.image.load("resources/background/dungeon_tiles.png")
# bg2 = pg.transform.scale(bg2, (bg2.get_width()*2, bg2.get_height()*2))
# bg2 = bg2.subsurface((230, 0, 100, 180))
# bg3 = pg.image.load("resources/background/dungeon_tiles.png")
# bg3 = pg.transform.scale(bg3, (bg3.get_width()*3, bg3.get_height()*3))
# bg3 = bg3.subsurface((500, 0, 195, 240))
bg1 = pg.image.load("resources/background/BG1.png")
bg1 = pg.transform.scale(bg1, (bg1.get_width()*1.6, bg1.get_height()*1.2))

# Загрузка спрайта
sprite_sheet = pg.image.load("resources/GG_mage/new_img/mage-dark.png")

# Разделение спрайта на кадры
sprite_width, sprite_height = 45, 64
sprite_sheet = pg.transform.scale(sprite_sheet, (sprite_sheet.get_width()*2, sprite_sheet.get_height()*2))
frames = {
    "up": [sprite_sheet.subsurface((i * sprite_width, 0, sprite_width, sprite_height)) for i in range(3)],
    "down": [sprite_sheet.subsurface((i * sprite_width, 2 * sprite_height, sprite_width, sprite_height)) for i in range(3)],
    "left": [sprite_sheet.subsurface((i * sprite_width, 3 * sprite_height, sprite_width, sprite_height)) for i in range(3)],
    "right": [sprite_sheet.subsurface((i * sprite_width, sprite_height, sprite_width, sprite_height)) for i in range(3)],
}

# Начальные координаты и скорость движения
player_x, player_y = 400, 300
speed = 22
current_direction = "down"
current_frame = 0

# Главный цикл программы
clock = pg.time.Clock()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    keys = pg.key.get_pressed()

    # Обновление координат мага в зависимости от нажатых клавиш
    if keys[pg.K_UP]:
        player_y -= speed
        current_direction = "up"
    elif keys[pg.K_DOWN]:
        player_y += speed
        current_direction = "down"
    elif keys[pg.K_LEFT]:
        player_x -= speed
        current_direction = "left"
    elif keys[pg.K_RIGHT]:
        player_x += speed
        current_direction = "right"

    # Отрисовка фона и спрайта мага
    # screen.blit(bg1, (340, 250))
    # screen.blit(bg1, (340, 0))
    # screen.blit(bg2, (460, 50))
    # screen.blit(bg3, (360, 220))
    # screen.blit(bg2, (520, 380))
    screen.blit(bg1, (0, 0))
    screen.blit(frames[current_direction][current_frame], (player_x, player_y))

    # Анимация: переключение кадров
    current_frame = (current_frame + 1) % len(frames[current_direction])

    pg.display.flip()
    clock.tick(10)  # Установите частоту обновления кадров


