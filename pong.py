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

#Change this to manipulate speed of simulation
GLOBAL_WIDTH = 640
GLOBAL_HEIGHT = 480
GLOBAL_SPEED = 200
GLOBAL_OFFSET = GLOBAL_HEIGHT / 200

#generates random number for variance in direction
def getRandomNum():
    return (random.randrange(9, 10) * .1)

#determines how to move padel based on neural net input
def movePadel(currentPosition, changeAmount):
    if changeAmount >= 6 and changeAmount <= 9:
        currentPosition -= (changeAmount ) * GLOBAL_OFFSET #move up
        if currentPosition <= 0:
            currentPosition = 0
    elif changeAmount <= 4 and changeAmount >= 0:
        currentPosition += (changeAmount + 5) * GLOBAL_OFFSET #move down
        if currentPosition >= GLOBAL_HEIGHT - 50:
            currentPosition = GLOBAL_HEIGHT - 50
    return currentPosition

#main method- magic happens here
def main():
    pygame.init()
    screen=pygame.display.set_mode((GLOBAL_WIDTH, GLOBAL_HEIGHT),0,32)
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
    #surface, color, position, radius, width
    circ = pygame.draw.circle(circ_sur,(0,255,0),(15/2,15/2),15/2)
    circle = circ_sur.convert()
    circle.set_colorkey((0,0,0))

    # x and y coordinates / speeds
    bar1_x, bar2_x = 10. , 620.
    bar1_y, bar2_y = 215. , 215.
    circle_x, circle_y = 307.5, 232.5
    bar1_move, bar2_move = 0. , 0.

    speed_x, speed_y, speed_circ = GLOBAL_SPEED, GLOBAL_SPEED, GLOBAL_SPEED

    #clock and font objects
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("calibri",40)
    count = 0

    while True: #game logic
        #Gives ability to exit
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()

        #redraws game state
        screen.blit(background,(0,0))
        frame = pygame.draw.rect(screen,(255,255,255),Rect((5,5),(630,470)),2)
        middle_line = pygame.draw.aaline(screen,(255,255,255),(330,5),(330,475))
        screen.blit(bar1,(bar1_x,bar1_y))
        screen.blit(bar2,(bar2_x,bar2_y))
        screen.blit(circle,(circle_x,circle_y))

        #movement of circle
        if count == 0:
            randArray = [-1, 1] # to randomly decide starting direction of ball
            ballDirection = randArray[random.randrange(0,2)]
            time_passed = clock.tick(30)
            time_sec = time_passed / 1000.0 * ballDirection
            count+= 1
        else:
            time_passed = clock.tick(30)
            time_sec = time_passed / 1000.0 * ballDirection
        #time_sec = .9
        circle_x += speed_x * time_sec
        circle_y += speed_y * time_sec
        ai_speed = speed_circ * time_sec
        #ai_speed = 1

        #right side AI
        #bar2_y = circle_y * getRandomNum();
        # TODO determine how to pass parameter
        bar2_y = movePadel(bar2_y, random.randrange(0, 10))
        #Left Side AI position
        #bar1_y = circle_y * getRandomNum();
        # TODO determine how to pass parameter
        bar1_y = movePadel(bar1_y, random.randrange(0, 10) )

        #Collision for left side
        if circle_x <= bar1_x + 8:
            if circle_y >= bar1_y - 7.5 and circle_y <= bar1_y + 42.5:
                circle_x = 20
                speed_x = -speed_x * getRandomNum()
                if speed_x == 0: #in case the ball gets stuck moving up and down
                        speed_x = GLOBAL_SPEED / 3

        # Collision for right side
        if circle_x >= bar2_x - 17:
            if circle_y >= bar2_y - 7.5 and circle_y <= bar2_y + 42.5:
                circle_x = 605
                speed_x = -speed_x * getRandomNum()
                if speed_x == 0: #in case the ball gets stuck moving up and down
                        speed_x = (GLOBAL_SPEED / 3) * -1

        #Increments score
        if circle_x < 5.:
            print "RIGHT AI WINS"
            exit()
        elif circle_x > 620.:
            print "LEFT AI WINS"
            exit()

        #Constrains vertical range of ball
        if circle_y <= 10.:
            speed_y = -speed_y * getRandomNum()
            circle_y = 10.
        elif circle_y >= 457.5:
            speed_y = -speed_y * getRandomNum()
            circle_y = 457.5

        pygame.display.update() #updates game

main()
