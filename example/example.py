#!/usr/bin/env python

import sys
import pygame

pygame.init()

size = width, height = 480, 272
speed = [1,1]

# color definitions
black = 0,0,0
red = 255,0,0
green = 0,255,0
blue = 0,0,255
white = 255,255,255
yellow = 255,255,0
cyan = 0,255,255
magenta = 255,0,255

colors = [black,red,green,blue,magenta,yellow,cyan,white]

screen = pygame.display.set_mode(size)

ball_image = pygame.image.load("intro_ball.gif")
ballrect = ball_image.get_rect()
ballgroup = pygame.sprite.RenderUpdates()
ball = pygame.sprite.Sprite(ballgroup)
ball.rect = ballrect
ball.image = ball_image
bg = pygame.Surface(size)
bg.fill(black)

counter = 0

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ball.rect = ball.rect.move(speed)
    if ball.rect.left < 0 or ball.rect.right > width:
        speed[0] = -speed[0]
    if ball.rect.top < 0 or ball.rect.bottom > height:
        speed[1] = -speed[1]

    #screen.fill(colors[counter%8])
    #screen.fill(black)
    #screen.blit(ball, ballrect)
    #pygame.display.flip()
    ballgroup.clear(screen, bg)
    ballgroup.draw(screen)
    pygame.display.flip()
    counter += 1
    #pygame.time.delay(240)
