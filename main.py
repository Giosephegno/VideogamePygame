import pygame
import sys
import pygame.locals
import os

pygame.init()



screen = pygame.display.set_mode((800, 600))

character_image = pygame.image.load("C:/Users/GGius/PycharmProjects/VideogamePygame/imgs/character.png")
character_rect = pygame.Rect(0,  200, 64, 64)



# Carica l'immagine del background
nero_surface = pygame.image.load("C:/Users/GGius/PycharmProjects/VideogamePygame/imgs/nero.png")
nero_surface_scaled = nero_surface.copy()
nero_surface_scaled = pygame.transform.scale(nero_surface_scaled, (800, 600))

background_surface = pygame.image.load("C:/Users/GGius/PycharmProjects/VideogamePygame/imgs/background.png")
background_surface_scaled = background_surface.copy()
background_surface_scaled = pygame.transform.scale(background_surface_scaled, (800, 600))

floor_surface = pygame.image.load("C:/Users/GGius/PycharmProjects/VideogamePygame/imgs/pavimento1.png")
floor_rect = pygame.Rect(0,  400, 24,48)



# Imposta la velocità del personaggio (in pixel al frame)
character_speed = 1
character_image_change_speed = 7
character_image_index = 0
current_frame = 0
jump_speed = 2
fall_speed = 5

# Determina se il personaggio sta saltando
jumping = False

# Inizializza il contatore delle fasi del salto
jump_frame_index = 0
character_jump_change_speed = 8
# Determina la massima altezza del salto
max_jump_height = 250



character_images = [
    pygame.image.load("C:/Users/GGius/PycharmProjects/VideogamePygame/imgs/character.png"),
    pygame.image.load("C:/Users/GGius/PycharmProjects/VideogamePygame/imgs/walks/Walk1.png"),
    pygame.image.load("C:/Users/GGius/PycharmProjects/VideogamePygame/imgs/walks/Walk2.png"),
    pygame.image.load("C:/Users/GGius/PycharmProjects/VideogamePygame/imgs/walks/Walk3.png"),
    pygame.image.load("C:/Users/GGius/PycharmProjects/VideogamePygame/imgs/walks/Walk4.png"),
    pygame.image.load("C:/Users/GGius/PycharmProjects/VideogamePygame/imgs/walks/Walk5.png"),
    pygame.image.load("C:/Users/GGius/PycharmProjects/VideogamePygame/imgs/walks/Walk6.png"),
    pygame.image.load("C:/Users/GGius/PycharmProjects/VideogamePygame/imgs/walks/Walk7.png"),
    pygame.image.load("C:/Users/GGius/PycharmProjects/VideogamePygame/imgs/walks/Walk8.png")

]

jump_frames = [pygame.image.load("C:/Users/GGius/PycharmProjects/VideogamePygame/imgs/jump/Jump1.png"),
               pygame.image.load("C:/Users/GGius/PycharmProjects/VideogamePygame/imgs/jump/Jump2.png"),
               pygame.image.load("C:/Users/GGius/PycharmProjects/VideogamePygame/imgs/jump/Jump3.png"),
               pygame.image.load("C:/Users/GGius/PycharmProjects/VideogamePygame/imgs/jump/Jump4.png"),
               pygame.image.load("C:/Users/GGius/PycharmProjects/VideogamePygame/imgs/jump/Jump5.png"),
               pygame.image.load("C:/Users/GGius/PycharmProjects/VideogamePygame/imgs/jump/Jump6.png")
               ]

while True:

    # Gestione degli eventi
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:

            # Se il personaggio non sta già saltando, inizia il salto
            if not jumping:
                jumping = True
                # Imposta la velocità di salto
                jump_velocity = -2
                # Imposta il contatore delle fasi del salto su 0
                jump_frame_index = 0


            elif event.type == pygame.KEYUP and event.key == pygame.K_SPACE:

                # Se il personaggio è ancora in aria, interrompi il salto
                if jumping:
                    jumping = False

    if jumping:
        # Aggiorna la posizione del personaggio in base alla velocità di salto
        character_rect.y += jump_velocity

        # Se il personaggio ha raggiunto l'altezza massima del salto, interrompi il salto
        if character_rect.y <= max_jump_height:
            jumping = False
            jump_velocity = 2
    else:
        # Se il personaggio è a terra, reimposta la posizione iniziale
        character_rect.y = 340

    if jumping:

        current_frame += 1

        if current_frame >= character_jump_change_speed:

            current_frame = 0
            jump_frame_index += 1

        if jump_frame_index >= len(jump_frames):
            jump_frame_index = 0



    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
        character_rect.x -= character_speed

    if keys[pygame.K_d]:

        # Muovi il personaggio a destra
        character_rect.x += character_speed
        current_frame += 1

        if current_frame >= character_image_change_speed:
            current_frame = 0
            character_image_index += 1

        if character_image_index >= len(character_images):
            character_image_index = 0

    if event.type == pygame.KEYUP and event.key == pygame.K_d:
        character_image_index = 0


    screen.blit(nero_surface_scaled, (0, 0))
    screen.blit(background_surface_scaled, (0, 0))
    screen.blit(floor_surface, floor_rect)
    i = 24
    while i < 800:
        screen.blit(floor_surface, (i,  400))
        i = i+24

    if character_rect.colliderect(floor_rect):
        fall_speed = 0
    else:
        character_rect.top += fall_speed

    # Disegno del personaggio e del terreno sullo schermo

    if not jumping:
        screen.blit(character_images[character_image_index], character_rect)
    else:
        screen.blit(jump_frames[jump_frame_index], character_rect)
    pygame.display.flip()


# Pulisci le risorse utilizzate da pygame
pygame.quit()
