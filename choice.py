#!/usr/bin/python
# -*- coding: utf-8 -*-


class Choice:
    '''
    when you are playing a game
    there must be choices
    content = content
    ino = choice id
    font = font
    value = leads to which dialog
    weight = affect the "san"
    l = text length
    '''

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
    '''
    get position of the ith choice
    '''
    return (225, 200 + i * 62.5)
