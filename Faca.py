import pygame
import random
from globals import SPEED, SCREEN_WIDTH, SCREEN_HEIGHT

class Faca(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images=[pygame.image.load('faca jett vento1.png').convert_alpha(),
                     pygame.image.load('faca jett vento1.png').convert_alpha(),
                     pygame.image.load('faca jett vento1.png').convert_alpha(),
                     pygame.image.load('faca jett vento1.png').convert_alpha(),
                     pygame.image.load('faca jett vento1.png').convert_alpha(),
                     pygame.image.load('faca jett vento1.png').convert_alpha(),
                     pygame.image.load('faca jett vento1.png').convert_alpha(),
                     pygame.image.load('faca jett vento1.png').convert_alpha(),
                     pygame.image.load('faca jett vento2.png').convert_alpha(),
                     pygame.image.load('faca jett vento2.png').convert_alpha(),
                     pygame.image.load('faca jett vento2.png').convert_alpha(),
                     pygame.image.load('faca jett vento2.png').convert_alpha(),
                     pygame.image.load('faca jett vento1.png').convert_alpha(),
                     pygame.image.load('faca jett vento1.png').convert_alpha(),
                     pygame.image.load('faca jett vento1.png').convert_alpha(),
                     pygame.image.load('faca jett vento1.png').convert_alpha(),
                     pygame.image.load('faca jett vento2.png').convert_alpha(),
                     pygame.image.load('faca jett vento2.png').convert_alpha(),
                     pygame.image.load('faca jett vento2.png').convert_alpha(),
                     pygame.image.load('faca jett vento2.png').convert_alpha(),]
        self.current_image = 0

        self.GRAVITY = SPEED

        self.image = pygame.image.load('faca jett vento1.png').convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)

        self.rect = self.image.get_rect()
        self.rect[0] = random.randint(0,700)
        self.rect[1] = -random.randint(400,2000)

    def update(self):
        self.current_image = (self.current_image + 1 ) % 20
        self.image = self.images[self.current_image]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect[1] += self.GRAVITY
        if self.rect[1] > 1000:
            self.rect[0] = random.randint(0, 700)
            self.rect[1] = -random.randint(400, 2000)