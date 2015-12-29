#!/usr/bin/python
# -*- coding: utf-8 -*-

def save(dpo, cpo):
    sa = open('save.txt', 'w')
    sa.write(str(dpo) + ' ' + str(cpo))
    sa.close()
def load():
    sa = open('save.txt', 'r')
    for x in sa:
        res = map(int, raw_input().strip().split(' '))
    sa.close()
    dpo = int(res[0])
    cpo = int(res[1])
    return (dpo, cpo)