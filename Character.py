import pygame

pygame.init()
larghezza = 800
altezza = 600

win = pygame.display.set_mode((larghezza, altezza))
pygame.display.set_caption("First Game")

nero_surface = pygame.image.load("C:/Users/GGius/PycharmProjects/VideogamePygame/imgs/nero.png")
nero_surface = pygame.transform.scale(nero_surface, (larghezza, altezza))

walkRight = [pygame.transform.scale(pygame.image.load('imgs/walks/Walk1.png'), (128, 128)), pygame.transform.scale(pygame.image.load('imgs/walks/Walk2.png'), (128, 128)),
             pygame.transform.scale(pygame.image.load('imgs/walks/Walk3.png'), (128, 128)), pygame.transform.scale(pygame.image.load('imgs/walks/Walk4.png'), (128, 128)),
             pygame.transform.scale(pygame.image.load('imgs/walks/Walk5.png'), (128, 128)), pygame.transform.scale(pygame.image.load('imgs/walks/Walk6.png'), (128, 128)),
             pygame.transform.scale(pygame.image.load('imgs/walks/Walk7.png'), (128, 128)), pygame.transform.scale(pygame.image.load('imgs/walks/Walk8.png'), (128, 128)),
             pygame.transform.scale(pygame.image.load('imgs/walks/Walk9.png'), (128, 128)), pygame.transform.scale(pygame.image.load('imgs/walks/Walk10.png'), (128, 128)),]

walkLeft = [pygame.transform.scale(pygame.image.load('imgs/Swalks/Walk1.png'), (128, 128)), pygame.transform.scale(pygame.image.load('imgs/Swalks/Walk2.png'), (128, 128)),
             pygame.transform.scale(pygame.image.load('imgs/Swalks/Walk3.png'), (128, 128)), pygame.transform.scale(pygame.image.load('imgs/Swalks/Walk4.png'), (128, 128)),
             pygame.transform.scale(pygame.image.load('imgs/Swalks/Walk5.png'), (128, 128)), pygame.transform.scale(pygame.image.load('imgs/Swalks/Walk6.png'), (128, 128)),
             pygame.transform.scale(pygame.image.load('imgs/Swalks/Walk7.png'), (128, 128)), pygame.transform.scale(pygame.image.load('imgs/Swalks/Walk8.png'), (128, 128)),
             pygame.transform.scale(pygame.image.load('imgs/Swalks/Walk9.png'), (128, 128)), pygame.transform.scale(pygame.image.load('imgs/Swalks/Walk10.png'), (128, 128)),]

bg = pygame.image.load("imgs/background.png")
bg = pygame.transform.scale(bg, (800, 600))

char =  pygame.transform.scale(pygame.image.load('imgs/character.png'), (128, 128))

x = 50
y = 400
width = 40
height = 60
vel = 5

clock = pygame.time.Clock()

isJump = False
jumpCount = 10

left = False
right = False
walkCount = 0


def redrawGameWindow():
    global walkCount

    win.blit(nero_surface, (0, 0))
    win.blit(bg, (0, 0))

    if walkCount + 1 >= 27:
        walkCount = 0

    if left:
        win.blit(walkLeft[walkCount // 3], (x, y))
        walkCount += 1

    elif right:
        win.blit(walkRight[walkCount // 3], (x, y))
        walkCount += 1

    else:
        win.blit(char, (x, y))
        walkCount = 0

    pygame.display.update()


run = True


while run:
    clock.tick(27)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
        left = True
        right = False

    elif keys[pygame.K_RIGHT] and x < 500 - vel - width:
        x += vel
        left = False
        right = True

    else:
        left = False
        right = False
        walkCount = 0

    if not (isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
            left = False
            right = False
            walkCount = 0
    else:
        if jumpCount >= -10:
            y -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
        else:
            jumpCount = 10
            isJump = False



    redrawGameWindow()

pygame.quit()