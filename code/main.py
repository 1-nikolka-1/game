import pygame
import sys
from player import Player
from map import *
from code_enemy.slime import Slime
from code_button.button import Button


# функция для отрисовки баров игрока 1
def draw_bar_player_1(screen, obj, param):
    color_var = black
    bar_length = tile_size / 1.2
    bar_height = tile_size / 10
    pad_x = (tile_size - bar_length) / 2
    fill = 100 * bar_length
    fill_loss = 100 * bar_length
    pad_y = 0

    if param == 'hp':
        if obj.hp < 0:
            obj.hp = 0
        if obj.position_y == 0:
            pad_y = - pad_screen
        else:
            pad_y = -2 * bar_height
        color_var = red
        fill = (obj.hp / obj.max_hp) * bar_length
        fill_loss = (1 - (obj.hp / obj.max_hp)) * bar_length

    if param == 'mp':
        if obj.hp < 0:
            obj.hp = 0
        if obj.position_y == 0:
            pad_y = 1 * bar_height - pad_screen
        else:
            pad_y = -bar_height
        color_var = blue
        fill = (obj.mp / obj.max_mp) * bar_length
        fill_loss = (1 - (obj.mp / obj.max_mp)) * bar_length

    fill_loss_rect = pygame.Rect(obj.position_x*tile_size + fill+pad_x-1, obj.position_y*tile_size + pad_y + pad_screen,
                                 fill_loss, bar_height)                                   # отсутствующее хп
    outline_rect = pygame.Rect(obj.position_x*tile_size+pad_x, obj.position_y*tile_size + pad_y + pad_screen,
                               bar_length, bar_height)                                    # контур
    fill_rect = pygame.Rect(obj.position_x*tile_size+pad_x, obj.position_y*tile_size + pad_y + pad_screen,
                            fill, bar_height)                                             # хп
    pygame.draw.rect(screen, color_var, fill_rect)                                        # рисование хп
    pygame.draw.rect(screen, black, fill_loss_rect)                                       # рисование отсутствующего хп
    pygame.draw.rect(screen, color_var, outline_rect, 2)                                  # рисование контура


# Функция шага вправо
def right():
    if player.position_x < 16:
        player.rect.x += tile_size
        player.position_x += 1
    else:
        for i in enemy_sprites:
                i.rect.x -= tile_size
                i.position_x -= 1
    if map_game:
        player.global_x += 1
    elif fight_game:
        player.fight_x += 1
    chek_fight()


# Функция шага влево
def left():
    if player.position_x > 3:
        player.rect.x -= tile_size
        player.position_x -= 1
    else:
        for i in enemy_sprites:
                i.rect.x += tile_size
                i.position_x += 1
    if map_game:
        player.global_x -= 1
    elif fight_game:
        player.fight_x -= 1
    chek_fight()


# Функция шага вверх
def forward():
    if player.position_y > 2:
        player.rect.y -= tile_size
        player.position_y -= 1
    else:
        for i in enemy_sprites:
                i.rect.y += tile_size
                i.position_y += 1
    if map_game:
        player.global_y -= 1
    elif fight_game:
        player.fight_y -= 1
    chek_fight()


# Функция шага вниз
def back():
    if player.position_y < 8:
        player.rect.y += tile_size
        player.position_y += 1
    else:
        for i in enemy_sprites:
                i.rect.y -= tile_size
                i.position_y -= 1
    if map_game:
        player.global_y += 1
    elif fight_game:
        player.fight_y += 1
    chek_fight()


# Функция проверки начала боя
def chek_fight():
    global map_game
    global fight_game
    if map_game:
        for i in enemy_dict:
            if player.global_x == enemy_dict[i][0] and player.global_y == enemy_dict[i][1]:
                map_game = False
                fight_game = True
                player.fight_x = 5
                player.fight_y = 5
                player.position_x = 5
                player.position_y = 5
                player.rect.x = player.position_x*tile_size
                player.rect.y = player.position_y*tile_size + pad_screen


# Функия удара
def button_hit_def(player):
    global target
    print(next(iter(enemy_fight_dict)))
    if target.hp > 0:
        target.hp -= player.damage
    if target.hp <= 0:
        enemy_fight_sprites.remove(target)
        del enemy_fight_dict[target]
        if len(enemy_fight_dict) != 0:
            target = next(iter(enemy_fight_dict))


# Инициализация pygame
pygame.init()

# Размеры окна и сопутствующие переменные
inf = pygame.display.Info()
screen_width = inf.current_w
screen_height = inf.current_h
screen_size = [screen_width, screen_height]
map_size = [20, 11]
tile_size = screen_width/map_size[0]
pad_screen = (screen_height - (map_size[1] * tile_size))/2

screen = pygame.display.set_mode((screen_width, screen_height))

# Название игры
pygame.display.set_caption("My RPG Game")

# Переменные цвета
blue = (0, 0, 255)
red = (255, 43, 43)
black = (0, 0, 0)

# Переменные режима игры
map_game = True
fight_game = False
inventory_game = True

# Загрузка фона
background_image = {
    #    '': pygame.image.load('../').convert(),
    'Moh': pygame.image.load('../sprite/background/Moh_Ebany_1.png').convert(),
    'Water': pygame.image.load('../sprite/background/Moh_Ebany-4_png_1.png').convert(),
    'testura_peska': pygame.image.load('../sprite/background/testura_peska.png').convert(),
    'textura_dorogi': pygame.image.load('../sprite/background/textura_dorogi.png').convert(),
    'textura_travy': pygame.image.load('../sprite/background/textura_travy.png').convert(),
    'textura_vody': pygame.image.load('../sprite/background/textura_vody.png').convert(),
    'empty': pygame.image.load('../sprite/background/empty.png').convert(),
}
for image in background_image:
    background_image[image] = pygame.transform.scale(background_image[image], (tile_size, tile_size))

# Ограничение фпс
clock = pygame.time.Clock()

# Создание групп спрайтов
player_sprites = pygame.sprite.Group()
enemy_sprites = pygame.sprite.Group()
enemy_fight_sprites = pygame.sprite.Group()
button_fight_sprites = pygame.sprite.Group()
button_sprites = pygame.sprite.Group()

# создание основной карты
tile_map = create_tile_map()     # map_size[0], map_size[1]
fight_map = create_fight_map()   # map_size[0], map_size[1]

# Положение персонажа
global_x = 7
global_y = 10

# Создание персонажа и врага
enemy = Slime(12, 5, tile_size, pad_screen, 12, 10, True)
enemy1 = Slime(12, 3, tile_size, pad_screen, 12, 10, True)
enemy2 = Slime(12, 8, tile_size, pad_screen, 12, 10, True)
player = Player(7, 5, tile_size, pad_screen, global_x, global_y)

target = enemy1
enemy_dict = dict()
enemy_dict[enemy] = [enemy.global_x, global_y]

enemy_fight_dict = dict()
enemy_fight_dict[enemy1] = [enemy1.global_x, enemy1.global_y]
enemy_fight_dict[enemy2] = [enemy2.global_x, enemy2.global_y]

# Создание кнопок
button_hit = Button(24, 20, tile_size, pad_screen, button_hit_def)

# Добавление спрайтов в группы
player_sprites.add(player)
enemy_sprites.add(enemy)
enemy_fight_sprites.add(enemy1)
enemy_fight_sprites.add(enemy2)
button_fight_sprites.add(button_hit)


while True:

    # Цикл для основной карты

    while map_game:

        mouse_x, mouse_y = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_a:
                    left()
                elif event.key == pygame.K_d:
                    right()
                elif event.key == pygame.K_w:
                    forward()
                elif event.key == pygame.K_s:
                    back()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pass

        screen.fill((0, 0, 0))

        # отрисовка фона
        for x, i in enumerate(range(player.global_x-player.position_x, player.global_x-player.position_x + map_size[0])):
            for y, j in enumerate(range(player.global_y-player.position_y, player.global_y-player.position_y + map_size[1])):
                screen.blit(background_image[tile_map[i][j]], (x * tile_size, y * tile_size + pad_screen))

        player_sprites.update()
        player_sprites.draw(screen)

        enemy.animation()
        enemy_sprites.update()
        enemy_sprites.draw(screen)

        draw_bar_player_1(screen, player, 'hp')
        draw_bar_player_1(screen, player, 'mp')

        pygame.display.update()

        clock.tick(60)

    # Цикл для боя

    while fight_game:

        mouse_x, mouse_y = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_a:
                    left()
                elif event.key == pygame.K_d:
                    right()
                elif event.key == pygame.K_w:
                    forward()
                elif event.key == pygame.K_s:
                    back()
                elif event.key == pygame.K_q:
                    button_hit_def(player)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for i in button_fight_sprites:
                    if i.collision_click(mouse_x, mouse_y):
                        i.func(player)
                for i in enemy_fight_sprites:
                    if i.collision_click(mouse_x, mouse_y):
                        target = i

        screen.fill((0, 0, 0))
        # отрисовка фона
        for x, i in enumerate(
                range(player.fight_x - player.position_x, player.fight_x - player.position_x + map_size[0])):
            for y, j in enumerate(
                    range(player.fight_y - player.position_y, player.fight_y - player.position_y + map_size[1])):
                screen.blit(background_image[fight_map[i][j]], (x * tile_size, y * tile_size + pad_screen))

        player_sprites.update()
        player_sprites.draw(screen)

        for i in enemy_fight_dict:
            i.animation()

        pygame.draw.circle(screen, blue, (target.position_x * tile_size + tile_size / 2, target.position_y * tile_size + tile_size / 2 + pad_screen), tile_size//2)
        enemy_fight_sprites.update()
        enemy_fight_sprites.draw(screen)

        button_sprites.update()
        button_sprites.draw(screen)

        button_fight_sprites.update()
        button_fight_sprites.draw(screen)
        pygame.sprite.collide_rect(player, enemy)

        draw_bar_player_1(screen, player, 'hp')
        draw_bar_player_1(screen, player, 'mp')
        for i in enemy_fight_dict:
            draw_bar_player_1(screen, i, 'hp')
            draw_bar_player_1(screen, i, 'mp')

        pygame.display.update()

        clock.tick(60)

    # Цикл инвентаря

    while inventory_game:
        pass

# pygame.sprite.collide_rect(player, enemy)
