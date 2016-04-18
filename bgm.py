#!/usr/bin/python
# -*- coding: utf-8 -*-

from pygame import mixer as mix


class Bgm(object):
    '''Bgm player
    sfx(or bgm) player
    '''

    def __init__(self, sfx):
        mix.init()
        self.sf = sfx

    def ld(self, sfx):
        self.sf = sfx

    def play(self):
        mix.music.load(self.sf)
        mix.music.play(-1, 0)

    def stop(self):
        mix.music.stop()

    def fade(self):
        mix.music.fadeout(1500)
