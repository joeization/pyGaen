#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os

def resource_path(relative):
    if hasattr(sys, "_MEIPASS"):
        # noinspection PyProtectedMember
        return os.path.join(sys._MEIPASS, relative)
    return os.path.join(relative)


class Saveload:

    def __init__(self, ft):
        self.font = ft

    def blit(self, screen, img, pos):
        screen.blit(img[0], pos[0])
        screen.blit(img[1], pos[1])

        text_surface = self.font.render(u'Save', True, (0, 0, 0))
        screen.blit(text_surface, (pos[0][0] + 5, pos[0][1] + 15))
        text_surface = self.font.render(u'Load', True, (0, 0, 0))
        screen.blit(text_surface, (pos[1][0] + 5, pos[1][1] + 15))

    def save(self, dpo, cpo, san):
        sa = open(resource_path('src/save.txt'), 'w')
        sa.write(str(dpo.encode('utf-8')) + ' ' + str(cpo.encode('utf-8')) + ' ' + str(san))
        sa.close()

    def load(self):
        sa = open(resource_path('src/save.txt'), 'r')
        for x in sa:
            res = map(str, x.strip().split(' '))
        sa.close()
        dpo = res[0].decode('utf-8')
        cpo = res[1].decode('utf-8')
        san = int(res[2])
        return (dpo, cpo, san)
