#!/usr/bin/python
# -*- coding: utf-8 -*-
from pygame.locals import *

class Dialog:

    def __init__(self, ct, font, nex, chi, im):
        self.content = ct
        self.font = font
        self.next = nex
        self.choi = chi
        self.image = im

    def blit(self, screen, pos, img, imglib):
        screen.blit(img, pos)
        dy = 10
        if self.image in imglib:
            screen.blit(imglib[self.image], (50, 50))
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