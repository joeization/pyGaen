#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
import pygame._view
from dialog import *
from choice import *
from text import *
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

font18 = pygame.font.SysFont('simhei', 18)
font24 = pygame.font.SysFont('simhei', 24)
cho = Text('src/dia.txt')
dia = Text('src/cho.txt')
ds = []
cs = []
if dia.has():
    while True:
        ne = dia.parse()

        if ne[0] == -1:
            break
        elif ne[0] == 0:
            ds.append(Dialog(ne[1], font24, ne[2], ne[3], ne[4]))
        elif ne[0] == 1:
            cc = []
            for chi in ne[1]:
                cc.append(Choice(chi[0], font18, chi[1], chi[2]))
            cs.append(cc)
if cho.has():
    while True:
        ne = cho.parse()
        
        if ne[0] == -1:
            break
        elif ne[0] == 0:
            ds.append(Dialog(ne[1], font24, ne[2], ne[3], ne[4]))
        elif ne[0] == 1:
            cc = []
            for chi in ne[1]:
                cc.append(Choice(chi[0], font18, chi[1], chi[2]))
            cs.append(cc)
if len(ds) == 0:
    exit()
dpos = 0
cpos = -1
cnex = 1
ccnt = 0
vimg = False
pick = -1
clock = pygame.time.Clock()
while True:
    (x, y) = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:
                vimg = not vimg
            if event.button == 1 and not vimg:
                if cpos != -1:
                    tmp = []
                    for c in cs[cpos]:
                        (lx, ly) = cgetpos(c.id())
                        if x >= lx and x <= lx + 350 and y >= ly and y \
                            <= ly + 50:
                            pick = c.id()
                            tmp.append(c)
                if pick != -1:
                    if len(tmp) > 0:
                        cs[cpos] = tmp
                else:
                    if ds[dpos].nxt() != -1:
                        if ds[dpos].nxt() == -2:
                            pygame.quit()
                            exit()
                        dpos = ds[dpos].nxt()
    screen.blit(imglib['bk'], (0, 0))
    if not vimg:
        ds[dpos].blit(screen, (50, 475), imglib['di'], imglib)
        cpos = ds[dpos].ask()
        if cpos != -1 and len(cs[cpos]) > 0:
            for c in cs[cpos]:
                (lx, ly) = cgetpos(c.id())
                if len(cs[cpos]) == 1 or x >= lx and x <= lx + 350 \
                    and y >= ly and y <= ly + 50:
                    c.blit(screen, (lx, ly), imglib['chiy'])
                else:
                    c.blit(screen, (lx, ly), imglib['chin'])
    pygame.display.update()
    if pick != -1:
        pygame.time.delay(300)
        dpos = cs[cpos][0].to()
        cs[cpos] = []
        cpos = -1
        pick = -1
    clock.tick(60)