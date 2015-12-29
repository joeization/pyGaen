#!/usr/bin/python
# -*- coding: utf-8 -*-

def save(cho, dpo, cpo):
    sa = open('save.txt', 'w')
    flag = False
    for x in cho:
        if flag:
            sa.write(' ')
        flag = True
        sa.write(str(x))
    sa.write('\n')
    sa.write(str(dpo))
    sa.write('\n')
    sa.write(str(cpo))
    sa.close()
def load():
    sa = open('save.txt', 'r')
    res = []
    for x in sa:
        res.append(x)
    sa.close()
    cho = map(int, res[0].strip().split(' '))
    dpo = int(res[1])
    cpo = int(res[2])
    return (cho, dpo, cpo)