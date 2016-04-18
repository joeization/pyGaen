#!/usr/bin/python
# -*- coding: utf-8 -*-

from saveload import *


class Settings(object):
    '''Settings Container
    experimental setting control
    font = font
    content = setting component
    '''

    def __init__(self, ft):
        self.font = ft
        self.content = []
        self.show = False
        self.content.append(Saveload(ft))

    def blit(self, screen, imglib, mpos):
        mx = mpos[0]
        my = mpos[1]
        x = 0
        y = 0
        if mx >= x and mx <= x+50 and my >= y and my <= y+50:
            screen.blit(imglib['sey'], (0, 0))
        else:
            screen.blit(imglib['sen'], (0, 0))
        screen.blit(imglib['gear'], (0, 0))
        if self.show:
            cnt = 1
            for se in self.content:
                y += 50
                ig = []
                if mx >= x and mx <= x+50 and my >= y and my <= y+50:
                    ig.append(imglib['sey'])
                else:
                    ig.append(imglib['sen'])
                y += 50
                if mx >= x and mx <= x+50 and my >= y and my <= y+50:
                    ig.append(imglib['sey'])
                else:
                    ig.append(imglib['sen'])
                se.blit(screen, ig, ((x, y-50), (x, y)))
            cnt += 2
            #suppose that each setting has two attribute
            #can some one handle this

    def click(self, mpos, dpo, cpo, sn):

        mx = mpos[0]
        my = mpos[1]
        x = 0
        y = 0
        if mx >= x and mx <= x+50 and my >= y and my <= y+50:
            self.show = not self.show
            return (0, ())
            #0 as reverse show

        #i could not find a better way to handle settings now
        #SL
        if self.show:
            y += 50
            if mx >= x and mx <= x+50 and my >= y and my <= y+50:
                self.content[0].save(dpo, cpo, sn)
                self.show = False
                return (1, ())
                #1 as save
            y += 50
            if mx >= x and mx <= x+50 and my >= y and my <= y+50:
                loaded = self.content[0].load()
                self.show = False
                return (2, loaded)
                #2 as load
        return (-1, ())
        #-1 as NULL
