import pygame

pygame.init()
larghezza = 800
altezza = 600


win = pygame.display.set_mode((larghezza, altezza))

pygame.display.set_caption("First Game")

nero_surface = pygame.image.load("C:/Users/GGius/PycharmProjects/VideogamePygame/imgs/nero.png")
nero_surface = pygame.transform.scale(nero_surface, (larghezza, altezza))

bg = pygame.image.load("imgs/background.png")
bg = pygame.transform.scale(bg, (800, 600))

char =  pygame.transform.scale(pygame.image.load('imgs/character.png'), (128, 128))

walkRight = [pygame.transform.scale(pygame.image.load('imgs/character.png'), (128, 128)),
             pygame.transform.scale(pygame.image.load('imgs/walks/Walk1.png'), (128, 128)), pygame.transform.scale(pygame.image.load('imgs/walks/Walk2.png'), (128, 128)),
             pygame.transform.scale(pygame.image.load('imgs/walks/Walk3.png'), (128, 128)), pygame.transform.scale(pygame.image.load('imgs/walks/Walk4.png'), (128, 128)),
             pygame.transform.scale(pygame.image.load('imgs/walks/Walk5.png'), (128, 128)), pygame.transform.scale(pygame.image.load('imgs/walks/Walk6.png'), (128, 128)),
             pygame.transform.scale(pygame.image.load('imgs/walks/Walk7.png'), (128, 128)), pygame.transform.scale(pygame.image.load('imgs/walks/Walk8.png'), (128, 128)),
             pygame.transform.scale(pygame.image.load('imgs/walks/Walk9.png'), (128, 128)), pygame.transform.scale(pygame.image.load('imgs/walks/Walk10.png'), (128, 128)),]

walkLeft = [pygame.transform.scale(pygame.image.load('imgs/Swalks/character.png'), (128, 128)),
            pygame.transform.scale(pygame.image.load('imgs/Swalks/Walk1.png'), (128, 128)), pygame.transform.scale(pygame.image.load('imgs/Swalks/Walk2.png'), (128, 128)),
            pygame.transform.scale(pygame.image.load('imgs/Swalks/Walk3.png'), (128, 128)), pygame.transform.scale(pygame.image.load('imgs/Swalks/Walk4.png'), (128, 128)),
            pygame.transform.scale(pygame.image.load('imgs/Swalks/Walk5.png'), (128, 128)), pygame.transform.scale(pygame.image.load('imgs/Swalks/Walk6.png'), (128, 128)),
            pygame.transform.scale(pygame.image.load('imgs/Swalks/Walk7.png'), (128, 128)), pygame.transform.scale(pygame.image.load('imgs/Swalks/Walk8.png'), (128, 128)),
            pygame.transform.scale(pygame.image.load('imgs/Swalks/Walk9.png'), (128, 128)), pygame.transform.scale(pygame.image.load('imgs/Swalks/Walk10.png'), (128, 128)),]

jump_frames = [ pygame.transform.scale(pygame.image.load("C:/Users/GGius/PycharmProjects/VideogamePygame/imgs/jump/Jump1.png"),(128, 128)),
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

clock = pygame.time.Clock()


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
        self.jumpc = 0
        self.walkCount = 0
        self.jumpCount = 10
        self.standing = True

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        if self.jumpc + 1 >= 27:
            self.jumpc = 0

        if not (self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1

            elif self.right:
                win.blit(walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1

        elif self.isJump:
            win.blit(jump_frames[self.jumpc //4], (self.x, self.y))
            self.jumpc += 1

        else:

            if self.right:
                win.blit(walkRight[0], (self.x, self.y))

            else:
                win.blit(walkLeft[0], (self.x, self.y))


class projectile(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


def redrawGameWindow():

    win.blit(nero_surface, (0, 0))
    win.blit(bg, (0, 0))

    man.draw(win)
    for bullet in bullets:
        bullet.draw(win)

    pygame.display.update()


# mainloop
man = player(200, 410, 64, 64)
bullets = []
run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if bullet.x < larghezza and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_r]:
        if man.left:
            facing = -1
        else:
            facing = 1

        if len(bullets) < 5:
            bullets.append(
                projectile(round(man.x + man.width // 2), round(man.y + man.height // 2), 6, (255, 255, 255), facing))

    if keys[pygame.K_a] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.standing = False

    elif keys[pygame.K_d] and man.x < larghezza - man.width - man.vel:
        man.x += man.vel
        man.right = True
        man.left = False
        man.standing = False
    else:
        man.standing = True
        man.walkCount = 0

    if not (man.isJump):
        if keys[pygame.K_w]:
            man.isJump = True
            man.right = False
            man.left = False
            man.walkCount = 0
    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) * 0.5 * neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10

    redrawGameWindow()

pygame.quit()