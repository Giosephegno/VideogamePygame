import pygame
import sys
import pygame.locals
import os

pygame.init()



screen = pygame.display.set_mode((800, 600))

character_image = pygame.image.load("C:/Users/GGius/PycharmProjects/VideogamePygame/imgs/character.png")

character_rect = pygame.Rect(0,  300, 128, 128)



# Carica l'immagine del background
nero_surface = pygame.image.load("C:/Users/GGius/PycharmProjects/VideogamePygame/imgs/nero.png")
nero_surface_scaled = nero_surface.copy()
nero_surface_scaled = pygame.transform.scale(nero_surface_scaled, (800, 600))

background_surface = pygame.image.load("C:/Users/GGius/PycharmProjects/VideogamePygame/imgs/background.png")
background_surface_scaled = background_surface.copy()
background_surface_scaled = pygame.transform.scale(background_surface_scaled, (800, 600))

floor_surface = pygame.image.load("C:/Users/GGius/PycharmProjects/VideogamePygame/imgs/pavimento1.png")
floor_rect = pygame.Rect(0,  400, 24,48)

# Parametri:

# Imposta la velocità del personaggio (in pixel al frame)
character_speed = 1
# Imposta ogni quanto cambiare immagine
character_image_change_speed = 7
# Indice che seleziona l'immagine nella lista
character_image_index = 0
# Serve a rallentare la velocità con la quale cambiano le immagini
current_frame = 0
## Altezza iniziale del personaggio
initial_height = character_rect.y

#
jump_speed = 2

fall_frame_count = 0
fall_speed = 5

# Determina se il personaggio sta saltando
isJump = False
jumpCount = 10

# Inizializza il contatore delle fasi del salto
jump_frame_index = 0
character_jump_change_speed = 3

character_rect.y = 320

character_images = [
    pygame.transform.scale(pygame.image.load("C:/Users/GGius/PycharmProjects/VideogamePygame/imgs/character.png"), (128, 128)),
    pygame.transform.scale(pygame.image.load("C:/Users/GGius/PycharmProjects/VideogamePygame/imgs/walks/Walk1.png"),(128, 128)),
    pygame.transform.scale(pygame.image.load("C:/Users/GGius/PycharmProjects/VideogamePygame/imgs/walks/Walk2.png"),(128, 128)),
    pygame.transform.scale(pygame.image.load("C:/Users/GGius/PycharmProjects/VideogamePygame/imgs/walks/Walk3.png"),(128, 128)),
    pygame.transform.scale(pygame.image.load("C:/Users/GGius/PycharmProjects/VideogamePygame/imgs/walks/Walk4.png"),(128, 128)),
    pygame.transform.scale(pygame.image.load("C:/Users/GGius/PycharmProjects/VideogamePygame/imgs/walks/Walk5.png"),(128, 128)),
    pygame.transform.scale(pygame.image.load("C:/Users/GGius/PycharmProjects/VideogamePygame/imgs/walks/Walk6.png"),(128, 128)),
    pygame.transform.scale(pygame.image.load("C:/Users/GGius/PycharmProjects/VideogamePygame/imgs/walks/Walk7.png"),(128, 128)),
    pygame.transform.scale(pygame.image.load("C:/Users/GGius/PycharmProjects/VideogamePygame/imgs/walks/Walk8.png"),(128, 128)),
    pygame.transform.scale(pygame.image.load("C:/Users/GGius/PycharmProjects/VideogamePygame/imgs/walks/Walk9.png"),(128, 128)),
    pygame.transform.scale(pygame.image.load("C:/Users/GGius/PycharmProjects/VideogamePygame/imgs/walks/Walk10.png"),(128, 128))

]

Scharacter_images = [
    pygame.transform.scale(pygame.image.load("C:/Users/GGius/PycharmProjects/VideogamePygame/imgs/Swalks/character.png"), (128, 128)),
    pygame.transform.scale(pygame.image.load("C:/Users/GGius/PycharmProjects/VideogamePygame/imgs/Swalks/Walk1.png"),(128, 128)),
    pygame.transform.scale(pygame.image.load("C:/Users/GGius/PycharmProjects/VideogamePygame/imgs/Swalks/Walk2.png"),(128, 128)),
    pygame.transform.scale(pygame.image.load("C:/Users/GGius/PycharmProjects/VideogamePygame/imgs/Swalks/Walk3.png"),(128, 128)),
    pygame.transform.scale(pygame.image.load("C:/Users/GGius/PycharmProjects/VideogamePygame/imgs/Swalks/Walk4.png"),(128, 128)),
    pygame.transform.scale(pygame.image.load("C:/Users/GGius/PycharmProjects/VideogamePygame/imgs/Swalks/Walk5.png"),(128, 128)),
    pygame.transform.scale(pygame.image.load("C:/Users/GGius/PycharmProjects/VideogamePygame/imgs/Swalks/Walk6.png"),(128, 128)),
    pygame.transform.scale(pygame.image.load("C:/Users/GGius/PycharmProjects/VideogamePygame/imgs/Swalks/Walk7.png"),(128, 128)),
    pygame.transform.scale(pygame.image.load("C:/Users/GGius/PycharmProjects/VideogamePygame/imgs/Swalks/Walk8.png"),(128, 128)),
    pygame.transform.scale(pygame.image.load("C:/Users/GGius/PycharmProjects/VideogamePygame/imgs/Swalks/Walk9.png"),(128, 128)),
    pygame.transform.scale(pygame.image.load("C:/Users/GGius/PycharmProjects/VideogamePygame/imgs/Swalks/Walk10.png"),(128, 128))

]


jump_frames = [ pygame.transform.scale(pygame.image.load("C:/Users/GGius/PycharmProjects/VideogamePygame/imgs/jump/Jump1.png"),(128, 128)),
                pygame.transform.scale(pygame.image.load("C:/Users/GGius/PycharmProjects/VideogamePygame/imgs/jump/Jump2.png"),(128, 128)),
                pygame.transform.scale(pygame.image.load("C:/Users/GGius/PycharmProjects/VideogamePygame/imgs/jump/Jump3.png"),(128, 128)),
                pygame.transform.scale(pygame.image.load("C:/Users/GGius/PycharmProjects/VideogamePygame/imgs/jump/Jump4.png"),(128, 128))
               ]

fall_images = [pygame.transform.scale(pygame.image.load("/imgs/jump/Jump5.png"), (128, 128)),
               pygame.transform.scale(pygame.image.load("/imgs/jump/Jump6.png"), (128, 128)),
               pygame.transform.scale(pygame.image.load("/imgs/jump/Jump7.png"), (128, 128)),
               pygame.transform.scale(pygame.image.load("/imgs/jump/Jump8.png"), (128, 128)),
               pygame.transform.scale(pygame.image.load("/imgs/jump/Jump9.png"), (128, 128)),
               pygame.transform.scale(pygame.image.load("/imgs/jump/Jump10.png"), (128, 128))]


while True:

    ## Renderizza uno sfondo nero dietro a tutto, in seguito lo sfondo degli alberi

    screen.blit(nero_surface_scaled, (0, 0))
    screen.blit(background_surface_scaled, (0, 0))

    ## Ora rederizza il pavimento

    screen.blit(floor_surface, floor_rect)
    i = 24
    while i < 800:
        screen.blit(floor_surface, (i,  400))
        i = i+24


    # Gestione degli eventi
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    keys = pygame.key.get_pressed()

    if not(isJump):

        ## Va a sinistra quando premo A
        if keys[pygame.K_a]:
            character_rect.x -= character_speed
            current_frame += 1
            if current_frame >= character_image_change_speed:
                current_frame = 0
                character_image_index += 1
            if character_image_index >= len(character_images):
                character_image_index = 0
            screen.blit(Scharacter_images[character_image_index], character_rect)

        ## Va a destra quando premo D
        elif keys[pygame.K_d]:
            character_rect.x += character_speed
            current_frame += 1
            if current_frame >= character_image_change_speed:
                current_frame = 0
                character_image_index += 1
            if character_image_index >= len(character_images):
                character_image_index = 0
            screen.blit(character_images[character_image_index], character_rect)


        else:
            character_image_index = 0
            screen.blit(character_images[character_image_index], character_rect)

        ## Salta quando premo W
        if keys[pygame.K_UP]:
            pass



    print(character_rect.y, initial_height)
    if character_rect.y < initial_height:

        current_frame += 1
        if current_frame >= character_jump_change_speed:
            current_frame = 0
            jump_frame_index += 1
        if jump_frame_index >= len(jump_frames):
            jump_frame_index = 0

        screen.blit(jump_frames[jump_frame_index], character_rect)

    if character_rect.y == initial_height:
        while character_rect.y < 320:
            current_frame += 1
            if current_frame >= character_jump_change_speed:
                current_frame = 0
                fall_frame_count += 1
            if fall_frame_count >= len(fall_images):
                fall_frame_count = 0


            character_rect.y += jump_speed
            screen.blit(fall_images[fall_frame_count % len(fall_images)], character_rect)











    pygame.display.flip()


# Pulisci le risorse utilizzate da pygame
pygame.quit()
