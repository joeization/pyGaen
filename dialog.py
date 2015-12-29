#!/usr/bin/python
# -*- coding: utf-8 -*-
from pygame.locals import *

class Dialog:

    def __init__(self, ct, font, nex, chi, im, po, sf):
        self.content = ct
        self.font = font
        self.next = nex
        self.choi = chi
        self.image = im
        self.pos = po
        self.sf = sf
        self.bgm = False

    def blit(self, screen, pos, img, imglib, sfxlib, bgpl):
        screen.blit(img, pos)
        dy = 10
        if self.image in imglib:
            screen.blit(imglib[self.image], (400-imglib[self.image].get_width()/2, 50))
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
        for x in self.content:
            text_surface = self.font.render(x, True, (0, 0, 0))
            screen.blit(text_surface, (pos[0] + 10, pos[1] + dy))
            dy += 25

    def change_content(self, ct):
        self.content = ct

    def nxt(self):
        return self.next

    def ask(self):
        return self.choi

    def wh(self):
        return self.pos

def whe(s):
    x = 50
    y = 75
    if s == 1:
        y = 475
    elif s == 0:
        y = 275
    return (x, y)