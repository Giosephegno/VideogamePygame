import pygame

walkRight = [

     pygame.transform.scale(pygame.image.load('imgs/character.png'), (128, 128)),
     pygame.transform.scale(pygame.image.load('imgs/walks/Walk1.png'), (128, 128)), pygame.transform.scale(pygame.image.load('imgs/walks/Walk2.png'), (128, 128)),
     pygame.transform.scale(pygame.image.load('imgs/walks/Walk3.png'), (128, 128)), pygame.transform.scale(pygame.image.load('imgs/walks/Walk4.png'), (128, 128)),
     pygame.transform.scale(pygame.image.load('imgs/walks/Walk5.png'), (128, 128)), pygame.transform.scale(pygame.image.load('imgs/walks/Walk6.png'), (128, 128)),
     pygame.transform.scale(pygame.image.load('imgs/walks/Walk7.png'), (128, 128)), pygame.transform.scale(pygame.image.load('imgs/walks/Walk8.png'), (128, 128)),
     pygame.transform.scale(pygame.image.load('imgs/walks/Walk9.png'), (128, 128)), pygame.transform.scale(pygame.image.load('imgs/walks/Walk10.png'), (128, 128))
]

walkRightRun = [

     pygame.transform.scale(pygame.image.load('imgs/RunWalks/Hobbit - run1.png'), (128, 128)), pygame.transform.scale(pygame.image.load('imgs/RunWalks/Hobbit - run2.png'), (128, 128)),
     pygame.transform.scale(pygame.image.load('imgs/RunWalks/Hobbit - run3.png'), (128, 128)), pygame.transform.scale(pygame.image.load('imgs/RunWalks/Hobbit - run4.png'), (128, 128)),
     pygame.transform.scale(pygame.image.load('imgs/RunWalks/Hobbit - run5.png'), (128, 128)), pygame.transform.scale(pygame.image.load('imgs/RunWalks/Hobbit - run6.png'), (128, 128)),
     pygame.transform.scale(pygame.image.load('imgs/RunWalks/Hobbit - run7.png'), (128, 128)), pygame.transform.scale(pygame.image.load('imgs/RunWalks/Hobbit - run8.png'), (128, 128)),
     pygame.transform.scale(pygame.image.load('imgs/RunWalks/Hobbit - run9.png'), (128, 128)), pygame.transform.scale(pygame.image.load('imgs/RunWalks/Hobbit - run10.png'), (128, 128))

]

walkLeftRun = [

     pygame.transform.scale(pygame.image.load('imgs/SRunWalks/Hobbit - run1.png'), (128, 128)), pygame.transform.scale(pygame.image.load('imgs/SRunWalks/Hobbit - run2.png'), (128, 128)),
     pygame.transform.scale(pygame.image.load('imgs/SRunWalks/Hobbit - run3.png'), (128, 128)), pygame.transform.scale(pygame.image.load('imgs/SRunWalks/Hobbit - run4.png'), (128, 128)),
     pygame.transform.scale(pygame.image.load('imgs/SRunWalks/Hobbit - run5.png'), (128, 128)), pygame.transform.scale(pygame.image.load('imgs/SRunWalks/Hobbit - run6.png'), (128, 128)),
     pygame.transform.scale(pygame.image.load('imgs/SRunWalks/Hobbit - run7.png'), (128, 128)), pygame.transform.scale(pygame.image.load('imgs/SRunWalks/Hobbit - run8.png'), (128, 128)),
     pygame.transform.scale(pygame.image.load('imgs/SRunWalks/Hobbit - run9.png'), (128, 128)), pygame.transform.scale(pygame.image.load('imgs/SRunWalks/Hobbit - run10.png'), (128, 128))

]

walkLeft = [

    pygame.transform.scale(pygame.image.load('imgs/Swalks/character.png'), (128, 128)),
    pygame.transform.scale(pygame.image.load('imgs/Swalks/Walk1.png'), (128, 128)), pygame.transform.scale(pygame.image.load('imgs/Swalks/Walk2.png'), (128, 128)),
    pygame.transform.scale(pygame.image.load('imgs/Swalks/Walk3.png'), (128, 128)), pygame.transform.scale(pygame.image.load('imgs/Swalks/Walk4.png'), (128, 128)),
    pygame.transform.scale(pygame.image.load('imgs/Swalks/Walk5.png'), (128, 128)), pygame.transform.scale(pygame.image.load('imgs/Swalks/Walk6.png'), (128, 128)),
    pygame.transform.scale(pygame.image.load('imgs/Swalks/Walk7.png'), (128, 128)), pygame.transform.scale(pygame.image.load('imgs/Swalks/Walk8.png'), (128, 128)),
    pygame.transform.scale(pygame.image.load('imgs/Swalks/Walk9.png'), (128, 128)), pygame.transform.scale(pygame.image.load('imgs/Swalks/Walk10.png'), (128, 128))

]

jump_frames = [

    pygame.transform.scale(pygame.image.load("C:/Users/GGius/PycharmProjects/VideogamePygame/imgs/jump/Jump1.png"),(128, 128)),
    pygame.transform.scale(pygame.image.load("C:/Users/GGius/PycharmProjects/VideogamePygame/imgs/jump/Jump2.png"),(128, 128)),
    pygame.transform.scale(pygame.image.load("C:/Users/GGius/PycharmProjects/VideogamePygame/imgs/jump/Jump3.png"),(128, 128)),
    pygame.transform.scale(pygame.image.load("C:/Users/GGius/PycharmProjects/VideogamePygame/imgs/jump/Jump4.png"),(128, 128)),
    pygame.transform.scale(pygame.image.load("C:/Users/GGius/PycharmProjects/VideogamePygame/imgs/jump/Jump5.png"),(128, 128)),
    pygame.transform.scale(pygame.image.load("C:/Users/GGius/PycharmProjects/VideogamePygame/imgs/jump/Jump6.png"),(128, 128)),
    pygame.transform.scale(pygame.image.load("C:/Users/GGius/PycharmProjects/VideogamePygame/imgs/jump/Jump7.png"),(128, 128)),
    pygame.transform.scale(pygame.image.load("C:/Users/GGius/PycharmProjects/VideogamePygame/imgs/jump/Jump8.png"),(128, 128)),
    pygame.transform.scale(pygame.image.load("C:/Users/GGius/PycharmProjects/VideogamePygame/imgs/jump/Jump9.png"),(128, 128)),
    pygame.transform.scale(pygame.image.load("C:/Users/GGius/PycharmProjects/VideogamePygame/imgs/jump/Jump10.png"),(128, 128))

]

stamina_frames = pygame.transform.scale(pygame.image.load('imgs/Stamina/11.png'),(92, 12))

class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.corsa = False
        self.jumpc = 0
        self.walkCount = 0
        self.jumpCount = 10
        self.standing = True
        self.stamina = 500


    def draw(self, win):
        if self.stamina >= 500:
            win.blit(stamina_frames, (625,58))
        if self.stamina < 500 and self.stamina >= 400:
            win.blit(pygame.transform.scale(pygame.image.load('imgs/Stamina/11.png'),(73.7, 12)), (625, 58))
        if self.stamina < 400 and self.stamina >= 300:
            win.blit(pygame.transform.scale(pygame.image.load('imgs/Stamina/11.png'),(55.3, 12)), (625, 58))
        if self.stamina < 300 and self.stamina >= 200:
            win.blit(pygame.transform.scale(pygame.image.load('imgs/Stamina/11.png'),(36.9, 12)), (625, 58))
        if self.stamina < 200 and self.stamina >= 100:
            win.blit(pygame.transform.scale(pygame.image.load('imgs/Stamina/11.png'),(18.5, 12)), (625, 58))
        if self.stamina < 100 and self.stamina >= 0:
            win.blit(pygame.transform.scale(pygame.image.load('imgs/Stamina/11.png'),(1, 12)), (625, 58))



        if self.walkCount + 1 >= 11:
            self.walkCount = 0

        if self.jumpc + 1 >= 11:
            self.jumpc = 0


        if not (self.standing):

            if self.left and self.corsa:
                win.blit(walkLeftRun[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1

            elif self.left:
                win.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1

            elif self.right and self.corsa:
                win.blit(walkRightRun[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1

            elif self.right:
                win.blit(walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1



        elif self.isJump:
            win.blit(jump_frames[self.jumpc //4], (self.x, self.y))
            self.jumpc += 1

        else:

            if self.left:
                win.blit(walkLeft[0], (self.x, self.y))

            else:
                win.blit(walkRight[0], (self.x, self.y))
