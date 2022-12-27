import pygame


# Inizializza pygame
pygame.init()

# Imposta le dimensioni della finestra del gioco
screen_width, screen_height = 640, 480
screen = pygame.display.set_mode((screen_width, screen_height))

# Imposta il titolo della finestra del gioco
pygame.display.set_caption('Il mio gioco')
font = pygame.font.SysFont('Arial', 36)
# Crea le opzioni del menu
menu_options = ['Inizia', 'Opzioni', 'Esci']

# Seleziona l'opzione iniziale del menu
selected_option = 0

# Avvia il ciclo principale del gioco
running = True
while running:
    # Gestisci gli eventi dell'input dell'utente
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                # Seleziona l'opzione precedente del menu
                selected_option = (selected_option - 1) % len(menu_options)
            elif event.key == pygame.K_DOWN:
                # Seleziona l'opzione successiva del menu
                selected_option = (selected_option + 1) % len(menu_options)
            elif event.key == pygame.K_RETURN:
                # Confirma la selezione dell'opzione del menu
                if menu_options[selected_option] == 'Inizia':
                    # Avvia il gioco
                    import main

                elif menu_options[selected_option] == 'Opzioni':
                    # Apri la schermata di impostazioni
                    pass
                elif menu_options[selected_option] == 'Esci':
                    # Esci dal gioco
                    running = False

    # Disegna la schermata del menu
    screen.fill((0, 0, 0))
    for i, option in enumerate(menu_options):
        if i == selected_option:
            color = (255, 255, 255)
        else:
            color = (200, 200, 200)
        text = font.render(option, True, color)
        text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2 + i * 50))
        screen.blit(text, text_rect)
    pygame.display.flip()

# Pulisci le risorse utilizzate da pygame
pygame.quit()
