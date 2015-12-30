#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
import pygame._view
from dialog import *
from choice import *
from text import *
from saveload import *
from bgm import *
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 600), 0, 32)
pygame.display.set_caption('alpha')
imglib = {}
imgres = open('src/img.txt', 'r')
for img in imgres:
    n, tar = map(str, img.strip().split(' '))
    i = pygame.image.load(tar).convert_alpha()
    imglib[n] = i

sfxlib = {}
sfxres = open('src/sfx.txt', 'r')
for sfx in sfxres:
    n, tar = map(str, sfx.strip().split(' '))
    sfxlib[n] = tar
sfplayer = Bgm('')

font18 = pygame.font.SysFont('simhei', 18)
font24 = pygame.font.SysFont('simhei', 24)
cho = Text('src/dia.ga')
dia = Text('src/cho.ga')
dialoglib = {}
choicelib = {}
dpos = 'main'
cpos = '-1'
vimg = False
pick = -1
clock = pygame.time.Clock()
san = 0
if dia.has():
    while True:
        ne = dia.parse()

        if ne[0] == -1:
            break
        elif ne[0] == 0:
            dialoglib[ne[7]] = (Dialog(ne[1], font24, ne[2], ne[3], ne[4], ne[5], ne[6]))
            #__init__(self, ct, font, chi, im, po, sf, br)
        elif ne[0] == 1:
            cc = []
            for chi in ne[1]:
                cc.append(Choice(chi[0], font18, chi[1], chi[2], chi[3]))
                #__init__(self, ct, font, ino, val, wei)
            choicelib[ne[2]] = cc
if cho.has():
    while True:
        ne = cho.parse()
        
        if ne[0] == -1:
            break
        elif ne[0] == 0:
            dialoglib[ne[7]]=(Dialog(ne[1], font24, ne[2], ne[3], ne[4], ne[5], ne[6]))
        elif ne[0] == 1:
            cc = []
            for chi in ne[1]:
                cc.append(Choice(chi[0], font18, chi[1], chi[2], chi[3]))
            print ne, ne[2]
            choicelib[ne[2]] = cc
if len(dialoglib) == 0:
    exit()
'''
print "Load? (y/n)"
ss = raw_input()

if ss.find('y') != -1:
    dpos, cpos = load()
'''
while True:
    (x, y) = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save(dpos, cpos)
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:
                vimg = not vimg
            if event.button == 1 and not vimg:
                if cpos != '-1':
                    tmp = []
                    for c in choicelib[cpos]:
                        (lx, ly) = cgetpos(c.id())
                        if x >= lx and x <= lx + 350 and y >= ly and y \
                            <= ly + 50:
                            pick = c.id()
                            tmp.append(c)
                if pick != -1:
                    if len(tmp) > 0:
                        choicelib[cpos] = tmp
                else:
                    if dialoglib[dpos].nxt() != '-1':
                        if dialoglib[dpos].nxt() == '-2':
                            pygame.quit()
                            exit()
                        dpos = dialoglib[dpos].next(san)
    screen.blit(imglib['bk'], (0, 0))
    if not vimg:
        dialoglib[dpos].blit(screen, whe(dialoglib[dpos].wh()), imglib['di'], imglib, sfxlib, sfplayer)
        cpos = dialoglib[dpos].ask()
        if cpos != '-1' and len(choicelib[cpos]) > 0:
            for c in choicelib[cpos]:
                (lx, ly) = cgetpos(c.id())
                if x >= lx and x <= lx + 350 \
                    and y >= ly and y <= ly + 50:
                    c.blit(screen, (lx, ly), imglib['chiy'])
                else:
                    c.blit(screen, (lx, ly), imglib['chin'])
    pygame.display.update()
    if pick != -1:
        pygame.time.delay(300)
        dpos = choicelib[cpos][0].to()
        san += choicelib[cpos][0].w()
        choicelib[cpos] = []
        cpos = -1
        pick = -1
    clock.tick(60)
