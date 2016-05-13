class Log():
    '''Log
    text log
    '''
    def __init__(self):
        self.content = []

    def add(self, tar):
        for s in tar:
            self.content.append(s)
        self.content = self.content[-16:]

    def blit(self, screen, font):
        z = 0
        for s in self.content:
            text_surface = font.render(s[:-1], True, (0, 0, 0))
            screen.blit(text_surface, (200, 100+z*25))
            z += 1
