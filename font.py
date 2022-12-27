import pygame
# Inizializza il font
font = pygame.font.Font(None, 36)

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
