import pygame


# Класс врага
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, tile_size, pad_screen, global_x, global_y, is_tile_map):
        self.position_x = x
        self.position_y = y
        self.global_x = global_x
        self.global_y = global_y
        self.tile_size = tile_size
        self.pad_screen = pad_screen
        self.is_tile_map = is_tile_map
        pygame.sprite.Sprite.__init__(self)

    def animation(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(self.anim):
                self.frame = 0
            self.image = self.anim[self.frame]

    def collision_click(self, mouse_x, mouse_y):
        if self.rect.x <= mouse_x <= self.rect.x + self.tile_size and self.rect.y <= mouse_y <= self.rect.y + self.tile_size:
            return True
        else:
            return False

