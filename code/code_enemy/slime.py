import pygame
from enemy import Enemy


# Класс врага
class Slime(Enemy):
    def __init__(self, x, y, tile_size, pad_screen, global_x, global_y, is_tile_map):
        Enemy.__init__(self, x, y, tile_size, pad_screen, global_x, global_y, is_tile_map)

        self.max_hp = 100
        self.max_mp = 100
        self.hp = 90
        self.mp = 40
        self.damage = [5, 8]

        self.anim = [pygame.image.load('../sprite/enemy/slime/2.png').convert_alpha(),
                     pygame.image.load('../sprite/enemy/slime/3.png').convert_alpha(),
                     pygame.image.load('../sprite/enemy/slime/4.png').convert_alpha(),
                     pygame.image.load('../sprite/enemy/slime/5.png').convert_alpha(),
                     pygame.image.load('../sprite/enemy/slime/6.png').convert_alpha(),
                     pygame.image.load('../sprite/enemy/slime/7.png').convert_alpha(),
                     pygame.image.load('../sprite/enemy/slime/8.png').convert_alpha(),
                     pygame.image.load('../sprite/enemy/slime/9.png').convert_alpha(),
                     pygame.image.load('../sprite/enemy/slime/10.png').convert_alpha(),
                     pygame.image.load('../sprite/enemy/slime/11.png').convert_alpha(),
                     ]
        for i in range(len(self.anim)):
            self.anim[i] = pygame.transform.scale(self.anim[i], (tile_size, tile_size))
        self.image = self.anim[0]
        self.frame = 0  # текущий кадр
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 120  # скорость обновления кадров
        self.rect = self.image.get_rect()
        self.rect.center = (x * tile_size + tile_size / 2, y * tile_size + tile_size / 2 + pad_screen)

