#!/usr/bin/env python
#
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.

import pygame
from pygame.locals import *
from sys import exit
import random

pygame.init()

screen=pygame.display.set_mode((640,480),0,32)
pygame.display.set_caption("Pong Simulator")

#Creating 2 bars, a ball and background.
back = pygame.Surface((640,480)) #grid
background = back.convert()
background.fill((0,0,0)) #fill with black
bar = pygame.Surface((10,50)) #make bar objet
bar1 = bar.convert() #first bar
bar1.fill((255, 255, 255)) #color
bar2 = bar.convert() #second bar
bar2.fill((255, 255, 255)) #color
circ_sur = pygame.Surface((15,15))
circ = pygame.draw.circle(circ_sur,(0,255,0),(15/2,15/2),15/2) #surface, color, position, radius, width
circle = circ_sur.convert()
circle.set_colorkey((0,0,0))

# some definitions
bar1_x, bar2_x = 10. , 620.
bar1_y, bar2_y = 215. , 215.
circle_x, circle_y = 307.5, 232.5
bar1_move, bar2_move = 0. , 0.
speed_x, speed_y, speed_circ = 250., 250., 250.
bar1_score, bar2_score = 0,0
#clock and font objects
clock = pygame.time.Clock()
font = pygame.font.SysFont("calibri",40)

while bar1_score == 0 and bar2_score == 0:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    score1 = font.render(str(bar1_score), True,(255,255,255))
    score2 = font.render(str(bar2_score), True,(255,255,255))

    screen.blit(background,(0,0))
    frame = pygame.draw.rect(screen,(255,255,255),Rect((5,5),(630,470)),2)
    middle_line = pygame.draw.aaline(screen,(255,255,255),(330,5),(330,475))
    screen.blit(bar1,(bar1_x,bar1_y))
    screen.blit(bar2,(bar2_x,bar2_y))
    screen.blit(circle,(circle_x,circle_y))
    screen.blit(score1,(250.,210.))
    screen.blit(score2,(380.,210.))

    #movement of circle
    time_passed = clock.tick(30)
    time_sec = time_passed / 1000.0

    circle_x += speed_x * time_sec
    circle_y += speed_y * time_sec
    #ai_speed = speed_circ * time_sec
    ai_speed = 1

    #right side AI
    bar2_y = circle_y * (random.randrange(9, 10) * .1);

    #Left Side AI position
    bar1_y = circle_y * (random.randrange(9, 10) * .1);

    #Collision
    if circle_x <= bar1_x + 8:
        if circle_y >= bar1_y - 7.5 and circle_y <= bar1_y + 42.5:
            circle_x = 20.
            # TODO add randomness here
            speed_x = -speed_x
    if circle_x >= bar2_x - 17:
        if circle_y >= bar2_y - 7.5 and circle_y <= bar2_y + 42.5:
            circle_x = 605.
            # TODO add randomness here
            speed_x = -speed_x
    #never executed??
    if circle_x < 5.:
        bar2_score += 1
        circle_x, circle_y = 320., 232.5
        bar1_y,bar2_y = 215., 215.
    elif circle_x > 620.:
        bar1_score += 1
        circle_x, circle_y = 307.5, 232.5
        bar1_y, bar2_y = 215., 215.
    if circle_y <= 10.:
        speed_y = -speed_y
        circle_y = 10.
    elif circle_y >= 457.5:
        speed_y = -speed_y
        circle_y = 457.5

    pygame.display.update()
