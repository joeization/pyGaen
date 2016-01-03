#!/usr/bin/python
# -*- coding: utf-8 -*-

class Choice:

    def __init__(self, ct, font, ino, val, wei):
        self.content = ct
        self.ino = ino
        self.font = font
        self.value = val
        self.weight = wei
        self.l = (350 - len(self.content) * 15) / 2

    def blit(self, screen, pos, img):
        screen.blit(img, pos)
        text_surface = self.font.render(self.content, True, (0, 0, 0))
        screen.blit(text_surface, (pos[0] + self.l, pos[1] + 15))

    def id(self):
        return self.ino

    def to(self):
        return self.value

    def w(self):
        return self.weight

def cgetpos(i):
    return (225, 200 + i * 62.5)
