import pygame
from Player import player
from Projectile import projectile

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



clock = pygame.time.Clock()

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

        if len(bullets) < 1:
            bullets.append(
                projectile(round(man.x+3 + man.width-3 // 2), round(man.y + man.height-11 // 2), 6, (255, 255, 255), facing))

    if keys[pygame.K_a] and man.x > man.vel:
        if man.stamina > 100 and man.stamina < 500 :
            man.stamina += 70
        if man.stamina < 100:
            man.stamina += 10

        man.x -= man.vel
        man.left = True
        man.right = False
        man.standing = False

    elif keys[pygame.K_d] and man.x < larghezza - man.width - man.vel and keys[pygame.K_SPACE] and man.stamina > 0:
        man.vel = 10
        print(man.stamina)
        man.stamina -= 30
        man.x += man.vel
        man.corsa = True
        man.left = False
        man.standing = False
        if man.corsa:
            man.corsa = False
            man.vel = 5


    elif keys[pygame.K_d] and man.x < larghezza - man.width - man.vel:
        if man.stamina > 100 and man.stamina < 500:
            man.stamina += 70
        if man.stamina < 100:
            man.stamina += 10

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