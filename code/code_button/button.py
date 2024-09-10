import pygame


class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, tile_size, pad_screen, func):
        self.tile_size = tile_size//2
        self.position_x = x
        self.position_y = y
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('../sprite/button/sword_v2.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.tile_size, self.tile_size))
        self.rect = self.image.get_rect()
        self.rect.center = (x * self.tile_size + self.tile_size / 2, y * self.tile_size + self.tile_size / 2 + pad_screen)
        self.func = func

    def collision_click(self, mouse_x, mouse_y):
        if self.rect.x <= mouse_x <= self.rect.x + self.tile_size and self.rect.y <= mouse_y <= self.rect.y + self.tile_size:
            return True
        else:
            return False
