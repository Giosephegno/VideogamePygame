"""
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
    character_rect.y = 320

if jumping:

    current_frame += 1

    if current_frame >= character_jump_change_speed:
        current_frame = 0
        jump_frame_index += 1

    if jump_frame_index >= len(jump_frames):
        jump_frame_index = 0
"""

if character_rect.y < initial_height - (2 * character_rect.height):
    # Stoppa il salto
    character_rect.y = initial_height - (2 * character_rect.height)

if character_rect.y == character_rect.top + 50:
    # Incrementa il contatore dei frame
    fall_frame_count += 1

    # Mostra l'immagine corrispondente al frame corrente
    screen.blit(fall_images[fall_frame_count % len(fall_images)], character_rect)