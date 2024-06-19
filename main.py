from circuits.wire import Wire
from circuits.connection_point import ConnectionPoint

import pygame
from pygame.locals import K_SPACE, K_m, K_w, KEYDOWN

pygame.init()

screen = pygame.display.set_mode([500, 500])

source_state = False
secondary_source = False


def source_func() -> bool:
    global source_state
    return source_state


def secondary_source_func() -> bool:
    global secondary_source
    return secondary_source


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
                source_state = not source_state
            if event.key == K_m:
                secondary_source = not secondary_source

    # Fill the background with white
    screen.fill((140, 140, 140))

    # Draw a wire
    source = ConnectionPoint((10, 10), source_func)
    end = ConnectionPoint((490, 10), lambda: False)
    wire = Wire(source, end)

    another_end = ConnectionPoint((50, 50), secondary_source_func)
    second_wire = wire.extend(another_end)

    wire.draw(screen)
    second_wire.draw(screen)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
