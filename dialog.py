#!/usr/bin/python
# -*- coding: utf-8 -*-

from pygame.locals import *


class Dialog(object):
    '''Dialog
    tell the story to player
    content = content

    choi = choices
    image = image(mostly a character)
    pos = image position
    sf = sfx
    branch = next dialog according to the "san"
    bmg = if we need to play the sfx
    talk = talker's name
    bkimg = background
    '''

    def __init__(self, ct, chi, im, po, sf, br, na, bk):
        self.content = ct
        self.choi = chi
        self.image = im
        self.pos = po
        self.sf = sf
        self.branch = br
        self.bgm = False
        self.talk = na
        self.bkimg = bk

        '''
        following is experimental features
        '''

        self.line = 0
        self.word = 0
        self.prevtime = -100

    def playbgm(self, sfxlib, bgpl):
        if not self.bgm:
            if self.sf == 'STOP':
                bgpl.stop()
            elif self.sf == 'FADE':
                bgpl.fade()
            elif self.sf in sfxlib:
                bgpl.stop()
                bgpl.ld(sfxlib[self.sf])
                bgpl.play()
        self.bgm = True

    def showimg(self, screen, pos, imglib):
        if self.bkimg != 'NONE':
            screen.blit(imglib[self.bkimg], (0, 0))
        screen.blit(imglib['di'], pos)
        cnt = 1
        for ig in self.image:
            if ig in imglib:
                screen.blit(imglib[ig], (200*cnt-imglib[ig].get_width()/2, 50))
            cnt += 1

    def showtext(self, screen, pos, tick, imglib, font):
        if self.line < len(self.content) and tick-self.prevtime >= 100:
            self.word += 1
            self.prevtime = tick
            if self.word >= len(self.content[self.line]):
                self.line += 1
                self.word = 0
        dy = 10
        x = 0
        while x <= self.line:
            if x < len(self.content):
                if x < self.line:
                    text_surface = font[0].render(self.content[x], True, (0, 0, 0))
                else:
                    text_surface = font[0].render(self.content[x][:self.word], True, (0, 0, 0))
                screen.blit(text_surface, (pos[0] + 10, pos[1] + dy))
                dy += 25
            x += 1
        if self.talk != 'NONE':
            screen.blit(imglib['name'], (pos[0]-10, pos[1]-25))
            text_surface = font[1].render(self.talk, True, (0, 0, 0))
            screen.blit(text_surface, (pos[0]-5, pos[1]-20))

    def blit(self, screen, pos, imglib, sfxlib, bgpl, tick, font):
        self.playbgm(sfxlib, bgpl)
        self.showimg(screen, pos, imglib)
        self.showtext(screen, pos, tick, imglib, font)

    def change_content(self, ct):
        self.content = ct

    def nxt(self):
        return self.branch[1]

    def ask(self):
        return self.choi

    def wh(self):
        return self.pos

    def next(self, sa):
        if sa >= self.branch[0]:
            return self.branch[1]
        else:
            return self.branch[2]

    def reset(self):
        self.bgm = False
        self.word = 0
        self.line = 0
        self.prevtime = -100

    def check(self):
        if self.line != len(self.content):
            self.line = len(self.content)
            return False
        else:
            return True


def whe(s):
    '''
    dialog position
    '''
    x = 50
    y = 75
    if s == 1:
        y = 475
    elif s == 0:
        y = 275
    return (x, y)
