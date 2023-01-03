import pygame

floor_frame = pygame.image.load("imgs/pavimento1.png")
sottoterra_frame = pygame.transform.scale(pygame.image.load("imgs/sottoterra.png"),(24,17))

class Floor(object):
    def __init__(self, y, width, height, larghezza):
        self.y = y
        self.width = width
        self.height = height
        self.larghezza = larghezza

    def draw(self, win):
        for i in range(1,self.larghezza,24):
            win.blit(floor_frame, (i,self.y))
        for i in range(1,self.larghezza,24):
            for j in range(518,600,16):
                win.blit(sottoterra_frame, (i,j))