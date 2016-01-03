#!/usr/bin/python
# -*- coding: utf-8 -*-

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
        sa = open('src/save.txt', 'w')
        sa.write(str(dpo) + ' ' + str(cpo) + ' ' + str(san))
        sa.close()

    def load(self):
        sa = open('src/save.txt', 'r')
        for x in sa:
            res = map(str, x.strip().split(' '))
        sa.close()
        dpo = res[0]
        cpo = res[1]
        san = int(res[2])
        return (dpo, cpo, san)
