#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
try:
    import pygame._view
except ImportError:
    pass
from dialog import *
from choice import *
from text import *
from settings import *
from bgm import *

pygame.init()
screen = pygame.display.set_mode((800, 600), 0, 32)
pygame.display.set_caption('alpha')
imglib = {}
imgres = open(resource_path('src/img.txt'), 'r')
for img in imgres:
    n, tar = map(str, img.strip().split(' '))
    i = pygame.image.load(resource_path(tar)).convert_alpha()
    imglib[n] = i

sfxlib = {}
sfxres = open(resource_path('src/sfx.txt'), 'r')
for sfx in sfxres:
    n, tar = map(str, sfx.strip().split(' '))
    sfxlib[n] = resource_path(tar)
sfplayer = Bgm('')

font18 = pygame.font.SysFont('simhei', 18)
font24 = pygame.font.SysFont('simhei', 24)
setting = Settings(font18)
cho = Text(resource_path('src/dia.ga'))
dia = Text(resource_path('src/cho.ga'))
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
            dialoglib[ne[7]] = (Dialog(ne[1], font24, ne[2], ne[3], ne[4], ne[5], ne[6]))
        elif ne[0] == 1:
            cc = []
            for chi in ne[1]:
                cc.append(Choice(chi[0], font18, chi[1], chi[2], chi[3]))
            print ne, ne[2]
            choicelib[ne[2]] = cc
if len(dialoglib) == 0:
    pygame.quit()
    exit()

while True:
    (x, y) = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:
                vimg = not vimg
            if event.button == 1:
                scl = setting.click((x, y), dpos, cpos, san)
                if scl[0] == 0:
                    #reverse show
                    pass
                elif scl[0] == 1:
                    #save
                    pass
                elif scl[0] == 2:
                    #load
                    dialoglib[dpos].reset()
                    dpos = scl[1][0]
                    cpos = scl[1][1]
                    san = scl[1][2]
                if not vimg and scl[0] == -1:
                    if cpos != '-1':
                        #tmp = []
                        for c in choicelib[cpos]:
                            (lx, ly) = cgetpos(c.id())
                            if x >= lx and x <= lx + 350 and y >= ly and y \
                                <= ly + 50:
                                pick = c.id()
                                #tmp.append(c)
                    if pick != -1:
                        pass
                        '''
                        if len(tmp) > 0:
                            choicelib[cpos] = tmp
                        '''
                    else:
                        if dialoglib[dpos].nxt() != '-1':
                            if dialoglib[dpos].nxt() == '-2':
                                pygame.quit()
                                exit()
                            dialoglib[dpos].reset()
                            dpos = dialoglib[dpos].next(san)
    screen.blit(imglib['bk'], (0, 0))
    setting.blit(screen, imglib, (x, y))
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
    else:
        dialoglib[dpos].blitimg(screen, imglib)
    pygame.display.update()
    if pick != -1:
        pygame.time.delay(300)
        dialoglib[dpos].reset()
        dpos = choicelib[cpos][pick].to()
        san += choicelib[cpos][pick].w()
        #choicelib[cpos] = []
        cpos = -1
        pick = -1
    clock.tick(60)
