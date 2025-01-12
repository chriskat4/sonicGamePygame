import random
import time
import pygame
import Player
import Faca
from pygame.locals import *
from globals import SPEED, SCREEN_WIDTH, SCREEN_HEIGHT
#import _pyinstaller_hooks_contrib

pygame.display.set_caption('Chrizotron')

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
BACKGROUND = pygame.image.load('catedral game.png')
KABUM = pygame.image.load('kabum.png')

player_group = pygame.sprite.Group()
player = Player.Player()
player_group.add(player)

faca_group = pygame.sprite.Group()
faca = Faca.Faca()
faca1 = Faca.Faca()
faca2 = Faca.Faca()
faca3 = Faca.Faca()
faca4 = Faca.Faca()
faca_group.add(faca)
faca_group.add(faca1)
faca_group.add(faca2)
faca_group.add(faca3)
faca_group.add(faca4)

clock=pygame.time.Clock()


open_window = True
while open_window:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            open_window = False

    keys=pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
            player.walk_left()
    if keys[pygame.K_RIGHT]:
            player.walk_right()




    screen.blit(BACKGROUND, (0, 0))


    player_group.update()
    faca_group.update()

    player_group.draw(screen)
    faca_group.draw(screen)

    pygame.display.update()
    if (pygame.sprite.groupcollide(player_group, faca_group, False, False, pygame.sprite.collide_mask)):
        screen.blit(KABUM, (0, 0))
        time.sleep(0.4)
        pygame.display.update()
        time.sleep(4)
        break

pygame.quit()
