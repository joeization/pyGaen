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


def main():
    '''
    1. init pygame then create window
    2. load image and sfx
    3. setup sfxplayer
    4. load contents
    5. setup other stuff
    6. setup dialog flag ans choice flag
    7. run
    '''

    '''
    init pygame
    '''
    pygame.init()
    screen = pygame.display.set_mode((800, 600), 0, 32)
    pygame.display.set_caption('alpha')

    '''
    load image from dest
    tag = image tag
    tar = image path
    '''
    imglib = {}
    imgres = open(resource_path('src/img.txt'), 'r')
    for img in imgres:
        tag, tar = map(str, img.strip().split(' '))
        imglib[tag] = pygame.image.load(resource_path(tar)).convert_alpha()

    '''
    load sfx from dest
    tag = sfx tag
    tar = sfx path
    '''
    sfxlib = {}
    sfxres = open(resource_path('src/sfx.txt'), 'r')
    for sfx in sfxres:
        tag, tar = map(str, sfx.strip().split(' '))
        sfxlib[tag] = resource_path(tar)

    '''
    setup sfxplayer
    '''
    sfplayer = Bgm('')

    '''
    setup fonts
    '''
    font18 = pygame.font.SysFont('simhei', 18)
    font24 = pygame.font.SysFont('simhei', 24)

    '''
    setup settings with the font
    '''
    setting = Settings(font18)

    '''
    load and setup choice and dialog library
    '''
    cho = Text(resource_path('src/dia.ga'))
    dia = Text(resource_path('src/cho.ga'))
    dialoglib = {}
    choicelib = {}

    '''
    start from main and choice shoud be -1
    no choice is picked
    '''
    dpos = 'main'
    cpos = '-1'
    pick = -1

    '''
    image-only mode
    '''
    vimg = False

    '''
    just a clock
    '''
    clock = pygame.time.Clock()

    '''
    a value which affect the story
    '''
    san = 0

    '''
    if we have dialogs, we should load it
    '''
    if dia.has():
        while True:
            '''
            see the parse function
            '''
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

    '''
    if we have choices, we should load it
    '''
    if cho.has():
        while True:
            '''
            see the parse function
            '''
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

    '''
    there has no story
    nice work!
    '''
    if len(dialoglib) == 0:
        pygame.quit()
        sys.exit()

    '''
    main game function
    '''
    while True:
        (x, y) = pygame.mouse.get_pos()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                '''
                right click to enable/disable image-only mode
                '''
                if event.button == 3:
                    vimg = not vimg

                if event.button == 1:

                    '''
                    first we check if click on the setting menu
                    '''
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

                    '''
                    else we can let the game go through
                    '''
                    if not vimg and scl[0] == -1:
                        '''
                        player "click" on something
                        and the dialog has choices
                        '''
                        if cpos != '-1':
                            for c in choicelib[cpos]:
                                (lx, ly) = cgetpos(c.id())
                                if x >= lx and x <= lx + 350 and y >= ly and y <= ly + 50:
                                    pick = c.id()
                        '''
                        player choose the fate?
                        just pass
                        '''
                        if pick != -1:
                            pass
                        else:
                            '''
                            there has a further dialog
                            '''
                            if dialoglib[dpos].nxt() != '-1':
                                if dialoglib[dpos].nxt() == '-2':
                                    pygame.quit()
                                    sys.exit()
                                dialoglib[dpos].reset()
                                dpos = dialoglib[dpos].next(san)
        '''
        blit a background
        before we blit others
        '''
        screen.blit(imglib['bk'], (0, 0))

        '''
        not a image-only mode
        '''
        if not vimg:
            dialoglib[dpos].blit(screen, whe(dialoglib[dpos].wh()), imglib['di'], imglib, sfxlib, sfplayer, pygame.time.get_ticks())
            cpos = dialoglib[dpos].ask()
            if cpos != '-1' and len(choicelib[cpos]) > 0:
                for c in choicelib[cpos]:
                    (lx, ly) = cgetpos(c.id())
                    if x >= lx and x <= lx + 350 and y >= ly and y <= ly + 50:
                        c.blit(screen, (lx, ly), imglib['chiy'])
                    else:
                        c.blit(screen, (lx, ly), imglib['chin'])
        else:
            dialoglib[dpos].blitimg(screen, imglib)

        '''
        finally blit the settings
        and tell pygame to update
        '''
        setting.blit(screen, imglib, (x, y))
        pygame.display.update()

        '''
        go through according to player's choice
        '''
        if pick != -1:
            pygame.time.delay(300)
            dialoglib[dpos].reset()
            dpos = choicelib[cpos][pick].to()
            san += choicelib[cpos][pick].w()
            #choicelib[cpos] = []
            cpos = -1
            pick = -1

        '''
        save my computer
        '''
        clock.tick(60)

'''
if python says run, then we should run
nice work!
'''
if __name__ == '__main__':
    main()
