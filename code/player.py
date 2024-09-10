import pygame


# Класс игрока
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, tile_size, pad_screen, global_x, global_y):
        self.tile_size = tile_size
        self.position_x = x
        self.position_y = y
        self.global_x = global_x
        self.global_y = global_y
        self.hp = 80
        self.mp = 20
        self.max_hp = 100
        self.max_mp = 100
        self.damage = 20
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('../sprite/character/fighter_mirror.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.tile_size, self.tile_size))
        self.rect = self.image.get_rect()
        self.rect.center = (x*tile_size + tile_size / 2, y*tile_size + tile_size / 2 + pad_screen)


