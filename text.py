#!/usr/bin/python
# -*- coding: utf-8 -*-

class Text:

    def __init__(self, tar):
        f = open(tar, 'r')
        self.content = []
        for x in f:
            sen = x.decode('utf-8').strip()
            if len(sen) > 0:
                if sen[0] != '#':
                    if sen[len(sen) - 1] == '\n':
                        sen = sen[:-1]
                    self.content.append(sen)
        f.close()
        self.pos = 0
        self.len = 0

    def out(self):
        for x in self.content:
            print x.encode('utf-8')

    def parse(self):
        while self.pos < len(self.content) \
            and len(self.content[self.pos]) == 0:
            self.pos += 1
        if self.pos >= len(self.content):
            n = (-1, u'')

            # (type, content)

            return n
        else:
            if self.content[self.pos].find('dialog') == 0:
                s = []
                t, name = self.content[self.pos].strip().split(' ')
                self.pos += 1
                sfx = str(self.content[self.pos])
                self.pos += 1
                poi, fi, se = self.content[self.pos].strip().split(' ')
                self.pos += 1
                choi = str(self.content[self.pos])
                self.pos += 1
                wh = int(self.content[self.pos])
                self.pos += 1
                im = self.content[self.pos].strip().split(' ')
                self.pos += 1
                while not (self.content[self.pos].find('end') == 0 and len(self.content[self.pos]) == 3):
                    if len(self.content[self.pos]) != 0:
                        s.append(self.content[self.pos])
                    self.pos += 1
                self.pos += 1
                n = (0, s, choi, im, wh, sfx, (int(poi), fi, se), name)

                # (type, content, ask, image, where, sfx, (beanch), name)

                return n
            elif self.content[self.pos].find('choice') ==0:
                c = []
                t, name = map(str, self.content[self.pos].strip().split(' '))
                self.pos += 1
                cnt = 0
                while not (self.content[self.pos].find('end') == 0 and len(self.content[self.pos]) == 3):
                    if len(self.content[self.pos]) != 0:
                        s = self.content[self.pos].strip()
                        self.pos += 1
                        v = self.content[self.pos].strip()
                        self.pos += 1
                        w = int(self.content[self.pos])
                        self.pos += 1
                        c.append((s, cnt, v, w))

                        # (content, id, value, weight)

                        cnt += 1
                self.pos += 1
                n = (1, c, name)

                # (type, pack, name)

                return n
            else:
                n = (-1, u'')
                return n

    def has(self):
        return len(self.content) > 0
