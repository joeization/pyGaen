#!/usr/bin/python
# -*- coding: utf-8 -*-

from pygame.locals import *


class Dialog:

    def __init__(self, ct, font, chi, im, po, sf, br):
        self.content = ct
        self.font = font
        self.choi = chi
        self.image = im
        self.pos = po
        self.sf = sf
        self.branch = br
        self.bgm = False

    def blit(self, screen, pos, img, imglib, sfxlib, bgpl):
        if not self.bgm:
            if self.sf == 'STOP':
                bgpl.stop()
            elif self.sf == 'FADE':
                bgpl.fade()
            elif self.sf in sfxlib:
                bgpl.stop()
                bgpl.ld(sfxlib[self.sf])
                bgpl.play()
        screen.blit(img, pos)
        dy = 10
        cnt = 1
        for ig in self.image:
            if ig in imglib:
                screen.blit(imglib[ig], (200*cnt-imglib[ig].get_width()/2, 50))
            cnt += 1
        self.bgm = True
        for x in self.content:
            text_surface = self.font.render(x, True, (0, 0, 0))
            screen.blit(text_surface, (pos[0] + 10, pos[1] + dy))
            dy += 25

    def blitimg(self, screen, imglib):
        cnt = 1
        for ig in self.image:
            if ig in imglib:
                screen.blit(imglib[ig], (200*cnt-imglib[ig].get_width()/2, 50))
            cnt += 1

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

def whe(s):
    x = 50
    y = 75
    if s == 1:
        y = 475
    elif s == 0:
        y = 275
    return (x, y)
