#!/usr/bin/python
# -*- coding: utf-8 -*-


class Text:

    def __init__(self, tar):
        '''
        to parse a dialog/choice file
        it is not necessary to separate into 2 files
        first we need to load the text
        '''
        f = open(tar, 'r')
        self.content = []
        for x in f:
            sen = x.decode('utf-8').strip()
            if len(sen) > 0:
                '''
                leading # is for comments
                just like python
                '''
                if sen[0] != '#':
                    if sen[len(sen) - 1] == '\n':
                        sen = sen[:-1]
                    self.content.append(sen)
        f.close()
        self.pos = 0
        self.len = 0

    def parse(self):
        '''
        parse the text file to dialog or choice file
        the code is very dirty
        '''
        while self.pos < len(self.content) and len(self.content[self.pos]) == 0:
            self.pos += 1

        #EOF
        if self.pos >= len(self.content):
            n = (-1, u'')
            # (type, content)
            return n

        else:
            if self.content[self.pos].find('dialog') == 0:
                '''
                dialog
                name = dialog tag
                sfx = sfx
                poi = san threshold
                fi = jmp to fi if less than
                se = jmp to se else
                choi = choice tag
                wh = dialog position
                im = dialog image
                na = talker's name
                bk = background
                '''
                s = []
                t, name = self.content[self.pos].strip().split(' ')
                self.pos += 1
                na = self.content[self.pos]
                self.pos += 1
                sfx = str(self.content[self.pos])
                self.pos += 1
                poi, fi, se = self.content[self.pos].strip().split(' ')
                self.pos += 1
                choi = str(self.content[self.pos])
                self.pos += 1
                wh = long(self.content[self.pos])
                self.pos += 1
                im = self.content[self.pos].strip().split(' ')
                self.pos += 1
                bk = self.content[self.pos]
                self.pos += 1

                '''
                load content until end
                '''
                while not (self.content[self.pos].find('end') == 0 and len(self.content[self.pos]) == 3):
                    if len(self.content[self.pos]) != 0:
                        s.append(self.content[self.pos])
                    self.pos += 1
                self.pos += 1

                '''
                create a dialog
                '''
                n = (0, s, choi, im, wh, sfx, (long(poi), fi, se), name, na, bk)

                # (type, content, ask, image, where, sfx, (beanch), name)

                return n

            elif self.content[self.pos].find('choice') == 0:
                '''
                choice
                name = choice tag
                c = options
                '''
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
                        w = long(self.content[self.pos])
                        self.pos += 1
                        c.append((s, cnt, v, w))

                        # (content, id, value, weight)

                        cnt += 1
                self.pos += 1
                n = (1, c, name)

                # (type, pack, name)

                return n
            else:
                '''
                other trash
                '''
                n = (-1, u'')
                return n

    def has(self):
        return len(self.content) > 0
