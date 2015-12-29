#!/usr/bin/python
# -*- coding: utf-8 -*-
from pygame import mixer as mi

class Bgm:

    def __init__(self, sfx):
        mi.init()
        self.sf = sfx

    def ld(self, sfx):
        self.sf = sfx

    def play(self):
        mi.music.load(self.sf)
        mi.music.play(0, 0)

    def stop(self):
        mi.music.stop()

    def fade(self):
        mi.music.fadeout(1000)

if __name__ == '__main__':
    b = Bgm('sfx/battle.mp3')
    b.play()
    n = input()
    b.stop()
