#!/usr/bin/python
# -*- coding: utf-8 -*-
class Text:

    def __init__(self, tar):
        f = open(tar, 'r')
        self.content = []
        for x in f:
            sen = x.decode('utf-8')
            if sen[len(sen) - 1] == '\n':
                sen = sen[:-1]
            self.content.append(sen)
        self.pos = 0
        self.len = 0

    def out(self):
        for x in self.content:
            print x.decode('utf-8')

    def parse(self):
        while self.pos < len(self.content) \
            and len(self.content[self.pos]) == 0:
            self.pos += 1
        if self.pos >= len(self.content):
            n = (-1, u'')

            # (type, content)

            return n
        else:
            if self.content[self.pos].find('dialog') != -1:
                s = []
                self.pos += 1
                jmp, choi = map(int, self.content[self.pos].strip().split(' '))
                self.pos += 1
                im = self.content[self.pos].encode('utf-8')
                self.pos += 1
                while self.content[self.pos].find('end') != 0:
                    if len(self.content[self.pos]) != 0:
                        s.append(self.content[self.pos])
                    self.pos += 1
                self.pos += 1
                n = (0, s, jmp, choi, im)

                # (type, content, jump to, ask, image)

                return n
            elif self.content[self.pos].find('choice') != -1:
                c = []
                self.pos += 1
                cnt = 0
                while self.content[self.pos].find('end') != 0:
                    if len(self.content[self.pos]) != 0:
                        s = self.content[self.pos]
                        v = int(self.content[self.pos + 1])
                        c.append((s, cnt, v))

                        # (content, id, value)

                        cnt += 1
                    self.pos += 2
                self.pos += 1
                n = (1, c)

                # (type, pack)

                return n
            else:
                n = (-1, u'')
                return n

    def has(self):
        return len(self.content) > 0