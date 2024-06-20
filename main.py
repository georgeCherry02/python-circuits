from circuits.examples import signal, source, simple_example, or_gate

import pygame
from pygame.locals import K_SPACE, K_m, K_w, KEYDOWN

pygame.init()

screen = pygame.display.set_mode([500, 500])

drawables = simple_example()

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
                source.inverse()
            if event.key == K_m:
                signal.inverse()

    # Fill the background with white
    screen.fill((140, 140, 140))

    # Draw components
    for drawable in or_gate():
        drawable.draw(screen)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
