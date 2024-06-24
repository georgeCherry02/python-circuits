import circuits.examples as circuits
from circuits.source import Source

import pygame
from pygame.locals import K_SPACE, K_m, K_w, KEYDOWN

pygame.init()

screen = pygame.display.set_mode([500, 500])

i1 = Source()
i2 = Source()

drawables = circuits.or_gate(i1, i2)

# Run until the user asks to quit
running = True
while running:
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_w:
                running = False
            if event.key == K_SPACE:
                i1.inverse()
            if event.key == K_m:
                i2.inverse()

    # Fill the background with white
    screen.fill((140, 140, 140))

    # Draw components
    for drawable in drawables:
        drawable.draw(screen)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
