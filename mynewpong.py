#!/usr/bin/env python
# -*- coding:utf-8 -*- 
#Author: Gao hongfei
#Time: 2018.03.01

import numpy
import pygame
from pygame.locals import *
from sys import exit
import random
import pygame.surfarray as surfarray


pygame.init()

screen = pygame.display.set_mode((640,480),0,32)

#create two bars a ball and background
back = pygame.Surface((640,480))
background = back.convert()
background.fill((60,150,50))
bar = pygame.Surface((10,50))
bar1 = bar.convert()
bar1.fill((255,255,255))
bar2 = bar.convert()
bar2.fill((255,255,255))
circ_sur = pygame.Surface((15,15))
circ = pygame.draw.circle(circ_sur,(255,255,255),(int(15/2),int(15/2)),int(15/2))
circle = circ_sur.convert()
circle.set_colorkey((0,0,0))

#some parameter
bar1_x, bar2_x = 10. , 620.
bar1_y, bar2_y = 215. , 215.
circle_x, circle_y = 307.5, 232.5
bar1_move, bar2_move = 0. , 0.
speed_x, speed_y, speed_circ = 250., 250., 250.
bar1_score, bar2_score = 0,0

#clock and font objects
clock = pygame.time.Clock()
font = pygame.font.SysFont("calibri",40)


done = False
while done == False:
    ##获得键盘事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == KEYDOWN:
            if event.key == K_UP:
                bar1_move = -ai_speed
            elif event.key == K_DOWN:
                bar1_move = ai_speed
        elif event.type == KEYUP:
            if event.key == K_UP:
                bar1_move = 0.
            elif event.key == K_DOWN:
                bar1_move = 0.
    #分数框
    score1 = font.render(str(bar1_score),True,(255,255,255))
    score2 = font.render(str(bar2_score),True,(255,255,255))

    ##外边框




    #画出图形
    screen.blit(background, (0, 0))
    frame = pygame.draw.rect(screen, (255, 255, 255), Rect((5, 5), (630, 470)), 2)
    middle_frame = pygame.draw.aaline(screen, (255, 255, 255), (330, 5), (330, 475))
    screen.blit(bar1, (bar1_x, bar1_y))
    screen.blit(bar2, (bar2_x, bar2_y))
    screen.blit(circle, (circle_x, circle_y))
    screen.blit(score1,(250.,210))
    screen.blit(score2,(380.,210.))


    #移动控制
    bar1_y += bar1_move

    #movement of circle
    time_passed = clock.tick(30)
    time_sec = time_passed/1000.0

    circle_x += speed_x*time_sec
    circle_y += speed_y*time_sec
    ai_speed = speed_circ*time_sec

    #move of circle

    if circle_x >= 305:
        if not bar2_y == circle_y + 7.5:
            if bar2_y < circle_y + 7.5:
                bar2_y += ai_speed
            if bar2_y > circle_y - 42.5:
                bar2_y -= ai_speed
        else:
            bar2_y = circle_y + 7.5
    #限定最大位置
    if bar1_y >= 420.:
        bar1_y = 420.
    elif bar1_y <= 10.:
        bar1_y = 10.
    if bar2_y >= 420.: bar2_y = 420.
    elif bar2_y <= 10.:
        bar2_y = 10.

    #撞击算法
    if circle_x <= bar1_x + 10.:
        if circle_y >= bar1_y - 7.5 and circle_y <= bar1_y + 42.5:
            circle_x = 20.
            speed_x = -speed_x
    if circle_x >= bar2_x - 15.:
        if circle_y >= bar2_y - 7.5 and circle_y <= bar2_y + 42.5:
            circle_x = 605.
            speed_x = -speed_x
    if circle_x < 5.:
        bar2_score += 1
        circle_x, circle_y = 307.5, 232.5
        bar1_y, bar2_y = 215., 215.
    elif circle_x > 620:
        bar1_score += 1
        circle_x, circle_y = 307.5, 232.5
        bar1_y, bar2_y = 215., 215.
    if circle_y <= 10.:
        speed_y = -speed_y
        circle_y = 10
    elif circle_y >= 457.5:
        speed_y = -speed_y
        circle_y = 457.5

    pygame.display.update()

pygame.quit()