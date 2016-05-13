#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
try:
    import pygame._view
except ImportError:
    pass
from choice import *
from bgm import *
from dialog import *
from settings import *
from text import *
from log import *


def main():

    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((800, 600), 0, 32)
    pygame.display.set_caption('alpha')

    imglib = {}
    imglib['load'] = pygame.image.load(resource_path('img/load.png')).convert_alpha()
    screen.blit(imglib['load'], (0, 0))
    pygame.display.update()

    imgres = open(resource_path('src/img.txt'), 'r')
    for img in imgres:
        tag, tar = map(str, img.strip().split(' '))
        imglib[tag] = pygame.image.load(resource_path(tar)).convert_alpha()

    sfxlib = {}
    sfxres = open(resource_path('src/sfx.txt'), 'r')
    for sfx in sfxres:
        tag, tar = map(str, sfx.strip().split(' '))
        sfxlib[tag] = resource_path(tar)

    sfplayer = Bgm('')

    ft18 = pygame.font.SysFont('simhei', 18)
    ft24 = pygame.font.SysFont('simhei', 24)
    ftpk = (ft24, ft18)

    setting = Settings(ft18)

    cho = Text(resource_path('src/cho.ga'))
    dia = Text(resource_path('src/dia.ga'))
    dialoglib = {}
    choicelib = {}

    dpos = 'main'
    cpos = '-1'
    pick = -1

    vmode = 0
    '''
    0 = normal
    1 = image
    2 = log
    '''

    clock = pygame.time.Clock()

    san = 0

    ddone = False

    if dia.has():
        while True:
            ne = dia.parse()

            if ne[0] == -1:
                break
            elif ne[0] == 0:
                dialoglib[ne[7]] = ne
                ddone = True
    del dia

    if cho.has():
        while True:
            ne = cho.parse()

            if ne[0] == -1:
                break
            elif ne[0] == 1:
                choicelib[ne[2]] = ne
    del cho

    if not ddone:
        pygame.quit()
        sys.exit()

    ddone = False
    cdone = False
    ce = []

    log = Log()

    while True:
        if not ddone:
            dg = Dialog(dialoglib[dpos][1], dialoglib[dpos][2], dialoglib[dpos][3],
                dialoglib[dpos][4], dialoglib[dpos][5], dialoglib[dpos][6],
                dialoglib[dpos][8], dialoglib[dpos][9])
            log.add(dg.log())
            ddone = True
            cpos = dg.ask()
        if not cdone:
            if cpos != '-1':
                ce = []
                for chi in choicelib[cpos][1]:
                    ce.append(Choice(chi[0], ft18, chi[1], chi[2], chi[3]))
            cdone = True
        (x, y) = pygame.mouse.get_pos()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                if event.button == 3:
                    if vmode == 0:
                        vmode = 3
                    elif vmode == 3:
                        vmode = 0

                if event.button == 4:
                    if vmode == 0:
                        vmode = 2

                if event.button == 5:
                    if vmode == 2:
                        vmode = 0

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
                        dg.reset()
                        dpos = scl[1][0]
                        cpos = scl[1][1]
                        san = scl[1][2]

                    if vmode == 0 and scl[0] == -1:
                        if cpos != u'-1':
                            for c in ce:
                                (lx, ly) = cgetpos(c.id())
                                if (x >= lx and x <= lx + 350 and
                                    y >= ly and y <= ly + 50):
                                    pick = c.id()
                        if pick != -1:
                            pass
                        else:
                            if dg.check():
                                if dg.nxt() != '-1':
                                    if dg.nxt() == '-2':
                                        pygame.quit()
                                        sys.exit()
                                    dg.reset()
                                    dpos = dg.next(san)
                                    ce = []
                                    ddone = False
                                    cdone = False
        screen.blit(imglib['bk'], (0, 0))
        if vmode == 0:
            dg.blit(screen, whe(dg.wh()), imglib,
                            sfxlib, sfplayer, pygame.time.get_ticks(), ftpk)
            if len(ce) > 0:
                for c in ce:
                    (lx, ly) = cgetpos(c.id())
                    if (x >= lx and x <= lx + 350 and
                        y >= ly and y <= ly + 50):
                        c.blit(screen, (lx, ly), imglib['chiy'])
                    else:
                        c.blit(screen, (lx, ly), imglib['chin'])
        else:
            dg.showimg(screen, whe(dg.wh()), imglib, False)

        if vmode == 1:
            dg.showimg(screen, whe(dg.wh()), imglib, False)
        elif vmode == 2:
            screen.blit(imglib['lg'], (200, 100))
            log.blit(screen, ft24)

        setting.blit(screen, imglib, (x, y))
        pygame.display.update()

        if pick != -1:
            pygame.time.delay(300)
            dg.reset()
            log.add(ce[pick].log())
            dpos = ce[pick].to()
            san += ce[pick].w()
            ddone = False
            cdone = False
            ce = []
            cpos = -1
            pick = -1

        clock.tick(60)

#if python says run, then we should run
if __name__ == '__main__':
    main()
