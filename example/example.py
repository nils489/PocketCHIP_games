#!/usr/bin/env python

import sys
import pygame

pygame.init()

size = width, height = 480, 272
speed = [2,2]

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

ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()
bg = pygame.Surface(ball.get_size())
bg.fill(black)
counter = 0

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.blit(bg, ballrect)
    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    #screen.fill(colors[counter%8])
    #screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()
    counter += 1
    #pygame.time.delay(240)
