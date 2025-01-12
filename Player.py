import pygame
from globals import SPEED, SCREEN_WIDTH


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.images=[pygame.image.load('sonic.png').convert_alpha(),
                     pygame.image.load('sonic.png').convert_alpha(),
                     pygame.image.load('sonic.png').convert_alpha(),
                     pygame.image.load('sonic.png').convert_alpha(),
                     pygame.image.load('sonic.png').convert_alpha(),
                     pygame.image.load('sonic.png').convert_alpha(),
                     pygame.image.load('sonic.png').convert_alpha(),
                     pygame.image.load('sonic.png').convert_alpha(),
                     pygame.image.load('sonic2.png').convert_alpha(),
                     pygame.image.load('sonic2.png').convert_alpha(),
                     pygame.image.load('sonic2.png').convert_alpha(),
                     pygame.image.load('sonic2.png').convert_alpha(),
                     pygame.image.load('sonic2.png').convert_alpha(),
                     pygame.image.load('sonic2.png').convert_alpha(),
                     pygame.image.load('sonic2.png').convert_alpha(),
                     pygame.image.load('sonic2.png').convert_alpha(),]

        self.current_image = 0
        self.speed = SPEED

        self.image = pygame.image.load('sonic.png').convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)

        self.rect = self.image.get_rect()
        self.rect[0] = SCREEN_WIDTH / 2
        self.rect[1] = 450

    def update(self):
        self.current_image = (self.current_image + 1 ) % 16
        self.image = self.images[self.current_image]
        self.mask = pygame.mask.from_surface(self.image)
    def walk_right(self):
        if self.rect[0] < 700:
            self.rect[0]+=self.speed
    def walk_left(self):
        if self.rect[0] > 0:
            self.rect[0]-=self.speed
